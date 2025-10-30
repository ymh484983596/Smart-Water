<template >
    <div style="background: #062047;overflow-x: hidden;padding:0px 24px 24px 24px ;">
        <div class="boxtop">
            <div class="titleWacth">
                <span style="margin-left: 16px;">用户管理>用户维护</span>
            </div>
            <div style="margin-top: 16px;">
                <el-row>
                    <el-col :span="3">
                        <el-select :popper-append-to-body="false" size="mini" v-model="quearyJg" placeholder="请选择">
                            <el-option v-for="item in JgList" :key="item.value" :label="item.label" :value="item.value">
                            </el-option>
                        </el-select>
                    </el-col>
                    <el-col :span="3">
                        <el-select :popper-append-to-body="false" size="mini" v-model="quearyYy" placeholder="请选择">
                            <el-option v-for="item in YyList" :key="item.value" :label="item.label" :value="item.value">
                            </el-option>
                        </el-select>
                    </el-col>
                    <el-col :span="3">
                        <el-input size="mini" placeholder="请输入账号查询" v-model="quearyName" class="input-with-select">
                            <el-button slot="append" icon="el-icon-search"></el-button>
                        </el-input>
                    </el-col>
                    <el-col :span="9">
                        <div style="width: 100%;"> &nbsp;</div>
                    </el-col>
                    <el-col :span="6">
                        <div class="btnclass">应用授权</div>
                        <div class="btnclass">禁用</div>
                        <div class="btnclass">启动</div>
                        <div class="btnclass">删除</div>
                        <div class="btnclass">添加</div>
                    </el-col>
                </el-row>
            </div>
            <div style="margin-top: 16px;">
                <div class="table">
                    <div class="tableLabel">
                        <div class="itemTable" style="width: 5%;"> <el-checkbox @change="checkChange"
                                v-model="checked"></el-checkbox></div>
                        <div class="itemTable">账号</div>
                        <div class="itemTable">姓名</div>
                        <div class="itemTable">所属机构</div>
                        <div class="itemTable">手机号</div>
                        <div class="itemTable">邮箱</div>
                        <div class="itemTable">地址</div>
                        <div class="itemTable">状态</div>
                        <div class="itemTable">操作</div>
                    </div>
                    <div style="height: 600px;overflow-y: auto;">
                        <div :style="{ background: index == activeIndex ? '#224B93' : '#072951' }" class="itemRow"
                            @click="rowClick(item, index)" v-for="(item, index) in tableList" :key="index">
                            <div class="itemCenter" style="width: 5%;"><el-checkbox @change="checkItemChang"
                                    v-model="item.checked"></el-checkbox>
                            </div>
                            <div class="itemCenter">{{ item.zhNum }}</div>
                            <div class="itemCenter">{{ item.name }}</div>
                            <div class="itemCenter">{{ item.jgName }}</div>
                            <div class="itemCenter">{{ item.phone }}</div>
                            <div class="itemCenter">{{ item.mailbox }}</div>
                            <div class="itemCenter">{{ item.address }}</div>
                            <div class="itemCenter"><el-tag type="success">{{ item.status == 1 ? "开启" : "禁用" }}</el-tag>
                            </div>
                            <div class="itemCenter"><span @click.stop="Openedit(item)" class="el-icon-edit-outline"></span>
                            </div>
                        </div>
                    </div>
                </div>
                <div style="float: right;margin-top: 20px;">
                    <el-pagination background layout="prev, pager, next" :total="1000">
                    </el-pagination>
                </div>
            </div>
        </div>

        <el-dialog title="编辑" :visible.sync="dialogVisible" width="25%" :before-close="handleClose">
            <el-form label-width="100px">
                <el-row type="flex">
                    <el-col :span="24">
                        <el-form-item label="编号：">
                            <el-input clearable size="mini" placeholder="请输入编号" v-model="objBj.bhNum">
                            </el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row type="flex">
                    <el-col :span="24">
                        <el-form-item label="账号：">
                            <el-input clearable size="mini" placeholder="请输入账号" v-model="objBj.zhNum"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row type="flex">
                    <el-col :span="24">
                        <el-form-item label="密码：">
                            <el-input clearable size="mini" type="password" placeholder="请输入密码"
                                v-model="objBj.passwrd"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row type="flex">
                    <el-col :span="24">
                        <el-form-item label="确认密码：">
                            <el-input clearable size="mini" type="password" v-model="objBj.passwrdOld"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row type="flex">
                    <el-col :span="24">
                        <el-form-item label="姓名：">
                            <el-input clearable size="mini" placeholder="请输入姓名" v-model="objBj.name"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row type="flex">
                    <el-col :span="24">
                        <el-form-item label="手机号：">
                            <el-input clearable size="mini" placeholder="请输入手机号" v-model="objBj.phone"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row type="flex">
                    <el-col :span="24">
                        <el-form-item label="邮箱：">
                            <el-input clearable size="mini" placeholder="请输入邮箱" v-model="objBj.mailbox"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row type="flex">
                    <el-col :span="24">
                        <el-form-item label="地址：">
                            <el-input clearable size="mini" placeholder="请输入地址" v-model="objBj.address"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button size="mini" @click="dialogVisible = false">取 消</el-button>
                <el-button style="background: #075EC0;" size="mini" type="primary" @click="save">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>
  
<script>

export default {
    data() {
        return {
            activeIndex: -1,
            objBj: {
                zhNum: "",
                bhNum: "",
                name: "",
                phone: "",
                passwrd: "",
                passwrdOld: "",
                mailbox: "",
                address: "",
            },
            dialogVisible: false,
            checked: false,
            quearyName: "",
            quearyJg: "1",
            quearyYy: "1",
            titleTime: null,
            titleTimeRight: null,
            JgList: [{
                label: "全部机构",
                value: "1"
            }
            ],
            YyList: [{
                label: "全部应用",
                value: "1"
            }

            ],
            tableList: [
                {
                    zhNum: "账号1",
                    name: "测试1",
                    phone: "12345689115",
                    jgName: "机构1",
                    address: "湖北省武汉市",
                    status: 1,
                    mailbox: "345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号2",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号3",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号4",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号5",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号6",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号7",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号8",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号9",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号10",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号11",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号12",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号13",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号14",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
                {
                    zhNum: "账号15",
                    name: "测试2",
                    phone: "18871445555",
                    jgName: "机构2",
                    address: "湖北省武汉市2",
                    status: 0,
                    mailbox: "1364345895@qq.com",
                    checked: false,
                },
            ]
        }
    },
    created() {
        // 1.密码由数字跟字母组成 2.不能含有空格 3.不能为常见密码
    },
    methods: {
        Openedit(item) {
            this.dialogVisible = true
            this.objBj = item
        },
        handleClose() {
            this.dialogVisible = false
        },
        save() {
            this.dialogVisible = false
        },
        rowClick(item, index) {
            console.log(11111);
            this.activeIndex = index
        },
        checkChange() {
            this.tableList.forEach((item) => {
                item.checked = this.checked
            })
        },
        checkItemChang() {
            if (this.tableList.filter((item) => !item.checked).length == 0) {
                this.checked = true
            } else {
                this.checked = false
            }

        }
    },
}
</script>
  
<style lang="scss" scoped>
@import "./css/index.scss";

/deep/ .el-input-group__append {
    background: rgba(1, 32, 78, 0.85) !important;
    color: #bfbfbf !important;
    border-color: #3b4f75 !important;
}

/deep/ .el-form-item__label {
    color: #fff !important;
}

/deep/ .el-dialog__title {
    color: #fff !important;
    font-size: 18px;
    font-family: "Microsoft YaHei", "Microsoft YaHei-Bold";
    font-weight: 700;
}

/deep/ .el-dialog__header {
    background: #072951 !important;
    color: #fff;
    text-align: left !important;
}

/deep/ .el-dialog__body {
    background: #072951 !important;
    color: #fff;
}

/deep/ .el-dialog__footer {
    background: #072951 !important;
    color: #fff;
}

/deep/ .el-pagination.is-background .el-pager li {
    background-color: #072951 !important;
    color: #fff !important;
}

/deep/ .el-pagination.is-background .btn-next {
    background-color: #072951 !important;
    color: #fff !important;
}

/deep/ .el-pagination.is-background .btn-prev {
    background-color: #072951 !important;
    color: #fff !important;
}

/deep/.el-pagination .is-background .el-pager li.active {
    color: #409EFF !important;
    cursor: default !important;
}

/deep/.el-pagination.is-background .el-pager li:not(.disabled).active {
    color: #409EFF !important;
    cursor: default !important;
}




.table {
    border: 1px solid #073673;

}

.itemRow {
    display: flex;
    cursor: pointer;
}



.tableLabel {
    display: flex;
    background: #0F1F40;

    .itemTable {
        width: 25%;
        height: 50px;
        line-height: 50px;
        text-align: center;
        color: #fff;
        font-size: 16px;
        font-weight: 500;
    }
}

.itemCenter {
    width: 25%;
    height: 50px;
    line-height: 50px;
    text-align: center;
    color: #fff;
    font-size: 14px;
    font-weight: 400;
    // background: #072951;

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
    margin: 0 5px;
}

.titleWacth {
    background-color: #1B4B78;
    height: 40px;
    line-height: 40px;
    color: #fff;
    width: 100%;
    text-align: left;
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

.boxtop {
    height: 50%;
    width: 100%;
    background: #062047;
    text-align: left;
}
</style>
  