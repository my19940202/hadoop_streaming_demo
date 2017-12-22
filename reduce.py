#!/usr/local/bin/python 
"""
File: mapper.py
Author: xishengbo
Date: 2015/10/23 16:08:25
"""
import sys

def main():
    show = 0
    arrowClick = 0
    requestImage = 0
    requestFail = 0
    showLayer = 0
    closeLayer = 0
    adPageShow = 0
    requestTimeTotal = 0
    for line in sys.stdin:
        items = line.split('\t')
        if 'actionid=4' in items[1]:
            show += 1
        if "yuetu-arrow_clicked" in items[1]:
            arrowClick += 1
        if 'attach=image_response_time:' in items[1]:
            idx = items[1].find('attach=image_response_time:')
            l = len('attach=image_response_time:')
            str = items[1][idx + l:]
            idx = str.find('&')
            time = int(str[:idx])
            requestTimeTotal += time
            requestImage += 1
        if 'image_do_not_response' in items[1]:
            requestFail += 1
        if 'salon_real_show' in items[1]:
            showLayer += 1
        if 'ad_page_show' in items[1]:
            adPageShow += 1
        if 'yfls-close-btn_clicked' in items[1]:
            closeLayer += 1

    print 'show', show
    print 'arrowClick', arrowClick
    print 'requestImage', requestImage
    print 'requestFail', requestFail
    print 'showLayer', showLayer
    print 'closeLayer', closeLayer
    print 'adPageShow', adPageShow
    if requestImage == 0:
        print 'requestImage is 0'
    else:
        print 'avgTime: %.2f'%(requestTimeTotal / requestImage)
    return None

if __name__ == '__main__':
    main()


