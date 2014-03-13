#!/usr/bin/env python2.7
# http://docs.python.org/2/library/urllib2.html#urllib2.urlopen
import urllib2
# http://docs.python.org/2/library/time.html#time.sleep
import time
url = 'http://www.python.org'
loop_time = 1 # seconds
time_of_last_success = -1
time_of_last_failure = -1
verbose = True
successful_last_time = -1
while True:
    try:
        f = urllib2.urlopen(url, data=None, timeout=0.5)
        print "Got past urllib2!"
    except urllib2.URLError:
        now = time.time()
        if verbose:
            print "Cannot resolve url",url
            if time_of_last_success != -1 and time_of_last_failure != -1:
                print "Connection has failed for this long:", now - time_of_last_success,"+/-",loop_time
        # The connection worked, so let's see if it failed last time. If so, let's see how long it was down.
        if time_of_last_success != -1 and time_of_last_failure != -1 and successful_last_time == True:
            print "Connection failed for this long:", now - time_of_last_success,"+/-",loop_time
        time_of_last_failure = now
        successful_last_time = False
        pass
    except:
        print "A different error."
        raise
    else:
        now = time.time()
        if verbose:
            print "Successfully resolved url", url
            if time_of_last_success != -1 and time_of_last_failure != -1:
                print "Connection has worked for this long:",now - time_of_last_failure,"+/-",loop_time
        # The connection failed, so let's see if it worked last time. If so, let's see how long it lasted.
        if time_of_last_success != -1 and time_of_last_failure != -1 and successful_last_time == False:
            print "Connection worked for this long:",now - time_of_last_failure,"+/-",loop_time
        time_of_last_success = now # Ignore the intervening time
        successful_last_time = True

    finally:
        time.sleep(loop_time)
