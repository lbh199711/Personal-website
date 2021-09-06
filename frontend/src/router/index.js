import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import ProjectPage from '../views/ProjectPage.vue'
import SaModelPage from '../views/SaModelPage.vue'
import PageNotFound  from '../views/PageNotFound.vue'


const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/project/:name',
        name: 'ProjectPage',
        component: ProjectPage
    },
    {
        path: '/sa_model',
        name: 'SaModelPage',
        component: SaModelPage
    }
    ,
    {
        path: '/404',
        name: '404',
        component: PageNotFound 
    },
    {
        path: '/:catchAll(.*)',
        name: 'default',
        redirect: '/404' 
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
