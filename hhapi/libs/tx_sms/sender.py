from qcloudsms_py import SmsSingleSender
from . import settings
from utils.logging import get_logger
import random

logger = get_logger("django")


def generator_code():
    """
    4位数字的字符串
    :return:
    """
    s_code = ''
    for i in range(4):
        s_code += str(random.randint(0, 9))
    return s_code


def sender_sms(phone, code):
    """
    这个是对腾讯短信进行了封装
    :param phone:
    :param code:
    :return:
    """

    ssender = SmsSingleSender(settings.appid, settings.appkey)
    try:
        result = ssender.send_with_param(86, phone,
                                         settings.template_id, params=[code, settings.cache_time],
                                         sign=settings.sms_sign, extend="", ext="")
        if result.get('result') == 0:
            return True
        return False
    except Exception as e:
        logger.error('发送%s,报错信息:%s' % (phone, str(e)))
