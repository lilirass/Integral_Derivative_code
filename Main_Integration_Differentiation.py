import integrand_functions
import auxiliary_integration_functions

#main integration function to give precision of 1e-10 by default
def integral(left_endpoint, right_endpoint, integrand, func_params, npoints, precision=1e-10, integration_method="midpoint"):
    """
it is the main integration function with defult precision of 1e-10 and midpoint inegration method as a default
you can change the integration methods to "simpson" or "euler" as well
    """
    n = npoints
    m = 2 * n
    A = 0.0   #integration with n points
    B = 0.0   #integration with 2 * n points
    if integration_method == "midpoint":
         A = auxiliary_integration_functions.integral_aux_midpoint(left_endpoint, right_endpoint, integrand, func_params, n)
         B = auxiliary_integration_functions.integral_aux_midpoint(left_endpoint, right_endpoint, integrand, func_params, m)
    elif integration_method == "simpson":
         A= auxiliary_integration_functions.integral_aux_simpson (left_endpoint, right_endpoint, integrand, func_params, n)
         B= auxiliary_integration_functions.integral_aux_simpson (left_endpoint, right_endpoint, integrand, func_params, m)
    elif integration_method == "euler" :
         A= auxiliary_integration_functions.integral_aux_euler (left_endpoint, right_endpoint, integrand, func_params, n)
         B= auxiliary_integration_functions.integral_aux_euler (left_endpoint, right_endpoint, integrand, func_params, m)

    err = float(abs(A - B))
    result = B
    
    while err > precision:
            A = B
            m = 2 * m
            B= auxiliary_integration_functions.integral_aux_midpoint(left_endpoint, right_endpoint, integrand, func_params, m)
            err = float(abs(A - B))
            result=B
              
    return result

 
# integration of two different integrand functions for all three different integration methods:
print ("for general_power_func")
answer = integral(1, 7, integrand_functions.general_power_func, {"x_multiple":3, "x_shift":3.0 ,"power":2, "y_shift":3 }, 3, precision=1e-3, integration_method="midpoint")
print ("midpoint", answer)
answer = integral(1, 7, integrand_functions.general_power_func, {"x_multiple":3, "x_shift":3.0 ,"power":2, "y_shift":3 }, 3, precision=1e-3, integration_method="simpson")
print ("simpson", answer)
answer = integral(1, 7, integrand_functions.general_power_func, {"x_multiple":3, "x_shift":3.0 ,"power":2, "y_shift":3 }, 3, precision=1e-3, integration_method="euler")
print ("euler", answer)
res_analytical = integrand_functions.analytical_general_power_func(1, 7, {"x_multiple":3, "x_shift":3.0 ,"power":2, "y_shift":3 })
print ("analytical for new func", res_analytical)

print("for new_func")
answer = integral(-1, 5, integrand_functions.new_func, {"multiple":3, "shift":3.0 }, 3, precision=1e-3, integration_method="midpoint")
print ("midpoint", answer)
answer = integral(-1, 5, integrand_functions.new_func, {"multiple":3, "shift":3.0 }, 3, precision=1e-3, integration_method="simpson")
print ("simpson", answer)
answer = integral(-1, 5, integrand_functions.new_func, {"multiple":3, "shift":3.0 }, 3, precision=1e-3, integration_method="euler")
print ("euler", answer)
res_analytical = integrand_functions.analytical_new_func (-1, 5, {"multiple":3, "shift":3.0 })
print ("analytical", res_analytical)
