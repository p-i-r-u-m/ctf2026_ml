<script setup lang="ts">
import logo from '../assets/logo.svg'
import Button from '../components/Button.vue'
import Footer from '../components/Footer.vue'

</script>

<template>
  <div class="mx-auto min-h-screen flex flex-col py-32pt px-32pt md:py-32pt md:px-64pt">

    <header class="flex justify-between items-end pb-128pt">
      <RouterLink to="/" class="transition-opacity hover:opacity-70 active:scale-95">
      <img :src="logo" alt="Logo" class="h-8 md:h-10 w-auto" />
      </RouterLink>
    </header>

    <main class="grow">
      <h2 class="font-mono">
        Motivation letter
      </h2>
      <h1 class="font-mono pb-16pt md:pb-32pt">
        Ivan Hrushevskyi
      </h1>

      <div class="flex gap-8pt">
        <Button to="/login">Content Responsible</Button>
        <Button to="/it_resp">IT Responsible</Button>
      </div>

    </main>

    <Footer></Footer>

  </div>
</template>
