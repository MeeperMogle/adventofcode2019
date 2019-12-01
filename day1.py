#! /usr/bin/env python3
from math import floor
from sys import exit

lines = list(map(lambda s: s.replace('\n', ''), open('inputs/input1.txt', 'r').readlines()))

# Test
def failIfNotEqual(actual, expected):
	if actual != expected:
		print('Expected', expected, 'but was', actual)
		exit(1)

# Implementation v1
def calculateFuelRequirementV1(mass):
	return floor(int(mass) / 3) - 2

# Implementation v2
def calculateFuelRequirementV2(mass):
	localSum = 0
	while int(mass) > 0:
		mass = int(floor(int(mass) / 3) - 2)
		localSum += mass if mass > 0 else 0
	return localSum

# Run tests on v1
failIfNotEqual(calculateFuelRequirementV1(12), 2)
failIfNotEqual(calculateFuelRequirementV1(14), 2)
failIfNotEqual(calculateFuelRequirementV1(1969), 654)
failIfNotEqual(calculateFuelRequirementV1(100756), 33583)

# Run tests on v2
failIfNotEqual(calculateFuelRequirementV2(14), 2)
failIfNotEqual(calculateFuelRequirementV2(1969), 966)
failIfNotEqual(calculateFuelRequirementV2(100756), 50346)

# Run version 1
sum = 0
for line in lines:
	sum += calculateFuelRequirementV1(line)
print('Version 1:', sum)

# Run version 2
sum = 0
for line in lines:
	sum += calculateFuelRequirementV2(line)
print('Version 2:', sum)
