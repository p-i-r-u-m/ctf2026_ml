<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import logo from "../assets/logo.svg";
import Footer from "../components/Footer.vue";
import Button from '../components/Button.vue'

const router = useRouter()
const login = ref('')
const password = ref('')
const errorMessage = ref('')

const handleLogin = async () => {
  errorMessage.value = '' // Очищуємо стару помилку

  try {
    const formData = new FormData()
    formData.append('username', login.value) // FastAPI хоче саме 'username'
    formData.append('password', password.value)

    const response = await fetch('https://ctf2026-ml.onrender.com/login', {
      method: 'POST',
      body: formData,
    })

    if (!response.ok) {
      // Якщо бекенд повернув 401 або іншу помилку
      const errorData = await response.json()
      throw new Error(errorData.detail || 'Access Denied')
    }

    const data = await response.json()

    // Зберігаємо JWT у браузері
    localStorage.setItem('access_token', data.access_token)

    console.log('Success! Token saved.')
    router.push('/content_resp') // Перенаправляємо на головну сторінку CTF

  } catch (err: any) {
    errorMessage.value = err.message
  }
}
</script>

<template>
  <div class="mx-auto min-h-screen flex flex-col py-32pt px-32pt md:py-32pt md:px-64pt">
    <header class="flex justify-between items-end pb-128pt">
      <RouterLink to="/" class="transition-opacity hover:opacity-70 active:scale-95">
        <img :src="logo" alt="Logo" class="h-8 md:h-10 w-auto" />
      </RouterLink>
      <p>Content Responsible</p>
    </header>

    <main class="grow">
      <h2 class="font-mono text-center pb-32pt">Welcome</h2>

      <!-- Оновлена форма -->
      <form @submit.prevent="handleLogin" class="flex flex-col gap-16pt w-full md:w-1/3 mx-auto">
        <div class="flex flex-col gap-4pt">
          <label class="font-mono text-xs uppercase opacity-60">Login</label>
          <input
              v-model="login"
              type="text"
              class="bg-transparent border-[3px] border-ui-white/20 focus:border-ui-accent outline-none px-8pt py-8pt font-mono text-ui-white transition-colors"
              placeholder="CTF(user)"
              required
          />
        </div>

        <div class="flex flex-col gap-4pt">
          <label class="font-mono text-xs uppercase opacity-60">Password</label>
          <input
              v-model="password"
              type="password"
              class="bg-transparent border-[3px] border-ui-white/20 focus:border-ui-accent outline-none px-8pt py-8pt font-mono text-ui-white transition-colors"
              placeholder="CTF(********)"
              required
          />
        </div>

        <!-- Блок помилки -->
        <p v-if="errorMessage" class="text-red-500 font-mono text-[10px] text-center uppercase bg-red-500/10 py-4pt border border-red-500/20">
          Error: {{ errorMessage }}
        </p>

        <div class="mt-8pt">
          <Button white fullWidth type="submit">
            Log In
          </Button>
        </div>
      </form>
    </main>

    <Footer></Footer>
  </div>
</template>