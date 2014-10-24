#!/usr/bin/env python2.7
# http://docs.python.org/2/library/urllib2.html#urllib2.urlopen
import urllib2
# http://docs.python.org/2/library/time.html#time.sleep
import time
import socket

# For catching Ctrl-C.
import signal
import sys

def print_with_time(in_string):
    print time.asctime() + " " + in_string

def exit_cleanly(signal_number, stack_frame):
    if signal_number == signal.SIGINT:
        print ''
        sys.exit(0)
    else:
        sys.exit(1)

signal.signal(signal.SIGINT, exit_cleanly)

# http://docs.python.org/2.7/library/socket.html#socket.socket.settimeout
url = 'http://www.google.com' #TODO: make a command flag for this
loop_time = 0.5 # seconds #TODO: make a command flag for this
# DONE: make global timeout wait forever by default.
global_timeout = 10000 # seconds #TODO: make a command flag for this
time_of_last_success = None
time_of_last_failure = None
running_connection_length = None
running_failure_length = None
verbose = False #TODO: make a command flag for this
successful_last_time = False
socket.setdefaulttimeout(global_timeout)
start_time = time.time()
print "Starting timer."
while True: # have to end the program manually. TODO: make a keypress like Ctrl-D end the program
    try:
        f = urllib2.urlopen(url, data=None, timeout=global_timeout)
    except socket.timeout:
        print "Socket timed out!"
        raise
    except urllib2.URLError:
        now = time.time()
        if time_of_last_success:
            running_failure_length = now - time_of_last_success
        else:
            running_failure_length = now - start_time
        if verbose:
            print "Cannot resolve url",url
            if running_failure_length:
                print_with_time("Connection has failed for this long: "+ str(running_failure_length) + "+/-" + str(loop_time) + " seconds.")
        # The connection failed, so let's see if it worked last time. If so, let's see how long it was up.
        if running_failure_length and successful_last_time == True:
            print_with_time("Connection was up for this long: "+str(running_connection_length)+"+/-"+str(loop_time) + " seconds.")
        time_of_last_failure = now
        successful_last_time = False
        running_connection_length = None
        pass
    else:
        now = time.time()
        if time_of_last_failure:
            running_connection_length = now - time_of_last_failure
        else:
            running_connection_length = now - start_time
        if verbose:
            print "Successfully resolved url", url
            print_with_time("Connection has worked for this long: "+str(running_connection_length)+"+/-"+str(loop_time) + " seconds.")
        # The connection worked, so let's see if it failed last time. If so, let's see how long it was down.
        if running_failure_length and successful_last_time == False:
            print_with_time("Connection failed for this long: "+str(running_failure_length)+"+/-"+str(loop_time) + " seconds.")
        time_of_last_success = now # Ignore the intervening time
        successful_last_time = True
        running_failure_length = None
    finally:
        time.sleep(loop_time)
