from .hello import hello  # 从当前目录下的hello模块导入hello函数
from .string_process import string_process
from .string_options import string_options
from aiohttp.web import Application


def setup_routes(app: Application):  # 定义设置路由的函数，参数为web应用
    app.router.add_get(
        "/", hello
    )  # 在web应用的路由上添加一个GET请求的路由，路径为"/"，处理函数为hello
    app.router.add_post("/string", string_process)
    app.router.add_get("/string/options", string_options)
