#!/usr/local/bin/python 
"""
File: mapper.py
Author: xishengbo
Date: 2015/10/23 16:08:25
"""
import sys

def main():
    for line in sys.stdin:
        if (line.find('render_id=563') > 0):
            _idx = line.find('actionid=9&attach')
            if (_idx == -1):
                _idx = line.find('actionid=4&attach')
            idx_ = line.find('HTTP/1.1" 200 1')
            # split the log
            str = line[_idx:idx_]
            if str != '':
                print "563\t" + str
    return None

if __name__ == '__main__':
    main()


