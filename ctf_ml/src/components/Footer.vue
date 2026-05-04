<script setup lang="ts">
import { ref, onMounted } from 'vue';

const commands = ['ls -la', 'cat motivation.txt', 'whoami', 'clear', './deploy.sh'];
const displayText = ref('');
const commandIndex = ref(0);
const isDeleting = ref(false);
const typeSpeed = ref(150);

const typeEffect = () => {
  const currentFullText = commands[commandIndex.value];

  if (isDeleting.value) {
    // Витираємо текст
    displayText.value = currentFullText.substring(0, displayText.value.length - 1);
    typeSpeed.value = 50; // Витираємо швидше
  } else {
    // Пишемо текст
    displayText.value = currentFullText.substring(0, displayText.value.length + 1);
    typeSpeed.value = 150;
  }

  // Якщо слово надруковане повністю
  if (!isDeleting.value && displayText.value === currentFullText) {
    typeSpeed.value = 2000; // Пауза перед витиранням
    isDeleting.value = true;
  }
  // Якщо слово повністю витерте
  else if (isDeleting.value && displayText.value === '') {
    isDeleting.value = false;
    commandIndex.value = (commandIndex.value + 1) % commands.length;
    typeSpeed.value = 500;
  }

  setTimeout(typeEffect, typeSpeed.value);
};

onMounted(() => {
  typeEffect();
});
</script>

<template>
  <footer class="mt-32pt pt-16pt border-t border-ui-white/10 font-mono text-sm opacity-40">
    root@localhost ~ # {{ displayText }}<span class="terminal-cursor">_</span>
  </footer>
</template>