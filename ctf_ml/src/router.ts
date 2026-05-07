import { createRouter, createWebHashHistory } from 'vue-router'
import Home from './views/Home.vue'
import LoginPage from './views/Login.vue'
import ContentPage from './views/Content_Resp.vue'
import ITPage from './views/IT_Resp.vue'

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/', component: Home },
        { path: '/it_resp', component: ITPage },
        { path: '/login', component: LoginPage },
        {
            path: '/content_resp',
            component: ContentPage,
            meta: { requiresAuth: true }
        }
    ],
    // Додай цей блок:
    // Зміни рядок 20 на цей:
scrollBehavior(_to, _from, savedPosition) { 
    if (savedPosition) {
        return savedPosition
    } else {
        return { top: 0, behavior: 'smooth' }
    }
}
})

// Новий синтаксис: повертаємо значення замість виклику next()
router.beforeEach((to) => {
    const isAuthRequired = to.matched.some(record => record.meta.requiresAuth)
    const token = localStorage.getItem('access_token')

    // ДЕБАГ: Розкоментуй цей рядок, щоб побачити в консолі, що там лежить
    // console.log('Auth Check:', { path: to.path, token: token, required: isAuthRequired });

    // Якщо шлях вимагає авторизації, а токена немає (null або пустий)
    if (isAuthRequired && !token) {
        return '/login'
    }

    // Якщо юзер залогінений і лізе на сторінку логіну
    if (to.path === '/login' && token) {
        return '/content_resp'
    }

    // В усіх інших випадках просто нічого не повертаємо (це аналог next())
})

export default router