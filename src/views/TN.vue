<template xmlns="http://www.w3.org/1999/html">
    <div style="background: #062047;overflow-x: hidden;">
        <div style="color: #fff;">站点TN</div>
      <div class="d">
        <div class="boxleft">
          <div class="title1">
            <div class="titleLeft">Ai监测站 各项水质参数实时数据检测表</div>  
            <div class="titleRight">当前水温： </div>
            <div style="color: #BCDCE1;"> <span class="hoverItem" id="water_temperature"
                  style="color: #BCDCE1;font-size: 20px;font-weight: 500;"></span>°C
              </div>
            <div class="titleRight">当前时间： {{ time }}</div>
          </div>
          <div class="boxCenterText" data="data">
            <div class="item">
              <div style="color: #0097B4;margin-top: 16px;margin-bottom: 4px;"> 氨氮</div>
              <div style="color: #0097B4;"> <span class="hoverItem" id="nhn"
                  style="color: #BCDCE1;font-size: 30px;font-weight: 500;"></span>mg/L
              </div>
            </div>
            <div class="item">
              <div style="color: #0097B4;margin-top: 16px;margin-bottom: 4px;"> 电导率</div>
              <div style="color: #0097B4;"> <span class="hoverItem" id="conductance"
                  style="color: #BCDCE1;font-size: 30px;font-weight: 500;"></span> us/cm
              </div>
            </div>
            <div class="item">
              <div style="color: #0097B4;margin-top: 16px;margin-bottom: 4px;"> PH</div>
              <div style="color: #0097B4;"> <span class="hoverItem" id="ph"
                  style="color: #BCDCE1;font-size: 30px;font-weight: 500;"></span> 
              </div>
            </div>
            <div class="item">
              <div style="color: #0097B4;margin-top: 16px;margin-bottom: 4px;"> 溶解氧</div>
              <div style="color: #0097B4;"> <span class="hoverItem" id="DO"
                  style="color: #BCDCE1;font-size: 30px;font-weight: 500;"></span> mg/L</div>
            </div>
            <div class="item">
              <div style="color: #0097B4;margin-top: 16px;margin-bottom: 4px;"> 浊度</div>
              <div style="color: #0097B4;"> <span class="hoverItem" id="turbidity"
                  style="color: #BCDCE1;font-size: 30px;font-weight: 500;"></span> NTU
              </div>
            </div>
            <div class="item">
              <div style="color: #0097B4;margin-top: 16px;margin-bottom: 4px;"> 叶绿素a</div>
              <div style="color: #0097B4;"> <span class="hoverItem" id="chla"
                  style="color: #BCDCE1;font-size: 30px;font-weight: 500;"></span> mg/L
              </div>
            </div>
            <div class="item">
              <div style="color: #0097B4;margin-top: 16px;margin-bottom: 4px;"> 总氮</div>
              <div style="color: #0097B4;"> <span class="hoverItem" id="total_nitrogen"
                  style="color: #BCDCE1;font-size: 30px;font-weight: 500;"></span> Mol/L
              </div>
            </div>
            <div class="item">
              <div style="color: #0097B4;margin-top: 16px;margin-bottom: 4px;"> 总磷</div>
              <div style="color: #0097B4;"> <span class="hoverItem" id="total_phosphorus"
                  style="color: #BCDCE1;font-size: 30px;font-weight: 500;"></span> Mol/L
              </div>
            </div>
          </div>
        </div>
        <!-- <div class="boxright">
          <div class="rightTitle">
            气温气象
          </div>
          <div class="divTime">
            <div class="divTimeLeft">
              <div style="font-size: 40px; color: #Fff;font-weight: 700;">{{ titleTimeRight }}</div>
              <div>{{ titleTime }} pm {{ weekDay }}</div>
              <div>武汉</div>
              <div>东南风 晴</div>
              <div>当前 6 ℃ 高温 8 ℃ 低温 4 ℃</div>
            </div>
            <div class="divTimeRight">
              <img src="./img/3.jpg" alt="">
            </div>
          </div>
          <div style="margin-left: 15px;color: #Fff;">昼夜温差大,容易发生感冒,注意添加衣服。</div>
        </div> -->
      </div>
      <div class="divCoenter">
        <div class="divConterLeft">
          <div class="tableTltle">
            PH数据
          </div>
          <div class="table" style="height: 150px;overflow-y: auto;">
            <div class="tableLabel"> 
              <div class="itemTable">经度</div>
              <div class="itemTable">纬度</div>
              <div class="itemTable">数值</div>
              <div class="itemTable">时间</div>
            </div>
            <div>
  
              <div  v-for="(item,index) in tableList" class="itemRow">
                <div class="itemCenter2">{{ item.longitude }}</div>
                <div class="itemCenter2">{{ item.latitude}}</div>
                <div class="itemCenter2">{{ item.ph}}</div>
                <!-- <div class="itemCenter2">{{ item.create_date}}</div> -->
                <div class="itemCenter2">{{item.create_date | dataFormat}}</div>
              </div>
            </div>
          </div>
        </div>
        <div class="divConterRight">
          <div class="icontItem">
            <div style="padding: 10px 0;">溶解氧 (7天)</div>
            <div>
              <div style="float: left;"> <img src="./img/icont.png" alt=""></div>
              <div style="float: right;width: 50%;">
                
                <div>  <p>最大值：{{DOlist | dataMax}}</p></div>
                <div>  <p>最小值：{{DOlist | dataMin}}</p></div>
                <div>  <p>平均值：{{DOlist | dataMean}}</p></div>
              </div>
            </div>
          </div>
          <div class="icontItem">
            <div style="padding: 10px 0;">电导率 (7天)</div>
            <div>
              <div style="float: left;"> <img src="./img/icont.png" alt=""></div>
              <div style="float: right;width: 50%;">
                <div>  <p>最大值：{{conductancelist | dataMax}}</p></div>
                <div>  <p>最小值：{{conductancelist | dataMin}}</p></div>
                <div>  <p>平均值：{{conductancelist | dataMean}}</p></div>
              </div>
            </div>
          </div>
          <div class="icontItem">
            <div style="padding: 10px 0;">浊度 (7天)</div>
            <div>
              <div style="float: left;"> <img src="./img/icont.png" alt=""></div>
              <div style="float: right;width: 50%;">
                <div>  <p>最大值：{{turbiditylist | dataMax}}</p></div>
                <div>  <p>最小值：{{turbiditylist | dataMin}}</p></div>
                <div>  <p>平均值：{{turbiditylist | dataMean}}</p></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="boxbottom">
        <div class="bottomLeft">
          <div style="padding:10px 16px;color: #fff;font-size: 18px;font-weight: 700;text-align: left;">监测点数据 <div
              class="btnclass">详情</div>
          </div>
          <div class="timedq">
            当前时间： <el-date-picker v-model="planWorkFormQuery.planDate" style="width: 20%;"
              :picker-options="planWorkFormQuery.shortcuts" type="daterange" range-separator="-" value-format="yyyy-MM-dd"
              start-placeholder="开始日期" end-placeholder="结束日期" size="mini" @change="changeplanDate" />
          </div>
          <!-- <div class="timedq">
            <div style="float: left;"> 监测点位置：</div>
            <div class="wzdiv">位置</div>
          </div> -->
          <div id="main" style="width: 100%;height: 220px;margin-top: 10px;"></div>
        </div>
  
      </div>
    </div>
  </template>
  
  <script>
  // import { apiAddress } from '../views/utils/api'
  export default {
    data() {
      return {
        time: null,
        titleTime: null,
        titleTimeRight: null,
      
        tableList: [],
        DOlist:[],
        turbiditylist:[],
        conductancelist:[],
  
        planWorkFormQuery: {
          planDate: []
        },
  
      }
    },
   
  
    created() {
      this.request.get("http://localhost:8080/query", {}).then((res) => {
        // console.log(res.data);  
        // Assuming that 'res' contains the data you want to display
        let latestdata = res.data;
     
        // console.log(latestdat,11111111);
  
        // Update HTML elements with the received data
        document.getElementById("water_temperature").textContent = latestdata.water_temperature;
        document.getElementById("nhn").textContent = latestdata.NHN;
        document.getElementById("conductance").textContent = latestdata.conductance;
        document.getElementById("ph").textContent = latestdata.ph;
        document.getElementById("DO").textContent = latestdata.DO;
        document.getElementById("turbidity").textContent = latestdata.turbidity;
        document.getElementById("chla").textContent = latestdata.chl_a;
        document.getElementById("total_nitrogen").textContent = latestdata.total_nitrogen;
        document.getElementById("total_phosphorus").textContent = latestdata.total_phosphorus;
      }),
  
      this.request.get("http://localhost:8080/querydata", {}).then((res) => {
        // console.log(res.data);  
        // Assuming that 'res' contains the data you want to display
        let latestdata1= res.data;
     
        // console.log(latestdata1);
  
        // Update HTML elements with the received data
        document.getElementById("chla").textContent = latestdata1.chla;
        document.getElementById("total_nitrogen").textContent = latestdata1.TN;
        document.getElementById("total_phosphorus").textContent = latestdata1.TP;
      }),
      
  
      this.request.get("http://localhost:8080/all", {}).then((res) => {
        // console.log(res.data);  
        // Assuming that 'res' contains the data you want to display
        let data = res.data;
        // console.log(data,22222222);
        this.tableList=res.data
          
        for (var ite in this.tableList){
          this.DOlist.push(this.tableList[ite].DO)
          this.turbiditylist.push(this.tableList[ite].turbidity)
          this.conductancelist.push(this.tableList[ite].conductance)
        }
         
         
         
        }),
  
        // apiAddress({}).then((res) => {
        //   console.log(res, 21212121);
        // })
        this.getSevenDaysAgo()
      setInterval(() => {
        this.time = this.newdate().minute;
        this.titleTime = this.newdate().minute.substring(0, 10);
        this.titleTimeRight = this.newdate().minute.substring(10, 19);
      }, 1000);
  
      let cnWeek = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
      let now = new Date();
      let weekDay = now.getDay();
      this.weekDay = cnWeek[weekDay];
      setTimeout(() => {
        this.drawChart()
      }, 200);
    },
    methods: {
      changeplanDate(value) {
        if (value) {
          this.planWorkFormQuery.planDate[0] = value[0] + " 00:00:00";
          this.planWorkFormQuery.planDate[1] = value[1] + " 23:59:59";
        }
      },
      getSevenDaysAgo() {
        var now = new Date();
        var SevenDaysAgo = new Date();
        var SevenDaysLater = new Date();
        //获取当前时间的毫秒数
        var nowMilliSeconds = now.getTime();
        //用获取毫秒数 减去两天的毫秒数 赋值给TwoDaysAgo对象（一天有86400000毫秒）
        SevenDaysAgo.setTime(nowMilliSeconds - (14 * 86400000));
        SevenDaysLater.setTime(nowMilliSeconds + (0 * 86400000));
        //通过赋值后的TwoDaysAgo对象来得到 两天前的 年月日。这里我们将日期格式化为20180301的样子。
        //格式化日，如果小于9，前面补0
        var day1 = ("0" + SevenDaysAgo.getDate()).slice(-2);
        var day2 = ("0" + SevenDaysLater.getDate()).slice(-2);
        //格式化月，如果小于9，前面补0
        var month1 = ("0" + (SevenDaysAgo.getMonth() + 1)).slice(-2);
        var month2 = ("0" + (SevenDaysLater.getMonth() + 1)).slice(-2);
        //拼装完整日期格式
        var getSevenDaysAgo = SevenDaysAgo.getFullYear() + "-" + (month1) + "-" + (day1);
        var getSevenDaysLater = SevenDaysLater.getFullYear() + "-" + (month2) + "-" + (day2);
        this.planWorkFormQuery.planDate = [getSevenDaysAgo + " 00:00:00", getSevenDaysLater + " 23:59:59"];
      },
      drawChart() {
        // 基于准备好的dom，初始化echarts实例  这个和上面的main对应
        let myChart = this.$echarts.init(document.getElementById("main"));
        // 指定图表的配置项和数据
        var option = {
          tooltip: {
            trigger: "axis",
            axisPointer: {
              type: "cross"
            }
          },
          legend: {
            textStyle: {
              color: "#fff",
              fontSize: 16,
            },
            itemGap: 60,
            data: ['叶绿素a', '总氮', '总磷',]
          },
          grid: {
            top: 70,
            bottom: 50
          },
          dataZoom: [
            {   // 这个dataZoom组件，默认控制x轴。
              type: "inside", // 这个 dataZoom 组件是 slider 型 dataZoom 组件
              start: 0,      // 左边在 10% 的位置。
              end: 100,// 右边在 60% 的位置。
              show: false
            }
          ],
          xAxis: {
            type: "category",
            axisLabel: {
              textStyle: {
                color: "rgb(178,187,200)"
              }
            },
            data: ['2023-10-28', '2023-10-29', '2023-10-30', '2023-10-31', '2023-11-1', '2023-11-2', '2023-11-3', '2023-11-4', '2023-11-5', '2023-11-6', '2023-11-7', '2023-11-8', '2023-11-9', '2023-11-10', '2023-11-11']
          },
          yAxis: [
            {
              splitLine: {
                show: true,
                lineStyle: {
                  type: "dashed",
                  color: "rgb(14,38,79)"
                }
              },
              axisLabel: {
                textStyle: {
                  color: "rgb(178,187,200)"
                }
              },
              type: "value"
            },
          ],
          series: [
            {
              name: "叶绿素a",
              data: [1, 6, 5, 1, 3, 4, 1, 2, 3, 2, 6, 6, 7, 6, 13],
              type: "line",
            },
            {
              name: "总氮",
              data: [1, 4, 7, 6, 2, 1, 2, 4, 5, 6, 4, 4, 3, 2, 12],
              type: "line",
            },
            {
              name: "总磷",
              data: [4, 7, 5, 2, 7, 3, 3, 5, 7, 8, 9, 1, 2, 2, 11],
              type: "line",
            },
          ]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
      },
      newdate() {
        const oDate = new Date();
        const Y = oDate.getFullYear() + "-";
        const M =
          (oDate.getMonth() + 1 < 10
            ? "0" + (oDate.getMonth() + 1)
            : oDate.getMonth() + 1) + "-";
        const D =
          (oDate.getDate() < 10 ? "0" + oDate.getDate() : oDate.getDate()) + " ";
        const h = oDate.getHours();
        const i = oDate.getMinutes();
        const s = oDate.getSeconds();
        const tday = oDate.getDay();
        return {
          day: Y + M + D,
          tday: tday,
          minute:
            Y +
            M +
            D +
            (h < 10 ? "0" + h : h) +
            ":" +
            (i < 10 ? "0" + i : i) +
            ":" +
            (s < 10 ? "0" + s : s),
        };
      },
    },
  }
  </script>
  
  
  
  
  <style lang="scss" scoped>
  .divCoenter {
    display: flex;
    justify-content: space-between;
    padding: 10px 24px 0px 24px;
  
    .divConterLeft {
      width: 49%;
      height: 100%;
    }
  
    .divConterRight {
      width: 49%;
      // height: 100%;
      display: flex;
      justify-content: space-between;
      color: #fff;
  
      .icontItem {
        width: 30%;
        background: #11365F;
  
        img {
          height: 90px;
          height: 90px;
          margin-left: 24px;
          margin-top: 18px;
        }
  
        p {
          text-align: left;
        }
      }
    }
  }
  
  /*滚动条整体样式*/
  ::-webkit-scrollbar {
    width: 12px;
    border-radius: 5px;
  }
  
  /*滚动条轨道样式*/
  ::-webkit-scrollbar-track {
    background: #021633;
  }
  
  /*滚动条滑块样式*/
  ::-webkit-scrollbar-thumb {
    background: #3F4F74;
    border-radius: 5px;
  }
  
  .item:hover .hoverItem {
    color: red !important;
  }
  
  .boxbottom {
    background: #062047;
    display: flex;
    justify-content: space-between;
    padding: 16px 16px 16px 24px;
    //height: calc(100vh - 560px);
    height: 30%;
  }
  
  .tableTltle {
    color: #06C7D9;
    font-size: 18px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
  }
  
  .table {
    border: 1px solid #fff;
    overflow: hidden;
  }
  
  .itemRow {
    display: flex;
    cursor: pointer;
    border-bottom: 1px solid #fff;
  }
  
  .tableLabel {
    display: flex;
    background: #0F1F40;
    border-bottom: 1px solid #fff;
  
    .itemTable {
      width: 25%;
      height: 50px;
      line-height: 50px;
      text-align: center;
      color: #fff;
      font-size: 16px;
      font-weight: 500;
      border-right: 1px solid #fff;
    }
  }
  
  .itemCenter {
    width: 25%;
    height: 33px;
    line-height: 33px;
    text-align: center;
    color: #fff;
    font-size: 14px;
    font-weight: 400;
    background: #072951;
    border-right: 1px solid #fff;
  
  }
  
  .itemCenter2 {
    width: 25%;
    height: 33px;
    line-height: 33px;
    text-align: center;
    color: #fff;
    font-size: 14px;
    font-weight: 400;
    background: #072951;
    border-right: 1px solid #fff;
  }
  
  .wzdiv {
    width: 180px;
    height: 24px;
    line-height: 24px;
    background: #C4D7E4;
    color: #000D19;
    text-align: center;
    float: left;
  }
  
  .btnclass {
    color: #fff;
    font-size: 14px;
    height: 24px;
    line-height: 24px;
    border: 1px solid #183B54;
    border-radius: 5px;
    font-weight: 300;
    width: 60px;
    float: right;
    text-align: center;
    color: #FFF;
    background-color: #909399;
    border-color: #909399;
    cursor: pointer;
  }
  
  .timedq {
    color: #Fff;
    text-align: left;
    padding-left: 16px;
  }
  
  .bottomLeft {
    background: #11365F;
    width: 100%;
    border-radius: 30px;
    border: 1px solid #11365F;
    height: 30%;
  }
  
  
  .divConterLeft {
    background: #11365F;
    width: 49%;
    border-radius: 30px;
    border: 1px solid #11365F;
    padding: 10px 16px;
    box-sizing: border-box;
    height: 30%;
  }
  
  .d {
    height: 40%;
    width: 100%;
    background: #062047;
    padding: 0 24px 0 24px;
    display: flex;
    box-sizing: border-box;
    justify-content: space-between;
  
    .boxleft {
      width: 100%;
      // min-height: 400px;
      height: 100%;
      border: 4px solid #1B4B78;
      border-radius: 30px;
      background: url("./img/2.png") repeat;
      background-size: 50%;
  
      .boxCenterText {
        // width: 70%;
        height: 100%;
        margin: 0 auto;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
  
        .item {
          width: 23%;
          height: 100px;
          border: 3px solid #0097B4;
          border-radius: 5px;
          background: #000D19;
          box-sizing: border-box;
          text-align: center;
          margin-bottom: 10px;
        }
      }
  
      .title1 {
        padding: 10px 40px 10px 40px;
        display: flex;
  
        .titleLeft {
          width: 70%;
          color: #0097B4;
          font-size: 18px;
          font-weight: 600;
          text-align: left;
        }
  
        .titleRight {
          width: 30%;
          color: #Fff;
          text-align: right;
        }
      }
    }
  
    .boxright {
      width: 29%;
      text-align: left;
      border: 4px solid #1B4B78;
      border-radius: 30px;
      box-sizing: border-box;
      margin-right: 50px;
  
      .rightTitle {
        color: #0097B4;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
        margin-top: 50px;
      }
  
      .divTime {
        display: flex;
        margin-left: 15px;
        color: #fff;
        height: 130px;
  
        .divTimeLeft {
          width: 60%;
          color: #fff;
        }
  
        .divTimeRight {
          width: 40%;
        }
      }
    }
  }
  
  .container {
    background-color: #373d44;
    background-size: 100%;
    display: flex;
    width: 100%;
    height: calc(100vh - 0px);
    flex-direction: column;
    /* 按照列column(垂直方向)排列*/
    //background: #fff;
  
  
  }
  </style>
  