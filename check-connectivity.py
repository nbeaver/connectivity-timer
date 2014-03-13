#!/usr/bin/env python2.7
# http://docs.python.org/2/library/urllib2.html#urllib2.urlopen
import urllib2
# http://docs.python.org/2/library/time.html#time.sleep
import time
url = 'http://www.python.org'
loop_time = 1 # seconds
while True:
    try:
        f = urllib2.urlopen(url, data=None, timeout=0.5)
    except urllib2.URLError:
        print "Cannot resolve url",url
        pass
    else:
        print "Successfully resolved url", url
    finally:
        time.sleep(loop_time)
