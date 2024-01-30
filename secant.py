def secant_algorithm(function, left_endpoint, right_endpoint, error_tolerance):
    guess = left_endpoint
    error = function(guess)
    number_of_tries = 0
    return guess, error
