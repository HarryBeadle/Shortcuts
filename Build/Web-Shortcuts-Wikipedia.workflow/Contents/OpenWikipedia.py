#!/usr/bin/env python
import webbrowser

Input = raw_input()

try:
    Formatted_Input = Input.replace(" ", "_")
    URL = "http://www.wikipedia.org/wiki/" + Formatted_Input
except:
    URL = "http://www.wikipedia.org/"

print URL