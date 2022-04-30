import logging
from sample_library.lib.sample_lib import decorate_text

# ライブラリの親階層を指定することで、伝播されたライブラリのログが得られる
logger = logging.getLogger('sample_library.lib')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('./log.txt')
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

if __name__ == '__main__':
    decorate_text('text')
