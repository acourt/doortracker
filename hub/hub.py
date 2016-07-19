#!/usr/bin/env python
###################################################################################
#
# Copyright (c)     2010-2016   Motsai
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
###################################################################################

import getopt
import signal
import sys
import httplib, urllib

from neblina import *
from neblinaAPI import NeblinaAPI

###################################################################################


class GracefulKiller:
    isKilled = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit)
        signal.signal(signal.SIGTERM, self.exit)

    def exit(self, signum, frame):
        print("Signal received: {0}.".format(signum))
        self.isKilled = True

###################################################################################

class Door(object):
    """docstring for Door"""
    def __init__(self,doorID, nebAPI):
        self.arg = arg
        self.closeVal = None
        self.openVal = None
        self.doorID = doorID

        nebAPI.streamMAG(True)

    def calibrate():
        print("Calibrating door.\n")
        input("Close the door and press enter")
        self.closeVal = nebAPI.getMAG().mag[0]
        input("Open the door to its fullest and press enter")
        self.openVal = nebAPI.getMAG().mag[0]
        print("Fully calibrated")


def test():
    signalKiller = GracefulKiller()
    while not signalKiller.isKilled:
        params = urllib.urlencode({'id': 1, 'type': 'open', 'position': 0})
        conn = httplib.HTTPConnection("bugs.python.org")
        headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
        conn.request("POST", "", params, headers)
    pass

###################################################################################


def main(address):
    signalKiller = GracefulKiller()

    print("Initialize NeblinaAPI")
    api = NeblinaAPI(Interface.BLE)
    print("Opening device: {0}".format(address))
    api.open(address)
    if not api.isOpened():
        exit("Unable to connect to device.")
    print("Opening BLE streaming port")
    api.setDataPortState(Interface.BLE, True)

    # It is required to downsample streaming rate to 25Hz (40ms delay) or more to ensure
    # reception of all incoming streaming packet and other packet when using BLE on Python.
    api.setDownsample(40)

    print("Starting EulerAngle Streaming")
    api.streamEulerAngle(True)
    while not signalKiller.isKilled:
        params = urllib.urlencode({'number': 12524, 'type': 'issue', 'action': 'show'})
        conn = httplib.HTTPConnection("bugs.python.org")
        headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
        conn.request("POST", "", params, headers)
        print(api.getEulerAngle())
    print("Stopping EulerAngle Streaming")
    api.streamEulerAngle(False)

###################################################################################


def printArguments():
    print("Door tracker v1.0.0")
    print("Neblina commands:")
    print("    -h --help   : Display available commands.")
    print("    -a --address: Device address to use (COM port)")

###################################################################################

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:")
    except getopt.GetoptError:
        printArguments()
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            printArguments()
            sys.exit()
        elif opt in ("-t", "--test"):
            test()
            sys.exit
        elif opt in ("-a", "--address"):
            main(arg)
            sys.exit()

    print("No device address specified. Exiting.")


