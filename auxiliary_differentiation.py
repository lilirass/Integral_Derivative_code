import integrand_functions

def differentiate (a, func, func_params, h=0.0001):
    """
 this function will calculate the value of derivative function in one point
 central difference formula: f'(a) = [f(a+h) - f(a-h)]/(2h)
 func = function 
 a = compute the derivative at this point 
 func_params = a dictionary of all function's parameters
 h = step size, is defined h= 0.1 by default
    """
    derivative = 0.5 * (func ((a + h) , func_params) - func ((a-h) , func_params))/h
    return derivative


print (differentiate (2, integrand_functions.general_power_func, {"x_multiple":3, "x_shift":3.0 ,"power":2, "y_shift":3 }))
print (integrand_functions.derivative_general_power_func (2, {"x_multiple":3, "x_shift":3.0 ,"power":2 }))