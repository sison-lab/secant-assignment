import bisection;

# Test whether it will work when solution is found exactly in the interior

def example_func(x):
    return 1-x**2

def test_bisection():
    assert bisection.bisection_algorithm(example_func, 0, 16, .01) == (1.0, 0.0, 4)
