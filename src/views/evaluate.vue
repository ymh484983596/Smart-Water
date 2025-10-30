<template>
    <div id="app">
        <div class="box">
            <div class="boxLeft">
                <!-- <div id="mychart" style="width: 100%;height: 100%;"></div> -->
                <baidu-map id="map-container" :center="center" :zoom="zoom" :ak="ak" @ready="handler"
                    style="width: 100%; height: 100%"></baidu-map>
                <div class="positonmap">
                    <div style="padding:10px 16px;color: #fff;font-size: 18px;font-weight: 700;text-align: left;">{{ objZd.name }}</div>
                    <p>流域面积：30 km²</p>
                    <p>水质类型：{{ objZd.wuran }}</p>
                    <p>富营养化程度：{{ objZd.chengdu }}</p>
                    <p>检测站点：3</p>
                    <p>达标站点：3</p>
                </div>
            </div>
            <div class="boxRight">
                <div class="flextitle">
                    <div class="titleItemFlex">
                        <div style="padding: 4px 6px;color: #8D454D;font-size: 20px;font-weight: 400;">3</div>
                        <div style="padding: 0px  6px 8px 6px;color: #6F7FA6;">监测站总数</div>
                    </div>
                    <div class="titleItemFlex">
                        <div style="padding: 4px  6px ;color: #2C85DF;font-size: 20px;font-weight: 400;">{{ totalData.datanum }}</div>
                        <div style="padding: 0px  6px 8px 6px;color: #6F7FA6;">监测站数据总量</div>
                    </div>
                    <div class="titleItemFlex">
                        <div style="padding: 4px 6px;color: #B2DC82;font-size: 20px;font-weight: 400;">3</div>
                        <div style="padding: 0px  6px 8px 6px;color: #6F7FA6;">当前站点</div>
                    </div>
                    <div class="titleItemFlex">
                        <div style="padding: 4px 6px;color: #37B1D0;font-size: 20px;font-weight: 400;">{{ updateDate.updatedate }}</div>
                        <div style="padding: 0px  6px 8px 6px;color: #6F7FA6;">最新更新时间</div>
                    </div>
                    <div class="eqDataList">
                        <div style="color: #65E9FF;font-size: 22px;padding: 10px 16px;">设备在线总数：<span
                                style="color: red;font-size: 22px;font-weight: 400;">{{ deviceNum.sitenum }}</span></div>
                        <ul>
                            <li>
                                <div style="width: 40%;">水质检测设备1:</div>
                                <div style="width: 30%;">是否在线</div>
                                <div style="width: 30%;"><el-tag type="success">开启</el-tag></div>
                            </li>
                            <li>
                                <div style="width: 40%;">水质检测设备2</div>
                                <div style="width: 30%;">是否在线</div>
                                <div style="width: 30%;"><el-tag type="danger">禁用</el-tag></div>
                            </li>
                            <li>
                                <div style="width: 40%;">水质检测设备3</div>
                                <div style="width: 30%;">是否在线</div>
                                <div style="width: 30%;"><el-tag type="danger">禁用</el-tag></div>
                            </li>
                            <!-- <li>
                                <div style="width: 40%;">水质检测设备1</div>
                                <div style="width: 30%;">是否在线</div>
                                <div style="width: 30%;"><el-tag type="danger">禁用</el-tag> </div>
                            </li> -->
                        </ul>
                    </div>
                </div>
                <!-- <div style="text-align: right;line-height: 24px;margin-right: 10px;margin-top: 5px;">更多</div>
                <div style="padding: 16px;color: #0097B4;font-size: 18px;font-weight: 700;text-align: left;">今日报警信息： <span
                        style="color: red;margin-left: 10px;">8</span></div>
                <div class="tablediv">
                    <div class="divtitle">
                        <div class="rowItem" style="width: 20%;">报警站点</div>
                        <div class="rowItem" style="width: 30%;">报警时间</div>
                        <div class="rowItem" style="width: 50%;">报警原因</div>
                    </div>
                    <div class="divtitle">
                        <div class="rowItem" style="width: 20%;">测试站点</div>
                        <div class="rowItem" style="width: 30%;">2023-11-07 10:59:34</div>
                        <div class="rowItem" style="width: 50%;">报警原因,设备故障</div>
                    </div>
                    <div class="divtitle">
                        <div class="rowItem" style="width: 20%;">报警站点</div>
                        <div class="rowItem" style="width: 30%;">2023-11-07 10:59:34</div>
                        <div class="rowItem" style="width: 50%;">报警原因,设备故障22222</div>
                    </div>
                    <div class="divtitle">
                        <div class="rowItem" style="width: 20%;">报警站点</div>
                        <div class="rowItem" style="width: 30%;">2023-11-07 10:59:34</div>
                        <div class="rowItem" style="width: 50%;">报警原因,设备故障33333333</div>
                    </div>
                </div> -->
            </div>
        </div>
        <div class="boxBottom">
            <div class="echartsLeft">
                <!-- <div style="padding:10px 16px;color: #fff;font-size: 18px;font-weight: 700;text-align: left;">监测点数据</div> -->
                <div id="main2" style="width: 100%;height: 300px;margin-top: 10px;"></div>
            </div>
            <div class="echartsright">
                <!-- <div style="padding:10px 16px;color: #fff;font-size: 18px;font-weight: 700;text-align: left;">本周水质检测数值对比
                </div> -->
                <div id="main3" style="width: 100%;height: 300px;margin-top: 10px;"></div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import BaiduMap from "vue-baidu-map/components/map/Map.vue";
export default {
    components: {
        BaiduMap
    },
    data() {
        return {
            objZd:{},
            active: 0,
            center: { lng: 121.511149, lat: 29.83276 },
            zoom: 6,
            ak: "4Ud8GvyhLSeGKm79PyW2mSHuGzFYoeKH",
            fiiterIndex: 0,
            marker: [],
            BMap: "",
            siteList: [
               
                { name: "站点2", lng: 121.507382, lat: 29.835049 ,wuran:"V",chengdu:"轻度"},
                { name: "站点3", lng: 121.497429, lat: 29.836334 ,wuran:"VI",chengdu:"低度"},
                { name: "站点4", lng: 121.513024, lat: 29.830663,wuran:"I",chengdu:"高度" }
            ],
            deviceNum:[],//站点总数
            deviceStatus:[],//设备在线状态
           totalData:[],//数据总量
           updateDate:[],//最新更新时间
        }
    },
     created() {
        this.request.get("http://localhost:8080/deviceonline", {}).then((res) => {
        // console.log(res.data);  
        // Assuming that 'res' contains the data you want to display
        this.deviceStatus = res.data;
        }),
        this.request.get("http://localhost:8080/querydatanum", {}).then((res) => {
        // console.log(res.data);  
        // Assuming that 'res' contains the data you want to display
        this.totalData = res.data;
        }),
        this.request.get("http://localhost:8080/queryupdate", {}).then((res) => {
        // console.log(res.data);  
        // Assuming that 'res' contains the data you want to display
        this.updateDate= res.data;
        }),
        this.request.get("http://localhost:8080/querysitenum", {}).then((res) => {
        // console.log(res.data);  
        // Assuming that 'res' contains the data you want to display
        this.deviceNum = res.data;
        });

    },
    
    methods: {
        getSiteDetail(i, bPoints) {
            this.fiiterIndex = i;
            let content = "";
            const opts = {
                width: 250, // 信息窗口宽度
                height: 2, // 信息窗口高度
                title: "<h4>" + this.siteList[i].name + "</h4>", // 信息窗口标题
                enableMessage: true //设置允许信息窗发送短息
            };
            // this.efficiencyInfo.date = this.timeFrame(0, null);
            // this.efficiencyInfo.siteId = this.siteList[i].id;
            // this.initElectricityInfo();
            this.zoom = 14;
            const infoWindow = new this.BMap.InfoWindow(content, opts);
            this.marker[i].openInfoWindow(infoWindow);
            this.setZoom(bPoints);
            // this.showOpen = true;
        },
        handler({ BMap, map }) {
            this.BMap = BMap;
            this.map = map;
            this.map.centerAndZoom(" ", this.zoom); // 地图初始化，同时设置地图展示级别
            this.map.enableScrollWheelZoom(true); //开启鼠标滚轮缩放
            this.map.setMapType(BMAP_HYBRID_MAP)
            this.setMarker();
        },
        setMarker() {
            this.map.clearOverlays();
            let bPoints = [];
            for (let i = 0; i < this.siteList.length; i++) {
                const statePoint = new this.BMap.Point(this.siteList[i].lng, this.siteList[i].lat);
                bPoints.push(statePoint);
                this.marker[i] = new this.BMap.Marker(statePoint);
                this.map.addOverlay(this.marker[i]);
                this.marker[i].setTitle(this.siteList[i].name);
                this.marker[i].addEventListener("click", () => {
                    console.log(this.objZd);
                    this.objZd=this.siteList[i]
                    this.getSiteDetail(i, bPoints);
                    this.$router.push({path:'/management',query: { objName: this.siteList[i].name }}).then(() => { this.$router.go() })
                      // 存储数据
                      sessionStorage.setItem('zdname', 1);
                });
            }
            this.setZoom(bPoints);
        },
        setZoom(bPoints) {
            var view = this.map.getViewport(eval(bPoints));
            var mapZoom = this.zoom;
            var centerPoint = view.center;
            this.map.centerAndZoom(centerPoint, mapZoom / 1.1);
            // 在 setZoom 方法中添加新的点

        },
        drawChart2() {
            // 基于准备好的dom，初始化echarts实例  这个和上面的main对应
            let myChart = this.$echarts.init(document.getElementById("main2"));
            // 指定图表的配置项和数据
            var option = {
                title: {
                    text: '监测点数据',//主标题文本
                    left: '10%', // 标题距离左边位置，可以使用right
                    top: "0", // 标题距离底部位置，可以使用top
                    textStyle: { // 主标题样式
                        fontSize: 17,
                        color: "#fff"
                    },
                    subtextStyle: { // 副标题样式
                        fontFamily: "微软雅黑",
                        fontSize: 16,
                        color: '#6c7a89',
                    }
                },
                tooltip: {
                    trigger: "axis",
                    axisPointer: {
                        type: "cross"
                    }
                },
                legend: {
                    textStyle: {
                        color: "#fff",
                        fontSize: 17,
                    },
                    itemGap: 60,
                    right: '5%',
                    data: ['Chl-a', 'TN', 'TP',]
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
                        name: "Chl-a",
                        data: [1, 6, 5, 1, 3, 4, 1, 2, 3, 2, 6, 6, 7, 6, 13],
                        type: "bar",
                    },
                    {
                        name: "TN",
                        data: [1, 4, 7, 6, 2, 1, 2, 4, 5, 6, 4, 4, 3, 2, 12],
                        type: "bar",
                    },
                    {
                        name: "TP",
                        data: [4, 7, 5, 2, 7, 3, 3, 5, 7, 8, 9, 1, 2, 2, 11],
                        type: "bar",
                    },
                ]
            };
            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
        },
        drawChart3() {
            // 基于准备好的dom，初始化echarts实例  这个和上面的main对应
            let myChart = this.$echarts.init(document.getElementById("main3"));
            // 指定图表的配置项和数据
            var option = {
                title: {
                    text: '本周水质检测数值对比',//主标题文本
                    left: '10%', // 标题距离左边位置，可以使用right
                    top: "0", // 标题距离底部位置，可以使用top
                    textStyle: { // 主标题样式
                        fontSize: 16,
                        color: "#fff"
                    },
                    subtextStyle: { // 副标题样式
                        fontFamily: "微软雅黑",
                        fontSize: 16,
                        color: '#6c7a89',
                    }
                },
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
                    right: '5%',
                    itemGap: 60,
                    data: ['Chl-a', 'TN', 'TP',]
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
                        name: "Chl-a",
                        data: [1, 6, 5, 1, 3, 4, 1, 2, 3, 2, 6, 6, 7, 6, 13],
                        type: "bar",
                    },
                    {
                        name: "TN",
                        data: [1, 4, 7, 6, 2, 1, 2, 4, 5, 6, 4, 4, 3, 2, 12],
                        type: "bar",
                    },
                    {
                        name: "TP",
                        data: [4, 7, 5, 2, 7, 3, 3, 5, 7, 8, 9, 1, 2, 2, 11],
                        type: "bar",
                    },
                ]
            };
            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
        },
        initEcharts() {
            axios({
                method: "GET",
                url: 'https://geo.datav.aliyun.com/areas_v3/bound/330000_full.json'
            }).then((res) => {
                let mychart = this.$echarts.init(document.getElementById("mychart"));
                this.$echarts.registerMap("浙江", res.data);// 注册地图
                let option = {
                    series: [
                        {
                            name: "浙江",
                            type: "map",
                            mapType: "浙江", // 自定义扩展图表类型
                            label: {
                                show: false,
                            },
                        },
                    ],
                };
                mychart.setOption(option);
            })

        }
    },
    mounted() {
        setTimeout(() => {
            // this.initEcharts()
            this.drawChart2()
            this.drawChart3()
            let bPoints = [];
            const statePoint = new this.BMap.Point(121.544019, 29.859592);
            bPoints.push(statePoint);
            this.getSiteDetail(0, bPoints);
        }, 400);
        this.objZd=this.siteList[0]
    }
}
</script>
<style lang="scss" scoped>
.positonmap {
    // height: 100%;
    min-height: 280px;
    width: 240px;
    color: #fff;
    background: rgba(52, 88, 122, 0.853);
    position: absolute;
    right: 0;
    bottom: 0;
    z-index: 100;
}

.boxBottom {
    display: flex;
    justify-content: space-between;
}

.echartsLeft {
    width: 65%;
    border: 4px solid #1B4B78;
    border-radius: 30px;
    box-sizing: border-box;
}

.echartsright {
    width: 34%;
    border: 4px solid #1B4B78;
    border-radius: 30px;
    box-sizing: border-box;
}

.flextitle {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    padding: 16px;

    .titleItemFlex {
        width: 48%;
        border: 1px solid #1B4B78;
        border-radius: 6px;
        margin-bottom: 10px;
    }
}

.eqDataList {
    border: 1px solid #1B4B78;
    width: 100%;
    overflow: hidden;

    ul {
        overflow-y: auto;

        li {
            height: 40px;
            line-height: 40px;
            display: flex;
        }
    }
}

.box {
    width: 100%;
    height: calc(100vh - 440px);
    min-height: 400px;
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;

    .boxLeft {
        width: 65%;
        height: calc(100vh - 440px);
        border: 4px solid #1B4B78;
        border-radius: 30px;
        box-sizing: border-box;
        position: relative;
        overflow: hidden;
    }

    .boxRight {
        width: 34%;
        border: 4px solid #1B4B78;
        border-radius: 30px;
        box-sizing: border-box;
        height: calc(100vh - 440px);
        color: #fff;
    }

    .tablediv {
        padding: 16px;

        .divtitle {
            display: flex;
            text-align: center;
            line-height: 24px;
        }
    }

    .bottomTitle {
        display: flex;
    }

    .bottomLeft {
        width: 70%;
        height: 40px;
        line-height: 40px;
    }

    .bottomRight {
        width: 30%;
        height: 40px;

        .selectList {
            display: flex;

            >div {
                padding: 4px 6px;
                background: #f0f9eb;
            }
        }
    }
}
</style>