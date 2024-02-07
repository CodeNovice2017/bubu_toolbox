from aiohttp import web  # 导入aiohttp的web模块
from .routes import setup_routes  # 从当前目录下的routes模块导入setup_routes函数


def create_app():  # 定义创建web应用的函数
    app = web.Application(middlewares=[cors_middleware])
    setup_routes(app)  # 设置web应用的路由
    return app  # 返回web应用


async def cors_middleware(app, handler):
    async def middleware_handler(request):
        if request.method == "OPTIONS":
            return web.Response(
                headers={
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "*",
                    "Access-Control-Allow-Methods": "OPTIONS, GET, POST, PUT, DELETE",
                }
            )
        else:
            response = await handler(request)
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers["Access-Control-Allow-Headers"] = "*"
            response.headers["Access-Control-Allow-Methods"] = (
                "OPTIONS, GET, POST, PUT, DELETE"
            )
            return response

    return middleware_handler
