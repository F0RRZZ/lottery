<script setup>
import { computed, ref } from "vue";

const props = defineProps({
  lottery: Object,
});

const numberOfWinners = computed(() =>
  props.lottery.tickets.reduce(
    (acc, item) => (item.status === "win" ? acc + 1 : acc),
    0
  )
);
</script>

<template>
  <div class="main-winners-div">
    <p class="winners-header">Победители:</p>
    <div v-if="numberOfWinners != 0" class="winners-number-list-div">
      <p class="number-of-winners">{{ numberOfWinners }}</p>
      <div class="winners-list-div">
        <p
          class="winner-p"
          v-for="ticket in lottery.tickets.filter((t) => t.status === 'win')"
          :key="ticket.id"
        >
          Пользователь #{{ ticket.user.id }}
        </p>
      </div>
    </div>
    <p class="without-winners-p" v-else>Победители ещё не определены</p>
  </div>
</template>

<style scoped>
.main-winners-div {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin: 65px 20px 65px 20px;
}

.winners-header {
  font-size: 2em;
  font-weight: bold;
}

.number-of-winners {
  font-size: 5em;
  font-weight: bold;
}

.winners-number-list-div {
    display: flex;
    align-items: center;
    gap: 50px;
}

.winners-list-div {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.winner-p {
    font-size: 1.5em;
}

.without-winners-p {
  font-size: 1.5em;
  font-weight: bold;
  color: #E4B808;
}

</style>
