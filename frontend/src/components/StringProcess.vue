<script setup>
// 从vue库中导入ref、onMounted和defineEmits函数
import { ref, onMounted, defineEmits } from 'vue';
// 导入axios库，用于发送HTTP请求
import axios from 'axios';

// 定义一个可以触发的事件列表
const emit = defineEmits(['update:modelValue']);
// 创建一个响应式引用options，初始值为一个空数组
const options = ref([]);
// 创建一个响应式引用inputText，初始值为空字符串
const inputText = ref('');
// 创建一个响应式引用selectedOption，初始值为空字符串
const selectedOption = ref('');

// 定义一个在组件挂载后执行的函数
onMounted(async () => {
    try {
        // 发送一个GET请求到指定的URL，并等待响应
        const response = await axios.get('http://localhost:9000/string/options');
        // 将options的值更新为响应的数据
        options.value = response.data;
        selectedOption.value = options.value[0].value;
        // 触发一个自定义事件update:options，并传递options的值
        emit('update:options', options.value);
    } catch (error) {
        // 如果请求失败，打印错误信息
        console.error(error);
    }
});

// 定义一个异步函数sendRequest
const sendRequest = async () => {
    try {
        // 使用axios发送一个POST请求到指定的URL，并等待响应
        const response = await axios.post('http://localhost:9000/string', {
            // 将selectedOption的值转换为整数，然后作为请求体的一部分发送
            mod: parseInt(selectedOption.value),
            // 将inputText的值作为请求体的一部分发送
            s: inputText.value,
        });
        // 打印响应的数据
        console.log(response.data);
    } catch (error) {
        // 如果请求失败，打印错误信息
        console.error(error);
    }
};
</script>

<template>
    <head>
    </head>
    <js-frame src="https://js.design/site/w/?id=js_jdFixoNmp4S"/>
    <div class="container">
        <div class="select-container">
            <select v-model="selectedOption">
                <option v-for="option in options" :key="option.label" :value="option.value">
                    {{ option.label }}
                </option>
            </select>
        </div>
        <div class="input-container">
            <input v-model="inputText" type="text" placeholder="请输入文本">
        </div>
        <div class="button-container">
            <button @click="sendRequest">发送请求</button>
        </div>
    </div>
</template>
