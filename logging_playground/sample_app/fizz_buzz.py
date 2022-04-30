from typing import Union
import logging

# Logger自体の設定は、mainモジュールでパッケージ名のLoggerを対象に反映済み
# よって、モジュール上では特に設定することなく利用できる
logger = logging.getLogger(__name__)

DIVISOR_FIZZ = 3
DIVISOR_BUZZ = 5
DIVISOR_FIZZBUZZ = 15

FIZZBUZZ_VALUE_MIN = 1
FIZZBUZZ_VALUE_MAX = 100


class InvalidFizzBuzzValue(Exception):
    """ FizzBuzzにおいて無効な値が渡されたことを表現 
        例外が送出されたときのログ出力を検証するために利用
    """


def get_fizz_buzz_message(value: int) -> Union[str, int]:
    """
    入力の数値と対応するFizz Buzzメッセージを取得

    :param value: 入力値
    :return: FizzBuzzメッセージまたは入力値
    """
    logger.info('call FizzBuzz')
    logger.debug('value: %s', value)

    if value < FIZZBUZZ_VALUE_MIN or value > FIZZBUZZ_VALUE_MAX:
        raise InvalidFizzBuzzValue('無効な値が渡されました')

    if value % DIVISOR_FIZZBUZZ == 0:
        logger.debug('return FizzBuzz')
        return 'FizzBuzz!!'

    if value % DIVISOR_FIZZ == 0:
        logger.debug('return Fizz')
        return 'Fizz'

    if value % DIVISOR_BUZZ == 0:
        logger.debug('return Buzz')
        return 'Buzz'

    logger.debug('return value: %s', value)
    return value
