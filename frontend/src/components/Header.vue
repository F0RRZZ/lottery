<script setup>
import { defineProps } from "vue";

defineProps({
    headerDivButtonText: String
})
</script>

<template>
    <div class="header-div">
        <p class="header-p-logo">лотерея</p>
        <button class="header-div-button">{{headerDivButtonText}}</button>
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
    background-color: #B25DFD;
    color: white;
    font-size: 1.5em;
    border: 0px;
    border-radius: 15px;
    padding: 7px 30px 7px 30px;
    cursor: pointer;
}
</style>
