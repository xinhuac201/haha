import re
from rest_framework.exceptions import ValidationError


def verify_mobile_num(mobile_num: str, flag=1) -> bool or Exception:
    """
    通用检测手机号码是否合法,仅仅检测国内
    :return:bool
    """
    pattern = r'^1([358][0-9]|4[579]|66|7[0135678]|9[89])[0-9]{8}$'
    if not flag:
        if re.match(pattern, mobile_num):
            return True
    if flag:
        if not re.match(pattern, mobile_num):
            raise ValidationError('手机号不合法')


def verify_email(username: str) -> bool:
    """
    通用邮箱检测
    :param username:
    :return:
    """
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.match(pattern, username):
        return True
