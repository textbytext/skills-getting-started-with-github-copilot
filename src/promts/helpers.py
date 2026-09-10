def odd_numbers_and_average(numbers):
	"""Return the odd numbers in a list and their average."""
	odd_numbers = [number for number in numbers if number % 2 != 0]
	average = sum(odd_numbers) / len(odd_numbers) if odd_numbers else None
	return odd_numbers, average


def calculate_average(numbers):
	"""Calculate and return the average value of a list of numbers."""
	if not numbers:
		return None
	return sum(numbers) / len(numbers)

