import bisection;

# Test whether it will work when solution is left endpoint

def example_func(x):
    return 1-x**2

def test_bisection():
    assert bisection.bisection_algorithm(example_func, 1, 2, .01) == (1, 0, 0)
