import logging

# デフォルトの設定ではログレベルwarning以上が出力される
# 内部的にはRootLoggerを利用して標準出力へメッセージを出力
logging.debug('出力されません')
logging.warning('出力されます')
# メッセージ: `WARNING:root:出力されます`
