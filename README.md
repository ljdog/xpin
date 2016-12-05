# xpin
内部统一PIN认证


### app

config 需要配置


    SECRET_KEY = 'tmp_secret_key'

    # flask-sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite')
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask_dpl'

    CLIENT_SECRET = '323'

    PIN_LENGTH = 6
    PIN_MAX_AGE = 300
    PIN_MAX_TRY_TIMES = 5
    PIN_LOG = False

    DING_CORP_ID =
    DING_CORP_SECRET =
    DING_AGENT_ID =

    SEND_CLOUD_API_USER =
    SEND_CLOUD_API_KEY =
    SEND_CLOUD_SENDER =


启动

    // 初始化数据库
    xpin -c config.py syncdb

    // 添加管理员
    xpin -c config.py addadmin admin password

    // 多线程模式启动
    xpin -c config.py runserver --threaded


注意:

    由于强依赖钉钉，务必要保证用户是公司员工，否则验证会失败。
