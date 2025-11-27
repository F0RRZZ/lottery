<script setup>
import { ref, reactive, onMounted } from "vue";

import Header from "../components/HeaderWithButton.vue";
import UserInformation from "../components/UserInformation.vue";
import UserLotteriesList from "../components/UserLotteriesList.vue";
import UserLotteriesListVue from "@/components/UserLotteriesList.vue";

const headerDivButtonText = ref("На главную");
const headerDivButtonLink = ref("/");

const user_info = reactive({});

onMounted(async () => {
  const access_token = localStorage.getItem("access_token");
  const response = await fetch("http://localhost:8000/api/auth/me", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${access_token}`,
    },
  });
  const data = await response.json();
  Object.assign(user_info, data);
});
</script>

<template>
  <Header
    :headerDivButtonText="headerDivButtonText"
    :headerDivButtonLink="headerDivButtonLink"
  />
  <UserInformation :user_info="user_info" />
  <UserLotteriesList :user_info="user_info" />
</template>
