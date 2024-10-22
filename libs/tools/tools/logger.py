"""Contain the logger module."""
import logging
from logging import Logger


def set_logger(name: str) -> Logger:
    """Set up logger."""
    # create logger
    log = logging.getLogger(name)

    if not log.handlers:
        log.propagate = False  # disable propagate property
        log.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(formatter)
        log.addHandler(console_handler)
        return log
    return log
