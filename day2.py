#! /usr/bin/env python3
from math import floor
from sys import exit

lines = list(map(lambda s: s.replace('\n', ''), open('inputs/input2.txt', 'r').readlines()))

# Test
def failIfNotEqual(actual, expected):
	if actual != expected:
		print('Expected', expected, 'but was', actual)
		exit(1)

# Implementation v1
def runIntcodeV1(theProgram, noun=None, verb=None):
	index = 0

	if noun is not None and verb is not None:
		program[1] = noun
		program[2] = verb

	while theProgram[index] != 99:
		operation = theProgram[index]
		operatorA = theProgram[theProgram[index + 1]]
		operatorB = theProgram[theProgram[index + 2]]
		writeToIndex = theProgram[index + 3]

		if operation == 1:
			theProgram[writeToIndex] = operatorA + operatorB
		elif operation == 2:
			theProgram[writeToIndex] = operatorA * operatorB
		
		index += 4
	return theProgram[0]

# Implementation v2
def runIntcodeV2(theProgram, desiredResultFromV1):
	noun = 0

	programLength = len(theProgram)
	
	while noun < programLength:
		verb = 0

		while verb < programLength:
			result = runIntcodeV1(program, 12, 2)
			if result == desiredResultFromV1:
				return (100 * noun) + verb
			verb += 1
		noun += 1

# Run tests on v1
exampleProgram1 = [1,0,0,0,99]
exampleProgram2 = [2,3,0,3,99]
exampleProgram3 = [2,4,4,5,99,0]
exampleProgram4 = [1,1,1,4,99,5,6,0,99]

failIfNotEqual(runIntcodeV1(exampleProgram1), 2)
failIfNotEqual(runIntcodeV1(exampleProgram2), 2)
failIfNotEqual(runIntcodeV1(exampleProgram3), 2)
failIfNotEqual(runIntcodeV1(exampleProgram4), 30)

# Run tests on v2
#program = list(map(lambda n: int(n), lines[0].split(',')))
#failIfNotEqual(runIntcodeV2(program, <redacted>), 1202)

# Run version 1
program = list(map(lambda n: int(n), lines[0].split(',')))
print('Version 1:', runIntcodeV1(program, 12, 2))

# Run version 2
#program = list(map(lambda n: int(n), lines[0].split(',')))
#print('Version 2:', runIntcodeV2(program, 19690720))
