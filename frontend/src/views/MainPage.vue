<script setup>
import Header from "../components/Header.vue";
import CarouselWithArrows from "../components/CarouselWithArrows.vue"
import EventsCard from "../components/EventsCard.vue"
</script>

<template>
    <Header headerDivButtonText="Вход и регистрация" />
    <CarouselWithArrows />
    <EventsCard title="Актуальные события" />
    <EventsCard title="Прошедшие события" />
</template>
