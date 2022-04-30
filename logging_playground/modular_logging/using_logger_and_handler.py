import logging

# ログ出力のインタフェースを提供するLoggerを生成
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 実際のログ出力を制御するHandlerを生成
handler = logging.FileHandler('./using_logger_and_handler_log.txt')
handler.setLevel(logging.INFO)
# LoggerがLogRecordを渡すHandlerを設定
logger.addHandler(handler)

# Loggerを介してログ出力
logger.debug('ファイルに出力されません。')
logger.info('ファイルに出力されます。')
logger.warning('これもファイルに出力されます。')
