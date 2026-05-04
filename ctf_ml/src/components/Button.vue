<script setup lang="ts">
// Додаємо проп fullWidth для керування шириною
const props = defineProps<{
  to?: string,
  href?: string,
  white?: boolean,
  fullWidth?: boolean
}>()

// Формуємо класи з урахуванням нових станів
const buttonClasses = `
  cursor-pointer text-center no-underline
  text-sm md:text-lg tracking-tighter
  border-[3px] transition-all active:scale-95
  px-24pt py-8pt

  /* 1. Логіка розтягування: flex дозволяє ідеально центрувати текст */
  ${props.fullWidth ? 'flex w-full items-center justify-center' : 'inline-flex items-center justify-center'}

  /* 2. Колірна логіка для білої та стандартної кнопок */
  ${props.white
    ? 'bg-ui-white text-ui-black border-ui-white hover:bg-ui-white hover:text-ui-accent'
    : 'bg-transparent border-ui-accent hover:bg-ui-accent hover:text-ui-white'}
`
</script>

<template>
  <!-- Внутрішній лінк -->
  <RouterLink v-if="to" :to="to" :class="buttonClasses">
    <slot />
  </RouterLink>

  <!-- Зовнішній лінк -->
  <a v-else-if="href" :href="href" :class="buttonClasses" target="_blank" rel="noopener">
    <slot />
  </a>

  <!-- Звичайна кнопка -->
  <button v-else :class="buttonClasses">
    <slot />
  </button>
</template>