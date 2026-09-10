from promts.helpers import odd_numbers_and_average, calculate_average

def test_odd_numbers_and_average_returns_odds_and_average():
	assert odd_numbers_and_average([1, 2, 3, 4, 5]) == ([1, 3, 5], 3.0)


def test_odd_numbers_and_average_returns_none_for_no_odd_numbers():
	assert odd_numbers_and_average([2, 4, 6]) == ([], None)


def test_odd_numbers_and_average_handles_empty_input():
	assert odd_numbers_and_average([]) == ([], None)


def test_calculate_average_returns_average_of_positive_numbers():
	assert calculate_average([1, 2, 3, 4, 5]) == 3.0


def test_calculate_average_returns_average_of_decimals():
	assert calculate_average([1.5, 2.5, 3.0]) == 2.333333333333333


def test_calculate_average_returns_none_for_empty_list():
	assert calculate_average([]) is None

