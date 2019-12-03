#! /usr/bin/env python3
from math import floor
from sys import exit
import re

lines = list(map(lambda s: s.replace('\n', ''), open('inputs/input3.txt', 'r').readlines()))

# Test
def failIfNotEqual(actual, expected):
	if actual != expected:
		print('Expected', expected, 'but was', actual)
		exit(1)

# Implementation v1
def findAllPositionsOfPath(path):
	pathPositions = set()

	currentX = 0
	currentY = 0

	for instruction in path:
		steps = int(re.search('\d+', instruction).group())
		direction = str(re.search('[^\d]', instruction).group())
		
		while steps > 0:
			if direction == 'R':
				currentX += 1
			elif direction == 'L':
				currentX -= 1
			elif direction == 'D':
				currentY += 1
			elif direction == 'U':
				currentY -= 1
			pathPositions.add((currentX, currentY))
			steps -= 1
	return pathPositions

def findIntersections(path1, path2):
	path1Positions = findAllPositionsOfPath(path1)
	path2Positions = findAllPositionsOfPath(path2)
	return path1Positions.intersection(path2Positions)

def findClosestCrossingDistanceV1(path1, path2):
	commonPositions = findIntersections(path1, path2)
	shortestDistance = None
	for position in commonPositions:
		currentDistance = abs(position[0]) + abs(position[1])
		if shortestDistance is None:
			shortestDistance = currentDistance
			continue
		if currentDistance < shortestDistance:
			shortestDistance = currentDistance
	return shortestDistance

# Implementation v2
def findNumberOfStepsToReachPosition(path, position):
	currentX = 0
	currentY = 0

	totalStepsTaken = 0
	for instruction in path:
		steps = int(re.search('\d+', instruction).group())
		direction = str(re.search('[^\d]', instruction).group())
		
		while steps > 0:
			if direction == 'R':
				currentX += 1
			elif direction == 'L':
				currentX -= 1
			elif direction == 'D':
				currentY += 1
			elif direction == 'U':
				currentY -= 1
			steps -= 1
			totalStepsTaken += 1

			if currentX == position[0] and currentY == position[1]:
				return totalStepsTaken

def findFewestStepsCrossingV2(path1, path2):
	commonPositions = findIntersections(path1, path2)
	lowestStepSum = None
	for intersection in commonPositions:
		currentStepsInPath1 = findNumberOfStepsToReachPosition(path1, intersection)
		currentStepsInPath2 = findNumberOfStepsToReachPosition(path2, intersection)
		currentSumOfSteps = currentStepsInPath1 + currentStepsInPath2

		if lowestStepSum is None:
			lowestStepSum = currentSumOfSteps
		if currentSumOfSteps < lowestStepSum:
			lowestStepSum = currentSumOfSteps
	return lowestStepSum


examplePath1 = ['R8','U5','L5','D3']
examplePath2 = ['U7','R6','D4','L4']

# Run tests on v1
failIfNotEqual(findClosestCrossingDistanceV1(examplePath1, examplePath2), 6)

# Run tests on v2
failIfNotEqual(findFewestStepsCrossingV2(examplePath1, examplePath2), 30)

# Run version 1
path1 = lines[0].split(',')
path2 = lines[1].split(',')
print('Version 1:', findClosestCrossingDistanceV1(path1, path2))

# Run version 2
print('Version 2:', findFewestStepsCrossingV2(path1, path2))
