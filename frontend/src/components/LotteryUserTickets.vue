<script setup>
import { ref } from "vue";
import Ticket from "../components/Ticket.vue";

const props = defineProps({
  userTickets: Array,
  lottery_id: Number,
  start_at: Date
});

const isSold = ref(false);

const buyTicket = async () => {
  if (new Date() > new Date(props.start_at)) isSold.value = true;
  const access_token = localStorage.getItem("access_token");
  const response = await fetch("http://localhost:8000/api/tickets", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${access_token}`,
    },
    body: JSON.stringify({ lottery_id: props.lottery_id }),
  });
};
</script>

<template>
  <div class="main-user-tickets-div">
    <p class="tickets-header">Ваши билеты</p>
    <button @click="buyTicket">Купить билет</button>
    <p class="error-p" v-if="isSold">Время покупки истекло!</p>
    <div class="tickets-div">
      <Ticket v-for="ticket in userTickets" :key="ticket.id" :ticket="ticket" />
    </div>
  </div>
</template>

<style scoped>
.main-user-tickets-div {
  display: flex;
  flex-direction: column;
  margin: 65px 20px 65px 20px;
  gap: 10px;
}

.tickets-header {
  font-size: 2em;
  font-weight: bold;
}

button {
  width: max-content;
  background-color: #b25dfd;
  color: white;
  font-size: 1.5em;
  border: 0px;
  border-radius: 15px;
  padding: 7px 30px 7px 30px;
  cursor: pointer;
  text-decoration: none;
  text-align: center;
}

.tickets-div {
  width: max-content;
  gap: 15px;
  margin: 15px 0px 15px 0px;
  padding: 0px 0px 0px 15px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.error-p {
  color: red;
  font-weight: bold;
}
</style>
