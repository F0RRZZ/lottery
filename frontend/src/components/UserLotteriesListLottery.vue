<script setup>
import { reactive } from "vue";

import Ticket from "../components/Ticket.vue";

defineProps({
  lottery: Object,
});
</script>

<template>
  <div class="lottery-div">
    <p class="lottery-header">{{ lottery.name }}</p>
    <div class="tickets-div">
      <Ticket class="ticket"
        v-for="ticket in lottery.tickets"
        :key="ticket.id"
        :ticket="ticket"
      />
    </div>
  </div>
</template>

<style scoped>
.lottery-header {
  font-size: 1.9em;
  font-weight: bold;
  color: black;
}

.tickets-div {
  gap: 15px;
  margin: 15px 0px 15px 0px;
  padding: 0px 0px 0px 15px;
  border-left: 5px solid black;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}
</style>