<script setup>
import { onMounted, reactive } from "vue";

import Ticket from "../components/Ticket.vue";

const props = defineProps({
  lottery: Object,
});

</script>

<template>
  <div class="lottery-div">
    <p class="lottery-header">{{ lottery.name }}</p>
    <div class="tickets-div">
      <Ticket
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

@media (max-width: 700px) {
  ::v-deep .field-div {
    grid-template-columns: repeat(9, 40px);
    grid-template-rows: repeat(3, 40px);
  }
}

@media (max-width: 500px) {
  ::v-deep .field-div {
    grid-template-columns: repeat(9, 35px);
    grid-template-rows: repeat(3, 35px);
  }
}

@media (max-width: 400px) {
  ::v-deep .cell-div {
    font-size: 0.7em;
  }

  ::v-deep .status {
    font-size: 0.7em;
    width: 120px;
  }

  ::v-deep .field-div {
    grid-template-columns: repeat(9, 25px);
    grid-template-rows: repeat(3, 25px);
  }

  ::v-deep .ticket-name-p {
    font-size: 0.8em;
  }
}
</style>
