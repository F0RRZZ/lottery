<script setup>
import MainPage from "./views/MainPage.vue";
import RegisterPage from "./views/RegisterPage.vue";

const tokenURL = "http://localhost:8000/auth/token";

const getToken = async (info) => {
  const response = await fetch(tokenURL, {
    method: "POST",
    headers: {
      "Content-Type": "apploication/json",
    },
    body: JSON.stringify(info),
  });
};
</script>

<template>
  <RegisterPage />
</template>

<style scoped></style>
