from aiohttp import web  # 导入aiohttp的web模块


async def hello(request):  # 定义异步的处理函数hello，参数为请求
    return web.Response(
        text="Hello, world",
        headers={
            "Access-Control-Allow-Origin": "*",
        },
    )  # 返回一个web响应，响应体为"Hello, world"
