<script setup>
import { onMounted, reactive, ref, computed } from "vue";

import Header from "../components/MainHeader.vue";
import CarouselWithArrows from "../components/CarouselWithArrows.vue";
import EventsCard from "../components/EventsCard.vue";

const headerDivButtonText = ref("");
const headerDivButtonLink = ref("");

const allLotery = reactive([
  {
    id: 0,
    type: "big",
    name: "Домашняя лотерея",
    image: "/main-page/example-big-draw-1.png",
    tickets: [
      {
        id: 0,
        user: {
          email: "user@example.com",
          username: "tYaEFoFZ8oxFq7B7aG5UuZAG9abSUCIy9OjEe_",
          name: "string",
          surname: "string",
          patronymic: "string",
          id: 0,
          is_active: true,
          created_at: "2025-11-25T11:13:37.856Z",
          updated_at: "2025-11-25T11:13:37.856Z",
        },
        lottery_id: 0,
        numbers: ["string"],
      },
    ],
    start_at: "2026-11-25T11:13:37.856Z",
    ended_at: "2026-11-25T11:13:37.856Z",
    numbers: [0],
  },
  {
    id: 1,
    type: "big",
    name: "Лотерея лотерея",
    image: "/main-page/example-big-draw-2.png",
    tickets: [
      {
        id: 0,
        user: {
          email: "user@example.com",
          username: "tYaEFoFZ8oxFq7B7aG5UuZAG9abSUCIy9OjEe_",
          name: "string",
          surname: "string",
          patronymic: "string",
          id: 0,
          is_active: true,
          created_at: "2025-11-25T11:13:37.856Z",
          updated_at: "2025-11-25T11:13:37.856Z",
        },
        lottery_id: 0,
        numbers: ["string"],
      },
    ],
    start_at: "2026-11-25T11:13:37.856Z",
    ended_at: "2026-11-25T11:13:37.856Z",
    numbers: [0],
  },
    {
    id: 2,
    type: "small",
    name: "Лотерея лотерея 1",
    image: "/main-page/example-small-card-draw-1.png",
    tickets: [
      {
        id: 0,
        user: {
          email: "user@example.com",
          username: "tYaEFoFZ8oxFq7B7aG5UuZAG9abSUCIy9OjEe_",
          name: "string",
          surname: "string",
          patronymic: "string",
          id: 0,
          is_active: true,
          created_at: "2025-11-25T11:13:37.856Z",
          updated_at: "2025-11-25T11:13:37.856Z",
        },
        lottery_id: 0,
        numbers: ["string"],
      },
    ],
    start_at: "2026-11-25T11:13:37.856Z",
    ended_at: "2026-11-25T11:13:37.856Z",
    numbers: [0],
  },
    {
    id: 3,
    type: "small",
    name: "Лотерея лотерея 2",
    image: "/main-page/example-small-card-draw-2.png",
    tickets: [
      {
        id: 0,
        user: {
          email: "user@example.com",
          username: "tYaEFoFZ8oxFq7B7aG5UuZAG9abSUCIy9OjEe_",
          name: "string",
          surname: "string",
          patronymic: "string",
          id: 0,
          is_active: true,
          created_at: "2025-11-25T11:13:37.856Z",
          updated_at: "2025-11-25T11:13:37.856Z",
        },
        lottery_id: 0,
        numbers: ["string"],
      },
    ],
    start_at: "2025-11-25T11:13:37.856Z",
    ended_at: "2025-11-25T11:13:37.856Z",
    numbers: [0],
  },
]);

const bigActualLotery = computed(() =>
  allLotery.filter(
    (item) => item.type === "big" && new Date(item.start_at) > new Date()
  )
);
const smallActualLotery = computed(() =>
  allLotery.filter(
    (item) => item.type === "small" && new Date(item.start_at) > new Date()
  )
);
const smallEndedLotery = computed(() =>
  allLotery.filter(
    (item) => item.type === "small" && new Date(item.ended_at) < new Date()
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

onMounted(changeHeaderDivButton);
</script>

<template>
  <Header
    :headerDivButtonText="headerDivButtonText"
    :headerDivButtonLink="headerDivButtonLink"
  />
  <CarouselWithArrows :lotteries="bigActualLotery" />
  <EventsCard title="Актуальные события" :lotteries="smallActualLotery" />
  <EventsCard title="Прошедшие события" :lotteries="smallEndedLotery" />
</template>
