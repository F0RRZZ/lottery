<script setup>
import { onMounted, ref, reactive, onUnmounted } from "vue";
import { useRoute } from "vue-router";

import Header from "../components/HeaderWithButton.vue";
import GameTimer from "../components/GameTimer.vue";
import NumbersOfLottery from "../components/NumbersOfLottery.vue";
import WinnersLottery from "../components/WinnersLottery.vue";
import LotteryUserTickets from "../components/LotteryUserTickets.vue";

const router = useRoute();
const backendUrl = "http://localhost:8000";
const lottery = reactive({});
const userTickets = ref([]);
const user_info = reactive({});

let timerToUpdateLotteries;

const props = defineProps({
  id: String,
});

const getUserInfo = async () => {
  const access_token = localStorage.getItem("access_token");
  const response = await fetch("http://localhost:8000/api/auth/me", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${access_token}`,
    },
  });
  const data = await response.json();
  Object.assign(user_info, data);
};

const getLottery = async () => {
  const response = await fetch(`${backendUrl}/api/lottery/${props.id}`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${localStorage.getItem("access_token")}`,
    },
  });
  let data = await response.json();
  Object.assign(lottery, data);

  userTickets.value = lottery.tickets.filter(
    (ticket) => ticket.user.id === user_info.id
  );

  userTickets.value = userTickets.value.map((ticket) => ({
    ...ticket,
    dropped_numbers: lottery.numbers,
  }));
};

onMounted(async () => {
  await getUserInfo();
  await getLottery();
  timerToUpdateLotteries = setInterval(getLottery, 1000);
});

onUnmounted(() => {
    if(timerToUpdateLotteries) {
        clearInterval(timerToUpdateLotteries);
    }
});

const headerDivButtonText = ref("Мой профиль");
const headerDivButtonLink = ref("/user-profile");
</script>

<template>
  <Header
    :headerDivButtonText="headerDivButtonText"
    :headerDivButtonLink="headerDivButtonLink"
  />
  <p class="name-of-lottery-p">{{ lottery.name }}</p>
  <GameTimer v-if="Object.keys(lottery).length !== 0" :lottery="lottery" />
  <NumbersOfLottery
    v-if="Object.keys(lottery).length !== 0"
    :lottery="lottery"
  />
  <WinnersLottery v-if="Object.keys(lottery).length !== 0" :lottery="lottery" />
  <LotteryUserTickets
    :userTickets="userTickets"
    :lottery_id="lottery.id"
    :start_at="lottery.start_at"
    :dropped_numbers="lottery.numbers"
  />
</template>
<style scoped>
.name-of-lottery-p {
  margin: 40px 20px 65px 20px;
  font-size: 2em;
  font-weight: bold;
}

::v-deep .tickets-div {
  padding: 0px;
}

@media (max-width: 1025px) {
  ::v-deep .number {
    width: 60px;
    height: 60px;
  }

  ::v-deep .numbers-div {
    padding: 10px 10px 3px 10px;
  }
}

@media (max-width: 700px) {
  name-of-lottery-p,
  ::v-deep .p-header,
  ::v-deep .winners-header,
  ::v-deep .numbers-header,
  ::v-deep .tickets-header {
    font-size: 1.6em;
  }

  ::v-deep .p-time,
  ::v-deep .numbers-of-winners {
    font-size: 4.6em;
  }
}

@media (max-width: 600px) {
  ::v-deep .field-div {
    grid-template-columns: repeat(9, 50px);
    grid-template-rows: repeat(3, 50px);
  }

  name-of-lottery-p,
  ::v-deep .p-header,
  ::v-deep .winners-header,
  ::v-deep .numbers-header,
  ::v-deep .tickets-header {
    font-size: 1.5em;
  }

  ::v-deep .p-time,
  ::v-deep .numbers-of-winners {
    font-size: 4.2em;
  }

  ::v-deep button {
    border-radius: 13px;
    font-size: 1.2em;
  }
}

@media (max-width: 500px) {
  ::v-deep .field-div {
    grid-template-columns: repeat(9, 40px);
    grid-template-rows: repeat(3, 40px);
  }

  ::v-deep .number {
    width: 45px;
    height: 45px;
    font-size: 1.8em;
  }

  ::v-deep .numbers-div {
    padding: 6px 10px 0px 10px;
  }

  name-of-lottery-p,
  ::v-deep .p-header,
  ::v-deep .winners-header,
  ::v-deep .numbers-header,
  ::v-deep .tickets-header {
    font-size: 1.3em;
  }

  ::v-deep .p-time,
  ::v-deep .numbers-of-winners {
    font-size: 3.5em;
  }

  ::v-deep button {
    border-radius: 11px;
    font-size: 1em;
  }
}

@media (max-width: 410px) {
  ::v-deep .cell-div {
    font-size: 0.7em;
  }

  ::v-deep .status {
    font-size: 0.7em;
    width: 120px;
  }

  ::v-deep .field-div {
    grid-template-columns: repeat(9, 30px);
    grid-template-rows: repeat(3, 30px);
  }

  ::v-deep .ticket-name-p {
    font-size: 0.8em;
  }
}
</style>
