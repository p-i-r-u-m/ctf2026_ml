<script setup lang="ts">
import logo from './assets/logo.svg'
import Button from './components/Button.vue'
</script>

<template>
  <div class="mx-auto min-h-screen flex flex-col pt-4 px-4 pb-4 md:pt-8 md:pb-4 md:px-16">

    <header class="flex justify-between items-end pb-128pt">
      <img :src="logo" alt="Logo" class="h-8 md:h-10 w-auto" />
    </header>

    <main class="grow">
      <h2 class="">
        Motivation letter
      </h2>
      <h1 class="pb-16pt">
        Ivan Hrushevskyi
      </h1>

      <div class="flex gap-8pt">
        <Button>Content Responsible</Button>
        <Button>IT Responsible</Button>
      </div>

    </main>

    <footer class="mt-32pt pt-16pt border-t border-ui-white/10 font-mono text-sm opacity-40">
      root@localhost ~ # _
    </footer>

  </div>
</template>
