<script setup>
import { onMounted, ref } from "vue"

import Header from "../components/Header.vue";
import CarouselWithArrows from "../components/CarouselWithArrows.vue"
import EventsCard from "../components/EventsCard.vue"

const headerDivButtonText = ref('');
const headerDivButtonLink = ref('');

const changeHeaderDivButton = () => {
    if(!localStorage.getItem('access_token')) {
        headerDivButtonText.value = 'Вход и регистрация'
        headerDivButtonLink.value = '/login'
        return
    }
};

onMounted(changeHeaderDivButton);

</script>

<template>
    <Header :headerDivButtonText="headerDivButtonText" :headerDivButtonLink="headerDivButtonLink" />
    <CarouselWithArrows />
    <EventsCard title="Актуальные события" :cardsDraw="[{ id: 0, image: '/main-page/example-small-card-draw-1.png' }, { id: 1, image: '/main-page/example-small-card-draw-2.png' }]" />
    <EventsCard title="Прошедшие события" :cardsDraw="[{ id: 0, image: '/main-page/example-small-card-draw-1.png' }, { id: 1, image: '/main-page/example-small-card-draw-2.png'}, { id: 0, image: '/main-page/example-small-card-draw-1.png' }, { id: 1, image: '/main-page/example-small-card-draw-2.png' },{ id: 0, image: '/main-page/example-small-card-draw-1.png' }, { id: 1, image: '/main-page/example-small-card-draw-2.png' }]" />
</template>
