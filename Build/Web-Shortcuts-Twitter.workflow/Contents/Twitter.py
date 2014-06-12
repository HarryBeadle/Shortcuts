#!/usr/bin/env python

# Web-Shortcuts

# Twitter Trends
# Harry Beadle
# 11 JUN 14

Input = raw_input()

Query = Input.replace(" ", "")

URL = "http://www.twitter.com/search?q=" + Query

print URL
