<script setup>
const props = defineProps({
  lottery: Object,
});
</script>

<template>
  <div class="main-numbers-div">
    <p class="numbers-header">Выпавшие числа:</p>
    <div class="numbers-div" v-if="lottery.numbers.length != 0">
      <p class="number" v-for="number in lottery.numbers" :key="number">
        {{ number }}
      </p>
    </div>
    <p class="without-numbers-p" v-else>Чисел ещё нет</p>
  </div>
</template>

<style scoped>
.main-numbers-div {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin: 65px 20px 65px 20px;
}

.numbers-header {
  font-size: 2em;
  font-weight: bold;
}

.without-numbers-p {
  font-size: 1.5em;
  font-weight: bold;
  color: #E4B808;
}

.numbers-div {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  border-radius: 60px;
  gap: 10px;
  overflow-x: auto;
  box-shadow: 0px 0px 25px grey;
  padding: 15px 10px 5px 10px;
  scroll-margin: 100px;
}

.number {
  flex: 0 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80px;
  height: 80px;
  margin: 5px;
  font-size: 2.5em;
  border-radius: 50%;
  border: #e4b808 solid 4px;
}
</style>
