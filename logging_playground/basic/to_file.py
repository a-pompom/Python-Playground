import logging

# basicConfig関数はrootロガーに対する設定を適用
logging.basicConfig(filename='./to_file_log.txt', encoding='utf-8', level=logging.DEBUG)

logging.debug('DEBUGも表示されます')
logging.info('これはINFOです')
