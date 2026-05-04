<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>
<template>
  <main class="grow">
    <RouterView v-slot="{ Component }">
      <transition name="page-fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </RouterView>
  </main>
</template>

<style>
/*
  Додаємо стилі анімації прямо сюди або в style.css.
  Використовуємо 8px (системний крок) для зміщення.
*/
.page-fade-enter-active,
.page-fade-leave-active {
  transition:
      opacity 0.3s ease,
      transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.page-fade-enter-from,
.page-fade-leave-to {
  opacity: 0;
  transform: translateY(8px);
}
</style>