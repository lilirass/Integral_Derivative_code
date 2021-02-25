import integrand_functions
import auxiliary_integration_functions

#main integration function
def integral(left_endpoint, right_endpoint, integrand, func_params, npoints, precision=1e-10, integration_method="midpoint"):
    """

    """
    n = npoints
    m = 2 * n
    A = 0.0
    B = 0.0
    if integration_method=="midpoint":
         A = auxiliary_integration_functions.integral_aux_midpoint(left_endpoint, right_endpoint, integrand, func_params, n)
         B = auxiliary_integration_functions.integral_aux_midpoint(left_endpoint, right_endpoint, integrand, func_params, m)
    elif integration_method=="simpson":
         A= auxiliary_integration_functions.integral_aux_simpson (left_endpoint, right_endpoint, integrand, func_params, n)
         B= auxiliary_integration_functions.integral_aux_simpson (left_endpoint, right_endpoint, integrand, func_params, n)

    err = float(abs(A-B))
    result = B
    
    while err > precision:
            A = B
            m = 2*m
            B= auxiliary_integration_functions.integral_aux_midpoint(left_endpoint, right_endpoint, integrand, func_params, m)
            err=float(abs(A-B))
            result=B
              
        
        
    return result

answer = integral(0, 1, integrand_functions.my_power_func, {"x_shift":3.0 ,"power":2, "y_shift":3 }, 3, precision=1e-3, integration_method="midpoint")
print ("midpoint", answer)
#answer = integral(0, 1, integrand_functions.my_power_func, {"x_shift":3.0 ,"power":2, "y_shift":3 }, 3, precision=1e-3, integration_method="simpson")
#print ("simpson", answer)