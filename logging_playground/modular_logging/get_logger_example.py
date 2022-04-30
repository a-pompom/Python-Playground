import logging

# name引数をもとにLoggerクラスのインスタンスを生成
# 生成されたインスタンスはManagerクラスにnameをキーとした辞書で保持されているので、
# 同一のname引数からは同一のLoggerクラスのインスタンスが得られる
print(__name__)
logger = logging.getLogger(__name__)
logger.warning('from logger message')
