<script setup>
import { onMounted, reactive, ref } from "vue";

import UserLotteriesListLottery from "../components/UserLotteriesListLottery.vue";

const props = defineProps({
  user_info: Object,
});

const lotteries = ref([]);

const getLotteries = async () => {
  const response = await fetch("http://localhost:8000/api/lottery", {
    method: "GET",
  });

  const data = await response.json();
  lotteries.value = data.map((lottery) => {
    return {
      ...lottery,
      tickets: lottery.tickets.filter(
        (ticket) => ticket.user.id === props.user_info.id
      ),
    };
  });
  lotteries.value = lotteries.value.filter(
    (lottery) => lottery.tickets.length > 0
  );
  lotteries.value = lotteries.value.sort(
    (a, b) => new Date(b.start_at) - new Date(a.start_at)
  );
};

onMounted(() => {
  getLotteries();
  setInterval(getLotteries, 1000);
});
</script>

<template>
  <div class="main-div">
    <p class="header-p">Ваши участия:</p>
  </div>
  <div class="lotteries-div">
    <UserLotteriesListLottery
      v-for="lottery in lotteries"
      :key="lottery.id"
      :lottery="lottery"
    />
  </div>
</template>

<style scoped>
.main-div {
  padding: 20px;
}

.header-p {
  font-size: 2em;
  font-weight: bold;
  color: black;
}

.lotteries-div {
  padding: 0px 0px 0px 15px;
  margin-left: 40px;
  gap: 30px;
  border-left: 5px solid black;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

@media (max-width: 500px) {
  .lotteries-div {
    margin-left: 20px;
  }
}
</style>
