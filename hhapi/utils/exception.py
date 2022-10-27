from rest_framework.views import exception_handler as drf_exception_handler
from utils.response import APIResponse
from rest_framework import status
from utils.logging import get_logger

logger = get_logger('django')


def exception_handler(exc, context):
    """
    自定义全局异常
    :param exc: 异常信息
    :param context:  # 这个是桥梁，可以确定是哪个视图报错，更准确的查找bug
    :return:
    """

    response = drf_exception_handler(exc, context)
    if response is None:
        # 记录服务器异常
        logger.critical('view是:%s,错误是%s' % (context['view'].__class__.__name__, str(exc)))
        print(context['view'].__class__.__name__)  # 这个是视图出错的名字
        response = APIResponse(msg='数据格式不对，请重新尝试', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response

