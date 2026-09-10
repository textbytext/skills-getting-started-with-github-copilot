from promts.helpers import odd_numbers_and_average

def test_odd_numbers_and_average_returns_odds_and_average():
	assert odd_numbers_and_average([1, 2, 3, 4, 5]) == ([1, 3, 5], 3.0)


def test_odd_numbers_and_average_returns_none_for_no_odd_numbers():
	assert odd_numbers_and_average([2, 4, 6]) == ([], None)


def test_odd_numbers_and_average_handles_empty_input():
	assert odd_numbers_and_average([]) == ([], None)
