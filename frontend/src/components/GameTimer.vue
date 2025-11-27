<script setup>
import { onMounted, ref } from "vue";

const props = defineProps({
  lottery: Object,
});

const gameStatus = ref("");
const timeToShow = ref("");

const dateToFormatDate = (unFormatDate) => {
  return unFormatDate.replace(
    /(\d+)-(\d+)-(\d+)T(\d+):(\d+):(\d+)\.(\d+)/,
    (_, y, m, d, h, min) => `${d}.${m}.${y} ${h}:${min}`
  );
};

let timerToUpdateTime = null;

onMounted(() => {
  timerToUpdateTime = setInterval(() => {
    if (props.lottery.start_at > new Date()) {
      gameStatus.value = "not_started";
      timeToShow.value = dateToFormatDate(props.lottery.start_at);
    } else if (
      props.lottery.start_at <= new Date() &&
      props.lottery.ended_at === null
    ) {
      gameStatus.value = "game_on";
      timeToShow.value = dateToFormatDate(props.lottery.start_at);
    } else {
      gameStatus.value = "game_end";
      timeToShow.value = dateToFormatDate(props.lottery.ended_at);
    }
  });
});
</script>

<template>
  <div class="main-timer">
    <div v-if="gameStatus === 'not_started'" class="not-started-game-div">
      <p class="p-header">Игра начнётся в</p>
      <p class="p-time">{{ timeToShow }}</p>
    </div>
    <div v-else-if="gameStatus === 'game_on'" class="game-on-div">
      <p class="p-header">Игра идёт! Игра началась в:</p>
      <p class="p-time">{{ timeToShow }}</p>
    </div>
    <div v-else class="game-end-div">
      <p class="p-header">Игра закончилась! Конец игры:</p>
      <p class="p-time">{{ timeToShow }}</p>
    </div>
  </div>
</template>

<style scoped>
.main-timer {
  margin: 65px 20px 65px 20px;
}

.not-started-game-div,
.game-on-div,
.game-end-div {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.p-header {
  font-size: 2em;
  font-weight: bold;
}

.p-time {
  font-size: 5em;
  font-weight: bold;
}
</style>
