import bisection;

def example_func(x):
    return 3-x**2

def test_bisection():
    location, error, number_of_tries = bisection.bisection_algorithm(example_func, 0, 2, .01)
    assert location - 1.734375 < .00001
    assert abs(error) < .01
    assert number_of_tries == 7
