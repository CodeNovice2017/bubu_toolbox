from aiohttp import web  # 导入aiohttp的web模块
from app.common import common_response


async def string_options(request: web.Request):
    filters = [
        common_response.Filter("1", "双引号转单引号"),
        common_response.Filter("2", "双引号转无引号"),
        common_response.Filter("3", "双引号转无引号(前拼and后拼=)"),
        common_response.Filter("4", "去除首尾空格"),
        common_response.Filter("5", "去除全部空格"),
    ]
    filters = list(map(lambda filter: filter.to_dict(), filters))
    return web.json_response(filters)
