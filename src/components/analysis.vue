<template>
  <el-container class="home-container">
    <el-aside :width="isCollapse ? '64px' : '250px'">
      <div class="toggle-button" @click="toggleCollapse">|||</div>
      <el-menu unique-opened :collapse="isCollapse"
               background-color="#14395b" :collapse-transition="false"
               text-color="#fff" active-text-color="#409EFF" router>
        <el-menu-item index="/totalN">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>总氮分布图</span>
          </template>
        </el-menu-item>
        <el-menu-item index="/totalP" >
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>总磷分布图</span>
            </template>
          </el-menu-item>
          <el-menu-item index="/totalChla" >
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>叶绿素a分布图</span>
            </template>
          </el-menu-item>
        

      </el-menu>
    </el-aside>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: "otherHome",
  data(){
    return {
      isCollapse: false
    }
  },
  methods:{
    handleSelect(key, keyPath) {

    },
    logout(){

    },
    toggleCollapse(){
      this.isCollapse=! this.isCollapse
    }
  }
}
</script>

<style lang="less" scoped>
.home-container{
  height: 100%;
}
.el-aside{
  background-color: #14395b;
  margin-left: -20px;
  margin-top: -20px;
  .el-menu{
    border-right: none;
  }
}

.logo{
  height: 60px;
}

.toggle-button{
  background-color: #4A5064;
  font-size: 10px;
  line-height: 30px;
  color: #fff;
  text-align: center;
  letter-spacing: 0.2em;
  cursor: pointer;
}
</style>
