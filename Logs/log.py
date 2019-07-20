# -*- coding: UTF-8 -*-
import logging
import time
import os
import getcwd


def get_log(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    path = getcwd.get_cwd()
    all_log_path = os.path.join(path, 'Logs/All_Logs/')
    error_log_path = os.path.join(path, 'Logs/Error_Logs/')
    all_log_name = all_log_path + rq + '.log'
    error_log_name = error_log_path + rq + '.log'
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)
    eh = logging.FileHandler(error_log_name)
    eh.setLevel(logging.ERROR)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    error_log_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')
    fh.setFormatter(all_log_formatter)
    ch.setFormatter(all_log_formatter)
    eh.setFormatter(error_log_formatter)
    logger.addHandler(fh)
    logger.addHandler(eh)
    logger.addHandler(ch)
    return logger


log1 = get_log("test")
