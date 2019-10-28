import json
import logging
from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin
import traceback

logger = logging.getLogger('log')

# 定义中间件类。 (类名可以任意，但类中的方法名是固定的)
class Middleware(MiddlewareMixin):

    # # 中间件函数。(用到哪个函数写哪个，不需要全写)
    # def process_request(self, request):
    #     '''产生request对象之后，url匹配之前调用'''
    #     print('----process_request----')
    #     # return HttpResponse('process_request')  # 默认放行,不拦截请求。
    #
    # def process_view(self, request, view_func, *view_args, **view_kwargs):
    #     '''url匹配之后，视图函数调用之前调用'''
    #     print('----process_view----')
    #     # view_func: url匹配到的视图函数。
    #     return HttpResponse('process_view')  # return HttpResponse对象,表示拦截,直接执行process_response函数。

    # def process_response(self, request, response):
    #     '''视图函数调用之后，response返回浏览器之前'''
    #     print('----process_response----')
    #     return response  # 一般会返回响应。

    # 如果注册多个process_exception函数，那么函数的执行顺序与注册的顺序相反。(其他中间件函数与注册顺序一致)
    # 中间件函数，用到哪个就写哪个，不需要写所有的中间件函数。
    def process_exception(self, request, exception):
        '''视图函数发生异常时调用'''
        # logger.exception(exception)
        # logger.error(exception)
        logger.error(traceback.format_exc())
        data = {"code": 500, "data": "请求失败", "message": "Failed", "detail": str(exception)}
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
