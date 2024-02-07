<script setup>
import { ref } from 'vue'; // 从vue库中导入ref和withProps函数
import axios from 'axios'; // 导入axios库，用于发送HTTP请求

const props = defineProps({
    options: Array,
});

const inputText = ref(''); // 创建一个响应式引用inputText，初始值为空字符串
const selectedOption = ref(''); // 创建一个响应式引用selectedOption，初始值为空字符串

const sendRequest = async () => { // 定义一个异步函数sendRequest
    try {
        const response = await axios.post('http://localhost:9000/string', { // 使用axios发送一个POST请求到指定的URL，并等待响应
            mod: parseInt(selectedOption.value) , // 将inputText的值作为请求体的一部分发送
            s: inputText.value, // 将selectedOption的值作为请求体的一部分发送
        });
        console.log(response.data); // 打印响应的数据
    } catch (error) {
        console.error(error); // 如果请求失败，打印错误信息
    }
};
</script>

<template>
    <div>
        <select v-model="selectedOption"> <!-- 创建一个选择器，使用v-model指令将其值绑定到selectedOption变量 -->
            <option v-for="option in options" :key="option.label" :value="option.value">
                <!-- 使用v-for指令遍历options数组，为每个选项创建一个<option>元素 -->
                {{ option.label }} <!-- 使用插值表达式显示选项的文本 -->
            </option>
        </select>
        <input v-model="inputText" type="text" placeholder="请输入文本"> <!-- 创建一个输入框，使用v-model指令将其值绑定到inputText变量 -->
        <button @click="sendRequest">发送请求</button> <!-- 创建一个按钮，使用@click指令将其点击事件绑定到sendRequest函数 -->
    </div>
</template>
