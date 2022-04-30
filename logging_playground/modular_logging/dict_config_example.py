import logging
import logging.config

config_dict = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'filename': './dict_config_example_log.txt'
        }
    },
    'loggers': {
        'simpleExample': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': 'no'
        }
    }
}

# 内部的には設定値をもとにHandlerクラスのインスタンスをつくったり、Logger.getLogger()を呼び出している
# つまり、Loggerでログを出力できる環境を設定値をもとに構築している
logging.config.dictConfig(config_dict)
logger = logging.getLogger('simpleExample')
logger.debug('debug log')
logger.info('info log')
