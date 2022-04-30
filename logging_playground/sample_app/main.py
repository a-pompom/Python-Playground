from sample_app.fizz_buzz import get_fizz_buzz_message, InvalidFizzBuzzValue
import logging

# パッケージ階層のrootに相当するパッケージ名でLoggerを作成
# こうすることで、各種モジュールは__name__でLoggerをつくると、階層構造でLogRecordが伝播し、
# 1つのLoggerでパッケージのログを管理することができる
logger = logging.getLogger('sample_app')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s: %(message)s')

handler = logging.FileHandler('./log.txt')
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

error_handler = logging.FileHandler('./error_log.txt')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(error_handler)

if __name__ == '__main__':
    try:
        get_fizz_buzz_message(15)
    except InvalidFizzBuzzValue as e:
        logger.exception('Invalid FizzBuzzValue')
