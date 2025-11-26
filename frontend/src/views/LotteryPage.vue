<script setup>
import { onMounted, ref, reactive } from "vue";
import { useRouter } from "vue-router";

import Header from "../components/HeaderWithButton.vue";
import GameTimer from "../components/GameTimer.vue";
import NumbersOfLottery from "../components/NumbersOfLottery.vue";
import WinnersLottery from "../components/WinnersLottery.vue";
import LotteryUserTickets from "../components/LotteryUserTickets.vue";

const router = useRouter();
const backendUrl = "http://localhost:8000";
const lottery = reactive({
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
        id: 2,
        is_active: true,
        created_at: "2025-11-24T12:21:52.924Z",
        updated_at: "2025-11-24T12:21:52.924Z",
      },
      status: "win",
      lottery_id: 0,
      numbers: [
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
      ],
    },
    {
      id: 1432,
      user: {
        email: "user@example.com",
        username: "Wu_oR5yss6xcgpnzP5Kr1Wh9Vyq2Fg1KCFUB6k5bMBL4BdEe0",
        name: "string",
        surname: "string",
        patronymic: "string",
        id: 1,
        is_active: true,
        created_at: "2025-11-24T12:21:52.924Z",
        updated_at: "2025-11-24T12:21:52.924Z",
      },
      status: "not played",
      lottery_id: 0,
      numbers: [
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
      ],
    },
    {
      id: 1432,
      user: {
        email: "user@example.com",
        username: "Wu_oR5yss6xcgpnzP5Kr1Wh9Vyq2Fg1KCFUB6k5bMBL4BdEe0",
        name: "string",
        surname: "string",
        patronymic: "string",
        id: 3,
        is_active: true,
        created_at: "2025-11-24T12:21:52.924Z",
        updated_at: "2025-11-24T12:21:52.924Z",
      },
      status: "win",
      lottery_id: 0,
      numbers: [
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
        4,
        null,
        27,
        null,
        null,
        null,
        62,
        78,
        90,
      ],
    },
  ],
  start_at: "2025-11-24T12:21:52.924Z",
  ended_at: "2025-11-24T12:21:52.924Z",
  numbers: [
    0, 1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 8, 9, 10, 1, 2, 3, 4, 5,
  ],
});
const userTickets = reactive([
  {
    id: 1433,
    user: {
      email: "user@example.com",
      username: "Wu_oR5yss6xcgpnzP5Kr1Wh9Vyq2Fg1KCFUB6k5bMBL4BdEe0",
      name: "string",
      surname: "string",
      patronymic: "string",
      id: 2,
      is_active: true,
      created_at: "2025-11-24T12:21:52.924Z",
      updated_at: "2025-11-24T12:21:52.924Z",
    },
    status: "win",
    lottery_id: 0,
    numbers: [
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
    ],
  },
  {
    id: 1432,
    user: {
      email: "user@example.com",
      username: "Wu_oR5yss6xcgpnzP5Kr1Wh9Vyq2Fg1KCFUB6k5bMBL4BdEe0",
      name: "string",
      surname: "string",
      patronymic: "string",
      id: 1,
      is_active: true,
      created_at: "2025-11-24T12:21:52.924Z",
      updated_at: "2025-11-24T12:21:52.924Z",
    },
    status: "not played",
    lottery_id: 0,
    numbers: [
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
      4,
      null,
      27,
      null,
      null,
      null,
      62,
      78,
      90,
    ],
  },
]);

// onMounted(async () => {
//     const response = await fetch(backendUrl + "/api/lottery/" + router.params.id, {
//         method: "POST",
//         headers: {
//             Authorization: `Bearer ${localStorage.getItem("access_token")}`
//         }
//     });
//     lottery = await response.json();
// });

const headerDivButtonText = ref("На главную");
const headerDivButtonLink = ref("/");
</script>

<template>
  <Header
    :headerDivButtonText="headerDivButtonText"
    :headerDivButtonLink="headerDivButtonLink"
  />
  <GameTimer :lottery="lottery" />
  <NumbersOfLottery :lottery="lottery" />
  <WinnersLottery :lottery="lottery" />
  <LotteryUserTickets :userTickets="userTickets" />
</template>
<style scoped>
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
