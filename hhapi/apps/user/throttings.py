from rest_framework.throttling import SimpleRateThrottle


class SMSSimpleRateThrottle(SimpleRateThrottle):
    """
    这是发送短信频率限制类
    """
    scope = 'sms'

    def get_cache_key(self, request, view):
        telephone = request.query_params.get('telephone')

        return self.cache_format % {
            'scope': self.scope,
            'ident': telephone
        }
