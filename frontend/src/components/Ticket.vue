<script setup>
import LottoPlayField from "./LottoPlayField.vue";

defineProps({
  ticket: Object,
});
</script>

<template>
  <div class="header-ticket-div">
    <p class="ticket-name-p">Билет №{{ ticket.id }}</p>
    <p
      :class="
        'status ' +
        (ticket.status === 'win'
          ? 'status-win'
          : ticket.status === 'lose'
          ? 'status-lose'
          : 'status-not-played')
      "
      v-text="
        ticket.status === 'win'
          ? 'Победа'
          : ticket.status === 'lose'
          ? 'Неудача'
          : 'В игре'
      "
    ></p>
  </div>
  <div class="play-fields-div">
    <LottoPlayField class="lotto-play-field" :numbers="ticket.numbers.slice(0, 27)" />
    <LottoPlayField class="lotto-play-field" :numbers="ticket.numbers.slice(27, 55)" />
  </div>
</template>

<style scoped>
.header-ticket-div {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: flex-start;
  gap: 5px;
  font-size: 1.5em;
}

.ticket-name-p {
  font-weight: bold;
  color: black;
}

.status {
  width: 150px;
  text-align: center;
  font-size: 0.9em;
  color: white;
  padding: 2px 25px 2px 25px;
  border-radius: 14px;
}

.status-win {
  background-color: #00ce48;
}

.status-lose {
  background-color: red;
}

.status-not-played {
  background-color: #929292;
}

.play-fields-div {
  display: flex;
  flex-direction: column;
  border: black solid 2px;
  font-size: 1.5em;
  padding: 10px;
  gap: 10px;
}
</style>
