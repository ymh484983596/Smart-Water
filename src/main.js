import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import './assets/css/global.css'
// import store from "./store";
import ElementUI from 'element-ui'; // 2.1引入结构
import 'element-ui/lib/theme-chalk/index.css'; // 2.2引入样式
import './plugins/element.js'
import moment from 'moment'
import dayjs from 'dayjs'
import request from "./views/utils/request";
import * as echarts from 'echarts';
import Enumerable from 'linq';



Vue.config.productionTip = false;
Vue.prototype.$moment = moment;
Vue.prototype.$dayjs = dayjs;
Vue.prototype.$echarts = echarts
Vue.prototype.request=request
Vue.use(ElementUI);

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");


Vue.filter('dataFormat', function (originVal) {
  const dt = new Date(originVal);
  dt.setHours(dt.getHours() - 8);
  const y = dt.getFullYear()
  const m = (dt.getMonth() + 1 + '').padStart(2, '0')
  const d = (dt.getDate() + '').padStart(2, '0')
 
  const hh = (dt.getHours() + '').padStart(2, '0')
  const mm = (dt.getMinutes() + '').padStart(2, '0')
  const ss = (dt.getSeconds() + '').padStart(2, '0')

  return `${y}-${m}-${d} ${hh}:${mm}`
})


Vue.filter('dataMax', function (arr) {
  var max =Number(arr[0]) ;
 
  for (var item in arr){
    var cur=Number(arr[item])
    cur>max?max=cur:max
  }
  return  max.toFixed(1)
})

Vue.filter('dataMin', function (arr) {
  var min =Number(arr[0]) ;

  for (var item in arr){
    var cur=Number(arr[item])
    cur<min?min=cur:min
  }
  
  return  min.toFixed(1)
})

Vue.filter('dataMean', function (arr) {
  if (arr.length === 0) {
    return 0; 
  }
  var sum = arr.reduce(function (acc, cur) {
    return acc + Number(cur);
  }, 0);
  var mean = sum / arr.length;
  return mean.toFixed(1)
})