# Autograding Example: Python
This example project is written in Python, and tested with pytest.

### The assignment
Write a bisection algorithm whose inputs are a function that will be set equal to zero, the left endpoint, the right endpoint, and an error tolerance. The outpouts should be the location of the root, the approximate value of the function at the found root, and the number of iterations.


### Setup command
`sudo -H pip3 install pytest`

### Run command
`pytest`

### Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be unaccessible.
