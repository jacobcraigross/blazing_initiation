import sys
import os
import math
import requests

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting

r = requests.get("https://regulatormoderator.com")
print(r.status_code)

#name = input("whats your name? -- ")
#print("hello", name)

