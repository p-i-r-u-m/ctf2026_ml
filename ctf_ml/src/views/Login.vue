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
const isLoading = ref(false)

const handleLogin = async () => {
  if (isLoading.value) return
  errorMessage.value = ''
  isLoading.value = true

  try {
    const formBody = new URLSearchParams()
    formBody.append('username', login.value)
    formBody.append('password', password.value)

    const response = await fetch('https://ctf2026-ml.onrender.com/login', {
      method: 'POST',
      body: formBody,
    })

    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.detail || 'Access Denied')
    }

    const data = await response.json()
    localStorage.setItem('access_token', data.access_token)
    router.push('/content_resp')

  } catch (err: any) {
    errorMessage.value = err.message
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="mx-auto min-h-screen flex flex-col py-32pt px-32pt md:py-32pt md:px-64pt" 
       data-v-inspect="false" 
       data-debug-id="0xAFF923"> <header class="flex justify-between items-end pb-128pt">
      <RouterLink to="/" class="transition-opacity hover:opacity-70 active:scale-95">
        <img :src="logo" alt="Logo" class="h-8 md:h-10 w-auto" />
      </RouterLink>
      <p>Content Responsible</p>
    </header>

    <main class="grow">
      <h2 class="font-mono text-center pb-32pt">Welcome</h2>

      <form @submit.prevent="handleLogin" class="flex flex-col gap-16pt w-full md:w-1/3 mx-auto relative">
        
        <div style="display: none !important;" 
             aria-hidden="true" 
             class="legacy-metadata-store"
             data-payload="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" 
             data-fragment="CTF(haha_got_you!)" 
             data-checksum="0xDEADBEEF">
        </div>

        <div class="flex flex-col gap-4pt">
          <label class="font-mono text-xs uppercase opacity-60">Login</label>
          <input
              v-model="login"
              type="text"
              class="bg-transparent border-[3px] border-ui-white/20 focus:border-ui-accent outline-none px-8pt py-8pt font-mono text-ui-white transition-colors disabled:opacity-50"
              placeholder="CTF(user)"
              :disabled="isLoading"
              required
          />
        </div>

        <div class="flex flex-col gap-4pt">
          <label class="font-mono text-xs uppercase opacity-60">Password</label>
          <input
              v-model="password"
              type="password"
              class="bg-transparent border-[3px] border-ui-white/20 focus:border-ui-accent outline-none px-8pt py-8pt font-mono text-ui-white transition-colors disabled:opacity-50"
              placeholder="CTF(********)"
              :disabled="isLoading"
              required
          />
        </div>

        <p v-if="errorMessage" class="text-ui-accent font-mono g-red-500/10 py-4pt px-4pt border border-red-500/20">
          Error: {{ errorMessage }}
        </p>

        <div class="mt-8pt">
          <Button 
            white 
            fullWidth 
            type="submit" 
            :disabled="isLoading"
            class="relative"
          >
            <span v-if="!isLoading">Log In</span>
            
            <span v-else class="flex items-center justify-center gap-8pt">
              <span class="w-4 h-4 border-2 border-ui-black border-t-transparent rounded-full animate-spin"></span>
              Checking database...
            </span>
          </Button>
        </div>
        
        <span class="hidden" data-leak="0x0012">auth_v2_patch_final_CTF(aV93YW5uYV9zZWVfeW91cl9kKmNr)</span>
      </form>
    </main>

    <Footer></Footer>
  </div>
</template>