from aiohttp import web  # 导入aiohttp的web模块
from app.utils import string_utils


async def string_process(request: web.Request):  # 定义异步的处理函数hello，参数为请求
    post_params = await request.json()
    mod = post_params.get("mod", None)  # 获取名为'mod'的参数，如果不存在则返回None
    if mod is not None:
        mod = int(mod)
    else:
        raise ValueError("mod类型不能为空!")
    s = post_params.get("s", None)  # 获取名为's'的参数，如果不存在则返回None
    return web.Response(
        text=process_args(mod, s),
        headers={
            "Access-Control-Allow-Origin": "*",
        },
    )


# 入参解释
# 1. 模式枚举：1-双引号转单引号,2-双引号转无引号,3-双引号转无引号(前拼and后拼=),4-去除首尾空格,5-去除全部空格
# 2. 必须是一个合法的Python字面量，Python的字符串以'',""
def process_args(mod, s):
    if mod == 1:
        return string_utils.convert_double_to_single_quotes(s)
    elif mod == 2:
        return string_utils.convert_double_to_no_quotes(s)
    elif mod == 3:
        return string_utils.convert_double_to_no_quotes_with_and_equal(s)
    elif mod == 4:
        return string_utils.trim(s)
    elif mod == 5:
        return string_utils.remove_spaces_and_newlines(s)
