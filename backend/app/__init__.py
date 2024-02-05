from aiohttp import web  # 导入aiohttp的web模块
from .routes import setup_routes  # 从当前目录下的routes模块导入setup_routes函数


def create_app():  # 定义创建web应用的函数
    app = web.Application()  # 创建web应用
    setup_routes(app)  # 设置web应用的路由
    return app  # 返回web应用
