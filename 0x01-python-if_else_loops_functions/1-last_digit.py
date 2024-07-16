#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastdigit = abs(number) % 10
if number < 0:
	lastdigit = -{lastdigit}
thestring = "Last digit of {}".format(number, lastdigit)
if lastdigit > 5:
	print(f"{thestring}
