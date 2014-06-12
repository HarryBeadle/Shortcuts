#!/usr/bin/env python

import os

try:
    os.remove("~/Library/Services/Window-Shortcuts")
    os.remove("~/Library/Services/Web-Shortcuts")
except:
    pass