<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const msg = ref('');

onMounted(async () => {
    try {
        const response = await axios.get('http://localhost:9000/');
        msg.value = response.data;
    } catch (error) {
        console.error(error);
    }
});
</script>

<template>
    <div class="hello">
        <h1>{{ msg }}</h1>
    </div>
</template>
