<script setup>
import { ref } from "vue";

import Header from "../components/HeaderWithButton.vue";
import UserInformation from "../components/UserInformation.vue"
import UserLotteriesList from "../components/UserLotteriesList.vue"
import UserLotteriesListVue from "@/components/UserLotteriesList.vue";

const headerDivButtonText = ref('На главную');
const headerDivButtonLink = ref('/')

</script>
    
<template>
    <Header :headerDivButtonText="headerDivButtonText" :headerDivButtonLink="headerDivButtonLink"/>
    <UserInformation />
    <UserLotteriesList />
</template>