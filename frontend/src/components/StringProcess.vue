<script setup>
import { ref } from 'vue'; // 从vue库中导入ref函数
import StringOptions from './StringOptions.vue'; // 导入StringOptions组件
import StringInput from './StringInput.vue'; // 导入StringInput组件

const options = ref([]); // 创建一个响应式引用options，初始值为一个空数组

const updateOptions = newOptions => { // 定义一个箭头函数updateOptions，接收一个参数newOptions
    options.value = newOptions; // 将options的值更新为newOptions
};
</script>

<template>
    <div>
        <StringOptions @update:options="updateOptions" /> <!-- 引入StringOptions组件，并监听其update:options事件 -->
        <StringInput :options="options" /> <!-- 引入StringInput组件，并将options作为prop传递给它 -->
    </div>
</template>
