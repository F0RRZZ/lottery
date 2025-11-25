<script setup>
import { reactive, ref } from "vue";

import UserLotteriesListLottery from "../components/UserLotteriesListLottery.vue";

const lotteries = reactive([
  {
    id: 0,
    name: "Лоттерея №52",
    tickets: [
      {
        id: 1432,
        user: {
          email: "user@example.com",
          username: "Wu_oR5yss6xcgpnzP5Kr1Wh9Vyq2Fg1KCFUB6k5bMBL4BdEe0",
          name: "string",
          surname: "string",
          patronymic: "string",
          id: 0,
          is_active: true,
          created_at: "2025-11-24T12:21:52.924Z",
          updated_at: "2025-11-24T12:21:52.924Z",
        },
        status: "not played",
        lottery_id: 0,
        numbers: [4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90],
      },
            {
        id: 1432,
        user: {
          email: "user@example.com",
          username: "Wu_oR5yss6xcgpnzP5Kr1Wh9Vyq2Fg1KCFUB6k5bMBL4BdEe0",
          name: "string",
          surname: "string",
          patronymic: "string",
          id: 0,
          is_active: true,
          created_at: "2025-11-24T12:21:52.924Z",
          updated_at: "2025-11-24T12:21:52.924Z",
        },
        status: "win",
        lottery_id: 0,
        numbers: [4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90],
      },
            {
        id: 1432,
        user: {
          email: "user@example.com",
          username: "Wu_oR5yss6xcgpnzP5Kr1Wh9Vyq2Fg1KCFUB6k5bMBL4BdEe0",
          name: "string",
          surname: "string",
          patronymic: "string",
          id: 0,
          is_active: true,
          created_at: "2025-11-24T12:21:52.924Z",
          updated_at: "2025-11-24T12:21:52.924Z",
        },
        status: "lose",
        lottery_id: 0,
        numbers: [4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90, 4, null, 27, null, null, null, 62, 78, 90],
      },
    ],
    start_at: "2025-11-24T12:21:52.924Z",
    ended_at: "2025-11-24T12:21:52.924Z",
    numbers: [0],
  }
]);
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
  border-left: 5px solid black;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}
</style>
