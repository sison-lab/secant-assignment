import bisection;

# Test whether it will terminate if it can't find the root

def example_func(x):
    return 3 + x**2

def test_bisection():
    assert bisection.bisection_algorithm(example_func, 0, 1, .01) == "Could Not Locate Root"
