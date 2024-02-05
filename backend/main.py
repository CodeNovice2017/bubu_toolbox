from aiohttp import web  # 导入aiohttp的web模块
from app import create_app  # 从app模块导入create_app函数

app = create_app()  # 创建web应用
web.run_app(app, host="127.0.0.1", port=9000)  # 运行web应用，监听本地8080端口
