<script setup>
import { onMounted } from "vue";

const props = defineProps({
  numbers: Array,
  dropped_numbers: Array,
});

</script>

<template>
  <div class="field-div">
    <div
      v-for="number in props.numbers"
      :class="{
        'cell-div': true,
        'dropped-cell': props.dropped_numbers.includes(number),
        'not-dropped-cell': !props.dropped_numbers.includes(number),
        'empty-cell': number === null
      }"
      :key="number"
      v-text="number"
    ></div>
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

.dropped-cell {
  color: white;
  background-color: #2ed400;
}

.not-dropped-cell {
  color: white;
  background-color: #ffce0a;
}

.empty-cell {
    color: black;
    background-color: white;
}
</style>
