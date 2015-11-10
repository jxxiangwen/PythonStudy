#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'jxxia'

UNITS = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
         1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def approximate(size, a_kilobyte_is_1024_bytes=True):
    """
    Convert a file size to human-readable form.
    :param size:the size want to change
    :param a_kilobyte_is_1024_bytes:if True (default), use multiples of 1024,if False, use multiples of 1000
    :return:changed size
    """
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for unit in UNITS[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:0.1f}{1}'.format(size, unit)

    raise ValueError('number too large')


if __name__ == '__main__':
    print(approximate(1000000000000, False))
    print(approximate(1000000000000))


