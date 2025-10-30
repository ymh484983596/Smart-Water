import Vue from "vue";
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import myHome from '../components/myHome.vue'
import analysis from '../components/analysis.vue'
import totalN from '../views/totalN.vue'
import management from '../views/management.vue'
import evaluate from '../views/evaluate.vue'
import system from '../views/system.vue'
import test from '../views/test.vue'
import totalP from '../views/totalP.vue'
import totalChla from '../views/totalChla.vue'
Vue.use(VueRouter)


const routes = [
    {
        path: '/',
        redirect: 'login'
    },

    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/test',
        name: 'test',
        component: test,
    },
    {
        path: '/home',
        name: 'myHome',
        component: myHome,
        children: [
            {
                path: '/analysis',
                name: 'analysis',
                component: analysis,
                children: [
                    {
                        path: '/',
                        redirect: '/totalN',
                        name: 'totalN',
                        component: totalN,
                    },
                    {
                        path: '/totalN',
                        name: 'totalN',
                        component: totalN,
                    },
                    {
                        path: '/totalP',
                        name: 'totalP',
                        component: totalP,
                    },
                    {
                        path: '/totalChla',
                        name: 'totalChla',
                        component: totalChla,
                    },
                
                   
                ]
            },

           
            {
                path: '/management',
                name: 'management',
                component: management,
            }, 
            {
                path: '/system',
                name: 'system',
                component: system,
            },
            {
                path: '/evaluate',
                name: 'evaluate',
                component: evaluate,
            },
            

        ]
    },

]
const router = new VueRouter({
    routes
})

export default router

