from .hello import hello  # 从当前目录下的hello模块导入hello函数


def setup_routes(app):  # 定义设置路由的函数，参数为web应用
    app.router.add_get(
        "/", hello
    )  # 在web应用的路由上添加一个GET请求的路由，路径为"/"，处理函数为hello
