<script setup>
import Header from "../components/Header.vue";
import CarouselWithArrows from "../components/CarouselWithArrows.vue"
import EventsCard from "../components/EventsCard.vue"
</script>

<template>
    <Header headerDivButtonText="Вход и регистрация" />
    <CarouselWithArrows />
    <EventsCard title="Актуальные события" :cardsDraw="[{ id: 0, image: '/main-page/example-small-card-draw-1.png' }, { id: 1, image: '/main-page/example-small-card-draw-2.png' }]" />
    <EventsCard title="Прошедшие события" :cardsDraw="[{ id: 0, image: '/main-page/example-small-card-draw-1.png' }, { id: 1, image: '/main-page/example-small-card-draw-2.png'}, { id: 0, image: '/main-page/example-small-card-draw-1.png' }, { id: 1, image: '/main-page/example-small-card-draw-2.png' },{ id: 0, image: '/main-page/example-small-card-draw-1.png' }, { id: 1, image: '/main-page/example-small-card-draw-2.png' }]" />
</template>
