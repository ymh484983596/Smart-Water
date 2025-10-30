<template>
  <el-container class="home-container">
    <el-header>
      <div>
        <img class="logo" src="../assets/11.png" alt="">
        <span>宁波市城市河道污染数据智慧监控平台</span>
      </div>
      <!-- <el-menu  class="el-menu-demo" :mode="'horizontal'" @select="handleSelect" router>
        <el-menu-item index="/evaluate" >水质评价</el-menu-item>
        <el-menu-item index="/management">数据管理</el-menu-item>
        <el-menu-item index="/analysis">数据分析</el-menu-item>
        <el-menu-item index="/system">系统管理</el-menu-item>
      </el-menu> -->
      <div class="meunDiv">
        <div :style="{ background: index == activeIndex ? '#fff' : '#597898' }" v-for="(item, index) in  routerList"
          :key="index" @click="GOpath(item, index)">
          {{ item.name }}
        </div>
      </div>
      <el-button type="info" @click="logout">退出</el-button>
    </el-header>
    <el-main>
      <router-view ref="aaaaa"></router-view>
    </el-main>

  </el-container>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: 0,
      routerList: [
        {
          name: "水质评价",
          active: 0,
          url: '/evaluate'
        },
        {
          name: "数据管理",
          active: 1,
          url: '/management'
        },
        {
          name: "数据分析",
          active: 2,
          url: '/analysis'
        },
        {
          name: "系统管理",
          active: 1,
          url: '/system'
        }
      ],
      isCollapse: false
    }
  },
  methods: {
    GOpath(item, index) {
      this.activeIndex = index
      if (item.name == '数据管理') {
        this.$router.push({ path: item.url, query: { objName: '站点2' } })
        return
      }
      this.$router.push({ path: item.url })
    },
    handleSelect(key, keyPath) {
    },
    logout() {
      this.$router.push("/login");
      sessionStorage.setItem('zdname','' );
    },
    toggleCollapse() {
      this.isCollapse = !this.isCollapse
    }
  },
  created() {
    if (sessionStorage.getItem('zdname') == 1) {
      this.activeIndex=1
    }

  }
}
</script>

<style lang="less" scoped>
.meunDiv {
  display: flex;
  align-items: center;
  width: 800px;
}

.meunDiv div:hover {
  background: #fff;
}

.meunDiv div {
  flex: 1;
  cursor: pointer;
  height: 60px;
  line-height: 60px;
}

.home-container {
  height: 100%;
}

.el-header {
  background-color: #597898;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  font-size: 20px;

  >div {
    display: flex;
    align-items: center;

    span {
      margin-left: 15px;
      font-size: 25px;
    }
  }
}

.el-aside {
  background-color: #373d44;

  .el-menu {
    border-right: none;
    background-color: #597898;



  }
}

.el-main {
  background-color: #062047;
}

.logo {
  height: 60px;
}

.iconfont {
  margin-right: 15px;
}

.toggle-button {
  background-color: #4A5064;
  font-size: 20px;
  line-height: 24px;
  color: #000000;
  text-align: center;
  letter-spacing: 0.2em;
  cursor: pointer;
}

.el-menu-item {
  background-color: #597898;
  font-size: 24px;
  color: #3b0606;
  letter-spacing: 4px;
  // padding-right:80px;

}
</style>
