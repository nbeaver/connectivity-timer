#!/usr/bin/env python2.7
# http://docs.python.org/2/library/urllib2.html#urllib2.urlopen
import urllib2
# http://docs.python.org/2/library/time.html#time.sleep
import time
url = 'http://www.python.org'
loop_time = 1 # seconds
time_of_last_success = -1
time_of_last_failure = -1
verbose = False
while True:
    try:
        f = urllib2.urlopen(url, data=None, timeout=0.5)
    except urllib2.URLError:
        time_of_last_failure = time.time()
        if verbose: print "Cannot resolve url",url
        if time_of_last_success != -1 and time_of_last_failure != -1:
            print "Connection has failed for this long:", time_of_last_failure - time_of_last_success
        pass
    else:
        time_of_last_success = time.time()
        if verbose: print "Successfully resolved url", url
        if time_of_last_success != -1 and time_of_last_failure != -1:
            print "Connection has worked for this long:",time_of_last_success - time_of_last_failure
    finally:
        time.sleep(loop_time)
