<template>
  <div class="container">
   <div class="textbox">{{ intro }}</div>
   <div style="height:20px"></div>

   <div class="list1">

     <div class="list2">
        <div style="height:25px;"></div> 
        <div style="font-weight: bold; font-size: 23px;">环境参数选择</div>
        <div style="margin: 30px 0;"></div> 
        <div class="checkbox-container">
            <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange">全选</el-checkbox>
            <div style="margin: 0 15px;"></div>
            <el-checkbox-group v-model="checkedCities" @change="handleCheckedCitiesChange">
                <div class="checkbox-wrapper" v-for="city in cities" :key="city">
                    <el-checkbox :label="city">{{ city }}</el-checkbox>
                </div>
            </el-checkbox-group>   
        </div>
     </div>

    <div class="list3">
        <div class="list3-1">
            <el-button type="primary" icon="el-icon-edit" circle @click="handle"></el-button>
            <div style="margin: 0 5px;"></div>
            <div style="font-size: 23px;">运行分析</div>
        </div>
        <div style="margin: 10px 0;"></div> 
        <div class="list3-2" style="justify-content: center; text-align: center;">
        <img v-if="showImage" :src="imageURL" alt="Image" style="object-fit: cover; width: 90%; height: 90%;">
        </div>
    </div>
    

    <div class="list2">
        <div style="height:25px;"></div> 
        <div style="font-weight: bold; font-size: 23px;">分析结果</div>
        <div style="margin: 70px 0;"></div> 
        <div class='list4-2'>
          <el-dropdown :hide-on-click="false" @command="handleCommand">
            <span class="el-dropdown-link">{{ii}}<i class="el-icon-arrow-down el-icon--right"></i>
            </span>
          <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="叶长" :disabled="isItemDisabled1">叶长</el-dropdown-item>
          <el-dropdown-item command="叶宽" :disabled="isItemDisable2">叶宽</el-dropdown-item>
          <el-dropdown-item command="叶片数" :disabled="isItemDisabled3">叶片数</el-dropdown-item>
          <el-dropdown-item command="茎粗" :disabled="isItemDisabled4">茎粗</el-dropdown-item>
          <el-dropdown-item command="株高" :disabled="isItemDisabled5">株高</el-dropdown-item>
          </el-dropdown-menu>
          </el-dropdown>
          <div style="margin: 0 5px;"></div> 
          <input type="text" v-model="userInput" placeholder="结果" style="background-color: transparent;">
        </div>
    </div>


   </div>
    

  </div>
</template>

<script>
const cityOptions = ['温度', '湿度', '光照强度', 'CO2浓度','土壤湿度','土壤温度','土壤PH值'];
export default {
  data() {
    return {
      intro: 'LASSO回归又称为套索回归，是Robert Tibshirani于1996年提出的一种新的变量选择技术。Lasso是一种收缩估计方法，其基本思想是在回归系数的绝对值之和小于一个常数的约束条件下，使残差平方和最小化，从而能够产生某些严格等于0的回归系数，进一步得到可以解释的模型。\n'+
      '       LASSO回归的特点是在拟合广义线性模型的同时进行变量筛选（variable selection）和复杂度调整（regularization）。因此，不论因变量是连续的（continuous），还是二元或者多元离散的（discrete），都可以用 LASSO 回归建模然后预测。算法中的复杂度调整是指通过一系列参数控制模型的复杂度，从而避免过度拟合（overfitting）。',


      checkAll: false,
      checkedCities: ['温度', '湿度'],
      cities: cityOptions,
      isIndeterminate: true,

      list: [],
      showImage: false, // 控制是否显示图片
      imageURL: "",
      ii:"叶长",
      isItemDisabled1:true,
      isItemDisabled2:false,
      isItemDisabled3:false,
      isItemDisabled4:false,
      isItemDisabled5:false,
      userInput:0,
    };
  },
  methods: {
      handleCommand(command) {
        this.ii=command;
        if(command==="叶长"){
          this.isItemDisabled1=true;
          this.isItemDisabled2=false;
          this.isItemDisabled3=false;
          this.isItemDisabled4=false;
          this.isItemDisabled5=false;
        }else if(command==="叶宽"){
          this.isItemDisabled1=false;
          this.isItemDisabled2=true;
          this.isItemDisabled3=false;
          this.isItemDisabled4=false;
          this.isItemDisabled5=false;
        }else if(command==="叶片数"){
          this.isItemDisabled1=false;
          this.isItemDisabled2=false;
          this.isItemDisabled3=true;
          this.isItemDisabled4=false;
          this.isItemDisabled5=false;
        }else if(command==="茎粗"){
          this.isItemDisabled1=false;
          this.isItemDisabled2=false;
          this.isItemDisabled3=false;
          this.isItemDisabled4=true;
          this.isItemDisabled5=false;
        }else if(command==="株高"){
          this.isItemDisabled1=false;
          this.isItemDisabled2=false;
          this.isItemDisabled3=false;
          this.isItemDisabled4=false;
          this.isItemDisabled5=true;
        }
      },
      handleCheckAllChange(val) {
        this.checkedCities = val ? cityOptions : [];
        this.isIndeterminate = false;
      },
      handleCheckedCitiesChange(value) {
        let checkedCount = value.length;
        this.checkAll = checkedCount === this.cities.length;
        this.isIndeterminate = checkedCount > 0 && checkedCount < this.cities.length;
      },
      handle(){
        console.log(this.checkedCities);
        console.log(this.checkedCities.length)
        if(this.checkedCities.length<2){
            this.$message.error("需要两个以上变量")
        }
        if(this.checkedCities.length===2){
            if(this.checkedCities[0]==="温度"&&this.checkedCities[1]==="湿度"&&this.ii==="叶长"){
                this.userInput=1
                this.showImage=true
                this.imageURL=require('@/assets/images/farminfo/farm1.jpg') // 图片的 URL
            }else if(this.checkedCities[0]==="温度"&&this.checkedCities[1]==="光照强度"){
                this.list=['光照强度']
            }
        }else if(this.checkedCities.length===3){
              if(this.checkedCities[0]==="温度"&&this.checkedCities[1]==="湿度"&&this.checkedCities[2]==="光照强度"){
                this.list=['温度','湿度']
            }
        }else if(this.checkedCities.length===4){
              if(this.checkedCities[0]==="温度"&&this.checkedCities[1]==="湿度"&&this.checkedCities[2]==="光照强度"&&this.checkedCities[3]==="CO2浓度"){
                this.list=['温度','湿度',"CO2浓度"]
            }
        }else if(this.checkedCities.length===5){
              if(this.checkedCities[0]==="温度"&&this.checkedCities[1]==="湿度"&&this.checkedCities[2]==="光照强度"&&this.checkedCities[3]==="CO2浓度"&&this.checkedCities[4]==="土壤湿度"){
                this.list=['温度','湿度',"CO2浓度","光照强度"]
            }
        }else if(this.checkedCities.length===6){
              if(this.checkedCities[0]==="温度"&&this.checkedCities[1]==="湿度"&&this.checkedCities[2]==="光照强度"&&this.checkedCities[3]==="CO2浓度"&&this.checkedCities[4]==="土壤湿度"&&this.checkedCities[5]==="土壤温度"){
                this.list=['温度','湿度',"土壤湿度","土壤温度"]
            }
        }else if(this.checkedCities.length===7){
                this.list=['温度','湿度','光照强度', 'CO2浓度','土壤湿度']
        }
        
      }
  }
};
</script>


<style>
.container {
  display: flex;
  flex-direction: column;
  margin-top: 5px; /* 距离顶部的距离 */
}

.textbox {
  padding: 20px; /* 左右空白距离 */
  font-family: Arial, sans-serif; /* 设置字体 */
  font-size: "15px";
  text-indent: 2em; /* 首段缩进两个空格 */
  white-space: pre-wrap;
}

.list1{
  display: flex;
  flex-direction: row;
  margin-left: 80px;
  margin-right: 80px;
}

.list2{
  flex: 1;
  height: 300px;
  background-color: #F6CB90; /* 设置背景颜色，仅为示例*/
  flex-direction: column;
  justify-content: center;
  text-align: center;
  border: 2px solid black; /* 设置边框样式：2像素宽度，实线，黑色 */
}

.list3{
  flex: 2;
  display: flex;
  align-items: center;
  /* justify-content: center; */
  flex-direction: column;
}

.list3-1{
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
}

.list4-2{
  justify-content: center;
  text-align: center;
  display: flex;
  flex-direction: row;
}

.checkbox-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start; 
}

.checkbox-wrapper {
  margin-bottom: 10px;
  text-align: left;  
}
</style>