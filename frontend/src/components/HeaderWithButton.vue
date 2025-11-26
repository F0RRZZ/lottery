<script setup>
import { defineProps } from "vue";

defineProps({
  headerDivButtonText: String,
  headerDivButtonLink: String,
});
</script>

<template>
  <div class="header-div">
    <router-link class="header-logo" to="/">лотерея</router-link>
    <router-link :to="headerDivButtonLink" class="header-div-button">{{
      headerDivButtonText
    }}</router-link>
  </div>
</template>

<style scoped>
.header-div {
  gap: 3px;
  display: flex;
  justify-content: space-between;
  padding: 20px;
  gap: 10px;
}

.header-logo {
  font-size: 2em;
  font-weight: bold;
  cursor: pointer;
  text-decoration: none;
  color: black;
}

.header-div-button {
  background-color: #b25dfd;
  color: white;
  font-size: 1.5em;
  border: 0px;
  border-radius: 15px;
  padding: 7px 30px 7px 30px;
  cursor: pointer;
  text-decoration: none;
  text-align: center;
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
    padding: 9px 20px 9px 20px;
  }
}
</style>
