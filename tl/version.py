# tl/version.py
#
#

""" version related stuff. """

## tl imports

from tl.lib.config import getmainconfig

## basic imports

import os
import binascii

## defines

version = "0.4.1"
__version__ = version

## getversion function

def getversion(txt=""):
    """ return a version string. """
    if txt: return "T I M E L I N E - %s - %s" % (version, txt)
    else: return "T I M E L I N E - %s" % version
