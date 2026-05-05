<script setup lang="ts">
import logo from "../assets/logo.svg";
</script>
<template>
  <div class="mx-auto min-h-screen flex flex-col py-32pt px-32pt md:py-32pt md:px-64pt">
    <header class="flex justify-between items-end pb-128pt">
      <RouterLink to="/" class="transition-opacity hover:opacity-70 active:scale-95">
        <img :src="logo" alt="Logo" class="h-8 md:h-10 w-auto" />
      </RouterLink>
      <p>Content Responsible</p>
    </header>
  </div>
</template>