<script setup>
import { onMounted, reactive, ref, computed } from "vue";

import Header from "../components/MainHeader.vue";
import CarouselWithArrows from "../components/CarouselWithArrows.vue";
import EventsCard from "../components/EventsCard.vue";

const headerDivButtonText = ref("");
const headerDivButtonLink = ref("");

const allLotery = ref([]);

const getLotteries = async () => {
  const response = await fetch("http://localhost:8000/api/lottery", {
    method: "GET",
  });
  allLotery.value = await response.json();
};

const bigActualLotery = computed(() =>
  allLotery.value.filter(
    (item) => item.lottery_type === "big" && new Date(item.start_at) > new Date() && item.numbers.length == 0
  )
);
const smallActualLotery = computed(() =>
  allLotery.value.filter(
    (item) => item.lottery_type === "small" && new Date(item.start_at) > new Date() && item.numbers.length == 0
  )
);
const smallEndedLotery = computed(() =>
  allLotery.value.filter(
    (item) => item.lottery_type === "small" && new Date(item.ended_at) < new Date() && item.numbers.length != 0
  )
);

const changeHeaderDivButton = () => {
  if (!localStorage.getItem("access_token")) {
    headerDivButtonText.value = "Вход и регистрация";
    headerDivButtonLink.value = "/login";
    return;
  } else {
    headerDivButtonText.value = "Мой профиль";
    headerDivButtonLink.value = "/user-profile";
  }
};

onMounted(async () => {
  await getLotteries();
  changeHeaderDivButton();
});
</script>

<template>
  <Header
    :headerDivButtonText="headerDivButtonText"
    :headerDivButtonLink="headerDivButtonLink"
  />
  <CarouselWithArrows v-if="bigActualLotery.length != 0" :lotteries="bigActualLotery" />
  <EventsCard title="Актуальные события" v-if="smallActualLotery.length != 0" :lotteries="smallActualLotery" />
  <EventsCard title="Прошедшие события" v-if="smallEndedLotery.length != 0" :lotteries="smallEndedLotery" />
</template>
