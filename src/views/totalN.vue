<!-- <template>
	<div  class="Container">
		<el-card class="box-card" style="position:absolute;top:100px;z-index:2;right:68px;background-color: rgb(218, 219, 225);width:210px;height:100px;border: 1px solid #222121;">
			<el-tabs v-model="activeMapName" @tab-click="handleMapChange">
				<el-tab-pane label="高德地图" name="first">
					<el-radio-group v-model="radioGD" @change="mapTypeChange">
						<span v-for="(item,index) in gdLayerTypeArr" :key="index">
							<el-radio :label="item.type" style="margin-right: 30px;">{{item.name}}</el-radio>
						</span>
					</el-radio-group>
				</el-tab-pane>
				<el-tab-pane label="天地图" name="second" >
					<el-radio-group v-model="radioTD" @change="mapTypeChange">
						<span v-for="(item,index) in tdLayerTypeArr" :key="index">
							<el-radio :label="item.type" style="margin-right: 30px;">{{item.name}}</el-radio>
		
						</span>
					</el-radio-group>
				</el-tab-pane>
			</el-tabs>
		</el-card>
		<div id="viewDiv" style="width: 100%;height:100% "></div>
	</div>
  </template>
  <script>
  import {ref} from 'vue'
  import Map from "@arcgis/core/Map";
  import MapView from "@arcgis/core/views/MapView";
  import esriConfig from "@arcgis/core/config";
  import '@arcgis/core/assets/esri/themes/dark/main.css';
  import WebTileLayer from "@arcgis/core/layers/WebTileLayer";
  import ImageryLayer from "@arcgis/core/layers/ImageryLayer";
  
  export default {
	  name: "MapDisplay",
	  data() {
		return {
		  map: null,
		  view: null,
		  urlTemplate: null,
		  activeMapName: "first",
		  radioGD: ref('st'),
		  radioTD: ref('st'),
		  gdLayerType:"st",
		  gdLayerTypeArr:[
		  	{type:"st",name:"影像"},
			{type:"normal",name:"标准"},
			
		  ],
		  tdLayerType:"st",
		  tdLayerTypeArr:[
		 	{type:"st",name:"影像"},
			{type:"normal",name:"标准"},
			
		  ],
		};
	  },
	  methods: {
		initMap(){
		  esriConfig.apiKey = "APK9bc1dfc28cce4d259a09b5af5c205248klw4hdkjzo5LbqG7ni87R0wr4tV0q_5pO-jRtGSY5BJyJmns2-FfsoF7J4Mc2K51"
		  // 创建地图
		  const map = new Map({
			basemap:"",// 底图图
		  })
		  // 创建地图视图
		  const view = new MapView({
			map: map,
			center: [121.498305,29.829034], // 地图中心点经纬度
			zoom: 16, // 缩放等级
			container: "viewDiv" // 地图容器id
		  });
		  view.on("click", function(event) {
			console.info(event)
		  });
		  console.info(view,1111)
		  this.map = map;
		  //加载高德地图
		  const gdLayer = this.loadGdMapLayer();
		  view.map.add(gdLayer);
		  this.view = view;
		  //加载天地地图
		  const tdLayer = this.loadTdMapLayer();
		  view.map.add(tdLayer);
		  //加载分布图
		  const imageryLayer = this.loadImageryLayer();
		  view.map.add(imageryLayer);
		  this.view = view;

		  
		},
		//分布图
		loadImageryLayer(){
			const imageryLayer = new ImageryLayer({
				url: "http://localhost:8081/E:/VScode/vuetest/src/img/2017-4COD.tif",
				id: "imageryLayer",
				name: "分布图"
			});
			return imageryLayer;
		},
		//高德地图
		loadGdMapLayer() {
			const gdMapLayer = new WebTileLayer({
			  urlTemplate:"",
			  id: "gaode",
			  name: "高德地图"
			});
			switch(this.gdLayerType){
				case "normal":{
					gdMapLayer.urlTemplate="https://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={col}&y={row}&z={level}"
					break
				}
				case "st":{
					gdMapLayer.urlTemplate="https://webst01.is.autonavi.com/appmaptile?style=6&x={col}&y={row}&z={level}"
					break
				}
			}
			return gdMapLayer;
		},
		//天地地图
		loadTdMapLayer() {
			const that = this;
			var tdtMapLayer=new WebTileLayer({
				urlTemplate:"",
				id:"tianditu",
				name:"天地图"
			});
			var tdtMapTextLayer=new WebTileLayer({
				urlTemplate:"",
				id:"tianditutext",
				name:"天地图文字标注"
			});
			const ak='a54e3fc8ebebae71e22a13e23b78ec6c'
			switch(that.tdLayerType){
				case "normal":{
					tdtMapLayer.urlTemplate="http://t0.tianditu.gov.cn/vec_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=vec&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TILEMATRIX={level}&TILEROW={row}&TILECOL={col}&tk="+
					ak
					tdtMapTextLayer.urlTemplate="http://t0.tianditu.gov.cn/cva_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=cva&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TILEMATRIX={level}&TILEROW={row}&TILECOL={col}&tk="+
					ak
					break
				}
				case "st":{
					tdtMapLayer.urlTemplate =
					'http://t0.tianditu.gov.cn/img_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=img&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TILEMATRIX={level}&TILEROW={row}&TILECOL={col}&tk=' +
					ak
					tdtMapTextLayer.urlTemplate =
					'http://t0.tianditu.gov.cn/cia_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=cia&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TILEMATRIX={level}&TILEROW={row}&TILECOL={col}&tk=' +
					ak
					break
				}
			}
			
			return {tdtMapLayer,tdtMapTextLayer};
	  },
		//地图变化
		handleMapChange(tab){
			
			console.info(tab)
			switch(tab.props.name){
				case "first":{
					this.gdLayerType="normal";
					this.map.layers.removeAll();
					const gdLayer = this.loadGdMapLayer();
					this.map.layers.add(gdLayer);
					this.view.goTo({
						center: [121.498305,29.829034],
						zoom: 16,
					})
					break
				}
					
				case "second":{
					this.tdLayerType="normal";
					this.map.layers.removeAll();
					const tdLayer = this.loadTdMapLayer();
					this.map.layers.add(tdLayer.tdtMapLayer);
					this.map.layers.add(tdLayer.tdtMapTextLayer);
					this.view.goTo({
						center: [121.498305,29.829034],
						zoom: 16,
					})
					break
				}  
				}

	  	},
		//地图风格变化
		mapTypeChange(e){
			this.map.layers.removeAll();
			switch(this.activeMapName){	
				case "first":{
					this.gdLayerType = e;
					const gdLayer = this.loadGdMapLayer();
					this.map.layers.add(gdLayer);
					break
				}
				case "second":{
					this.tdLayerType = e;
					const tdLayer = this.loadTdMapLayer();
					this.map.layers.add(tdLayer.tdtMapLayer);
					this.map.layers.add(tdLayer.tdtMapTextLayer);
					break
				}
			}
		}
	  },
		mounted() {
			this.initMap()
		}
	}

  </script>
  
  <style lang="scss" scoped>
  .Container{
	padding: 0 12px 12px 12px;
	border-radius: 5px;
	height: calc(100vh - 69px);
		
}
  </style>
   -->
   <template>
	<div class="Container">
	 
	  <div class="image-container">
		<img src="../assets/TN.jpg" alt="Static Image">

	  </div>
	</div>
  </template>
  <style lang="scss" scoped>
  .Container {
	padding: 0 12px 12px 12px;
	border-radius: 5px;
	height: calc(100vh - 69px);
  }
  
  .image-container {
  
	width: 100%;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
  
	img {
	  max-width: 100%;
	  max-height: 100%;
	}
  }
  </style>