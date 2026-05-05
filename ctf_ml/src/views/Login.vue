<script setup lang="ts">
import { ref } from 'vue'
import logo from "../assets/logo.svg";
import Footer from "../components/Footer.vue";
import Button from '../components/Button.vue'

const login = ref('')
const password = ref('')

const handleLogin = () => {
  console.log('Logging in with:', login.value, password.value)
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
      <h2 class="font-mono text-center pb-32pt">Welcome!</h2>

      <form @submit.prevent="handleLogin" class="flex flex-col gap-16pt w-full md:w-1/3 mx-auto">
        <!-- Поле логіну -->
        <div class="flex flex-col gap-4pt">
          <label class="font-mono text-xs uppercase opacity-60">Login</label>
          <input
              v-model="login"
              type="text"
              class="bg-transparent border-[3px] border-ui-white/20 focus:border-ui-accent outline-none px-8pt py-8pt font-mono text-ui-white transition-colors"
              placeholder="CTF(login)"
          />
        </div>

        <!-- Поле пароля -->
        <div class="flex flex-col gap-4pt">
          <label class="font-mono text-xs uppercase opacity-60">Password</label>
          <input
              v-model="password"
              type="password"
              class="bg-transparent border-[3px] border-ui-white/20 focus:border-ui-accent outline-none px-8pt py-8pt font-mono text-ui-white transition-colors"
              placeholder="CTF(password)"
          />
        </div>

        <!-- Біла кнопка Login -->
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