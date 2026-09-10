def odd_numbers_and_average(numbers):
	"""Return the odd numbers in a list and their average."""
	odd_numbers = [number for number in numbers if number % 2 != 0]
	average = sum(odd_numbers) / len(odd_numbers) if odd_numbers else None
	return odd_numbers, average


