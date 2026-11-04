import os
import sys
import json
import math
import random
import datetime
import time

print("1.OS Module")
print("Current Directory:",os.getcwd())
print("Operating System:",os.name)

print("\n2.SYS Module")
print("Python Version:",sys.version)
print("Platform:",sys.platform)

print("\n3.JSON Module")
data={"name":"Python","version":3.14}
json_data=json.dumps(data)
print("JSON:",json_data)
print("Converted:",json.loads(json_data))

print("\n4.MATH Module")
print("Square root:",math.sqrt(64))
print("Power:",math.pow(2,5))
print("Factorial:",math.factorial(5))

print("\n5.RANDOM Module")
print("Random Number:",random.randint(1,1000))
print("Random Choice:",random.choice(["Apple","Orange","Banana"]))

print("\n6.DATETIME Module")
now=datetime.datetime.now()
print("Current Date and Time:",now)
print("Current Year:",now.year)

print("\n7.TIME Module")
print("Current Timestamp:",time.time())
print("Formatted Time:",time.ctime())

