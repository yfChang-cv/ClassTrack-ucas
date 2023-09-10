# -*- coding: utf-8 -*-
filename = '课表.ics'


def trans_file_encoding(file_name=filename):
    with open(filename, 'r', encoding='gbk') as f:
        content = f.read()
        with open(filename, 'w', encoding='utf8') as f:
            f.write(content)
