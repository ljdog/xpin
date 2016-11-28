# -*- coding: utf-8 -*-

NAME = 'xpin'

# URL 定义

# 生成并发送PIN码
URL_PIN_CREATE = '/pin/create'

# 验证PIN码
URL_PIN_VERIFY = '/pin/verify'


# 返回码定义

# 内部错误
RET_INTERNAL = -1000

# 用户无效
RET_USER_INVALID = 1000

# PIN无效
RET_USER_PIN_VALID = 2000


# 默认app配置
CONFIG = dict(
    # flask-sqlalchemy
    SQLALCHEMY_ECHO=False,

    # admin_user
    SESSION_KEY_ADMIN_USERNAME='admin_username',
)
