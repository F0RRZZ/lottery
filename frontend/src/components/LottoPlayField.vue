<script setup>

defineProps({
    numbers : Array
});

</script>

<template>
    <div class="field-div">
        <div class="cell-div" v-for="number in numbers" :key="number" v-text="number"></div>
    </div>
</template>

<style scoped>
.field-div {
    display: grid;
    grid-template-columns: repeat(9, 60px);
    grid-template-rows: repeat(3, 60px);
}

.cell-div {
    display: flex;
    align-items: center;
    justify-content: center;
    border: solid black 2px;
    margin: 2px;
    padding: 10px;
}
</style>