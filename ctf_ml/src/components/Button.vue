<script setup lang="ts">
// Компонент-кнопка з адаптивним текстом
</script>

<template>
  <button
      class="
      /* 1. Основа та позиціювання */
      inline-block cursor-pointer

      /* 2. ТВОЯ АДАПТАЦІЯ ТЕКСТУ (як у <p>) */
      text-base md:text-lg
      tracking-tighter

      /* 3. Рамка та кольори */
      border-[3px] border-ui-accent
      bg-transparent

      /* 4. Внутрішні відступи (padding) */
      px-16pt py-8pt

      /* 5. Анімації та Ховер */
      transition-all
      hover:bg-ui-accent hover:text-ui-white
      active:scale-95
    "
  >
    <slot />
  </button>
</template>