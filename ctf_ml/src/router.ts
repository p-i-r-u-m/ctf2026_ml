import { createRouter, createWebHashHistory } from 'vue-router'
import Home from './views/Home.vue'
import LoginPage from './views/Login.vue'

const router = createRouter({
    history: createWebHashHistory(), // Саме Hash режим для стабільності на GH Pages
    routes: [
        { path: '/', component: Home },
        { path: '/login', component: LoginPage }
    ]
})

export default router