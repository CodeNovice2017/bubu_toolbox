<script setup>
import { ref, onMounted, defineEmits } from 'vue'; // 从vue库中导入ref和onMounted函数
import axios from 'axios'; // 导入axios库，用于发送HTTP请求

const emit = defineEmits(['update:modelValue']);
const options = ref([]); // 创建一个响应式引用options，初始值为一个空数组

onMounted(async () => { // 定义一个在组件挂载后执行的函数
    try {
        const response = await axios.get('http://localhost:9000/string/options'); // 发送一个GET请求到指定的URL，并等待响应
        options.value = response.data; // 将options的值更新为响应的数据
        emit('update:options', options.value); // 触发一个自定义事件update:options，并传递options的值
    } catch (error) {
        console.error(error); // 如果请求失败，打印错误信息
    }
});
</script>

<template>
    <div>
        <!-- 这里可以添加其他的HTML和Vue代码 -->
    </div>
</template>
