from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from common import mysql_operate,mysql_pooldb
from common.json_response import JsonResponse
from common.json_flask import JsonFlask
import  json


# #创建Flask对象app并初始化
app =JsonFlask(__name__)
# #解决跨域问题
# CORS(app, supports_credentials=True)
# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.after_request(after_request)
#主函数

#写好的数据库连接函数，传入的是Table，数据表的名称
#返回值是数据表中所有的数据，以元组返回

#查询信息
def get_Table_Data(table1,table2):
    sql = 'SELECT *FROM '+table1+' ,' +table2+' where '+table1+'.station_code ='+table2+'.station_code and DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(create_date)' # 获取所有信息
    # res=mysql_operate.db.select_db(sql)
    res =mysql_pooldb.db.getAll(sql)
    return res

def get_Latest_Data(table):
    sql = 'SELECT *FROM '+table+" order by create_date desc limit 1"  # 获取所有信息
    res=mysql_pooldb.db.getOne(sql)
    return res

def getData(table):
    sql = 'SELECT * FROM '+table+" where DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(create_date)"  # 获取所有信息
    res=mysql_operate.db.select_db(sql)
    return res

#修改信息
def Update_Table_Data(Table,id):
    sql = "SELECT * FROM "+Table+ "WHERE info_id =" + id
    data = mysql_operate.db.select_db(sql)
    if data:
        newsql = ("update "+Table+" set  water_temperature='%s',ph='%s',conductance='%s',"
                  "DO='%s',turbidity='%s',chl-a='%s',total_phosphorus='%s',total_nitrogen='%s' WHERE info_id=" + id)
        mysql_operate.db.execute_db(newsql)
        return True
    else:
        return False

#删除信息
def Delete_Table_Data(Table,id):
    sql = "SELECT * FROM "+Table+" WHERE info_id =" + id
    data = mysql_operate.db.select_db(sql)
    if data:
        newsql = "DELETE FROM "+Table+"WHERE info_id =" + id
        mysql_operate.db.execute_db(newsql)
        return  True
    else:
        return False

# #通过python装饰器的方法定义路由地址
@app.route("/",methods=["GET","POST"])
# #定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def root():
    return render_template("index.html")

@app.route("/all",methods=["GET","POST"])
def get_all_info():
    res=get_Table_Data('tb_monitoring_info','tb_monitoring_station')

    return JsonResponse.success(msg="查询成功",data=res)

@app.route("/query",methods=["GET","POST"])
def getinfo():
    res=get_Latest_Data('tb_monitoring_info')
    return JsonResponse.success(msg="查询成功",data=res)

@app.route("/update",methods=["PUT"])
def update():
    # "修改信息"
    data=json.loads(request.data)
    if 'id' not in data:
        return JsonResponse.fail(msg="需要传入id")
    isOk=Update_Table_Data("tb_monitoring_info",data['id'])
    return JsonResponse.success(msg="修改成功") if isOk else JsonResponse.fail(msg="修改失败")


@app.route("/delete", methods=["DELETE"])
def delete():
    if 'id' not in request.args:
        return JsonResponse.fail(msg="需要传入id")
    isOk=Delete_Table_Data("tb_monitoring_info",request.args['id'])
    return JsonResponse.success(msg="删除成功") if isOk else JsonResponse.fail(msg="删除失败")


#获取一周数据
@app.route("/queryweek", methods=["GET"])
def get_weekdata():
    res=getData('tb_monitoring_info')
    return JsonResponse.success(msg="查询成功",data=res)

#获取站点数量
@app.route("/querysitenum", methods=["GET"])
def get_sitenum():
    sql = 'SELECT COUNT(station_id) FROM tb_monitoring_station'
    res = mysql_operate.db.select_db(sql)
    return JsonResponse.success(msg="查询成功", data=res)

#获取站点数据数量
@app.route("/querydatanum", methods=["GET"])
def get_site():
    sql = 'SELECT COUNT(info_id) FROM tb_monitoring_info'
    res = mysql_operate.db.select_db(sql)
    return JsonResponse.success(msg="查询成功", data=res)

#获取更新时间
@app.route("/queryupdate", methods=["GET"])
def get_update():
    sql = 'SELECT create_date FROM tb_monitoring_info order by create_date desc limit 1'
    res = mysql_operate.db.select_db(sql)
    return JsonResponse.success(msg="查询成功", data=res)

#获取当前站点
@app.route("/querysite", methods=["GET","POST"])
def get_siteinfo(longitude,latitude):
    sql = 'SELECT station_code FROM tb_monitoring_station where longitude='+longitude+' and latitude='+latitude
    res = mysql_operate.db.select_db(sql)
    return JsonResponse.success(msg="查询成功", data=res)


if __name__=='__main__':
    # #定义app在8080端口运行
    app.run(debug=True,port=8080)