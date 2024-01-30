import secant;

# Test whether it will terminate if it can't find the root

def example_func(x):
    return 3 + x**2

def test_secant():
    assert secant.secant_algorithm(example_func, 0, 5, .01) == "Could Not Locate Root"
