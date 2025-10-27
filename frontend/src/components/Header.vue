<script setup>
import { defineProps } from "vue";

defineProps({
  headerDivButtonText: String,
});
</script>

<template>
  <div class="header-div">
    <p class="header-p-logo">лотерея</p>
    <button class="header-div-button">{{ headerDivButtonText }}</button>
  </div>
</template>

<style scoped>
.header-div {
  display: flex;
  justify-content: space-between;
  padding: 20px;
}

.header-p-logo {
  font-size: 2em;
  font-weight: bold;
  cursor: pointer;
}

.header-div-button {
  background-color: #b25dfd;
  color: white;
  font-size: 1.5em;
  border: 0px;
  border-radius: 15px;
  padding: 7px 30px 7px 30px;
  cursor: pointer;
}

@media (max-width: 700px) {
  .header-p-logo {
    font-size: 1.6em;
  }

  .header-div-button {
    font-size: 1.1em;
    border-radius: 13px;
    padding: 8px 25px 8px 25px;
  }
}

@media (max-width: 450px) {
  .header-p-logo {
    font-size: 1.45em;
  }

  .header-div-button {
    font-size: 0.95em;
    border-radius: 11px;
    padding: 9px 20px 9px 2px;
  }
}
</style>
