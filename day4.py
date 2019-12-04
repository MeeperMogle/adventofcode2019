#! /usr/bin/env python3
from math import floor
from sys import exit
from re import search

range_start = 273025
range_end = 767253

# Test
def failIfNotEqual(actual, expected):
	if actual != expected:
		print('Expected', expected, 'but was', actual)
		exit(1)

# Implementation v1
def number_meets_criteria(number):
	index = 1
	number = str(number)
	length = len(str(number))

	highest_number_found = number[0]
	has_found_double = False
	while index < length:
		if number[index] < highest_number_found:
			return False
		elif number[index] > highest_number_found:
			highest_number_found = number[index]
		elif number[index] == number[index - 1]:
			has_found_double = True
		index += 1
	return has_found_double

def count_criteria_meeters_in_range(start, end):
	current = start
	meet_criteria = 0
	while current <= end:
		if number_meets_criteria(current):
			meet_criteria += 1
		current += 1
	return meet_criteria

# Implementation v2
def number_meets_with_added_criteria(number):
	number = str(number)
	d = 0
	found_exclusive_double = False

	while d <= 9:
		ds = str(d)
		match = search('([^'+ds+']|^)'+ds+ds+'([^'+ds+']|$)', number)
		if match is not None:
			found_exclusive_double = True
			break
		d += 1

	if found_exclusive_double:
		return number_meets_criteria(int(number))
	return False

def count_number_meet_extra_criteria(start, end):
	current = start
	meet_criteria = 0
	while current <= end:
		if number_meets_with_added_criteria(current):
			meet_criteria += 1
		current += 1
	return meet_criteria

# Run tests on v1
failIfNotEqual(number_meets_criteria(111111), True)
failIfNotEqual(number_meets_criteria(223450), False)
failIfNotEqual(number_meets_criteria(123789), False)

# Run tests on v2
failIfNotEqual(number_meets_with_added_criteria(112233), True)
failIfNotEqual(number_meets_with_added_criteria(123444), False)
failIfNotEqual(number_meets_with_added_criteria(111122), True)

# Run version 1
print('Version 1:', count_criteria_meeters_in_range(range_start, range_end))

# Run version 2
print('Version 2:', count_number_meet_extra_criteria(range_start, range_end))

