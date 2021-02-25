import integrand_functions


# midpoint rule
def integral_aux_midpoint (left_endpoint, right_endpoint, integrand, func_params, npoints):
   
   dx = (right_endpoint - left_endpoint) / (npoints)
   value = 0
   n = 1
   while n <= (npoints):
      xpoint = left_endpoint + ((2*n - 1)/2) * (dx)
      value += integrand(xpoint,func_params) * (dx)
      n += 1
   return value



# simpson rule 
def integral_aux_simpson (left_endpoint, right_endpoint, integrand, func_params, npoints):
    """
Simpson rule integral=(dx/3)[f(a)+2f(x[i=even])+4f(x[i=odd])+f(b)]
n should b positive even integer
n is the number of subintervals
endpointa would be xi = {x0,x1,x2,...,xn}
    """ 
    dx = (right_endpoint-left_endpoint)/(npoints)
    #B = sum f(x(i=odd)) and C = sum f(x(i=even))
    B = 0
    C = 0
    i = 1
    while i < npoints:
        if i%2 != 0 :
            xpoint = left_endpoint + i * (dx)
            B = B + integrand(xpoint, func_params)
            i = i+1
        elif i%2 == 0:
            xpoint = left_endpoint + i * (dx)
            C = C + integrand(xpoint, func_params)
            i = i+1
    result = ((dx) / 3) * (integrand (left_endpoint, func_params) + 4 * B + 2 * C + integrand (right_endpoint, func_params))
    return result



# Euler rule
def integral_aux_euler (left_endpoint, right_endpoint, integrand, func_params, npoints):
   
   dx = (right_endpoint-left_endpoint) / (npoints)
   value = integrand(left_endpoint, func_params) * (dx)
   n = 1
   while n < (npoints):
      xpoint = left_endpoint + n*(dx)
      value += integrand(xpoint,func_params) * (dx)
      n +=1
   return value


#cheking different auxiliary functions
"""
res= integral_aux_midpoint(2,5,integrand_functions.new_func, {"multiple":3.0 , "shift":2 },10)
print ("mid point is for new_func",res)
res_analytical = integrand_functions.analytical_new_func(2,5,{"multiple":3.0 , "shift":2})
print ("analytical for new func", res_analytical)
res= integral_aux_simpson(2,5,integrand_functions.new_func, {"multiple":3.0 , "shift":2 },10)
print ("simpson point is for new_func",res)
res= integral_aux_euler(2,5,integrand_functions.new_func, {"multiple":3.0 , "shift":2 },10)
print ("euler is for new_func",res)
answer= integral_aux_simpson (2,5,integrand_functions.my_power_func, {"x_shift":3.0 ,"power":2, "y_shift":3 },10)
print ("simpson is for my_power_func" ,answer)
answer= integral_aux_euler (2,5,integrand_functions.my_power_func, {"x_shift":3.0 ,"power":2, "y_shift":3 },100)
print ("euler is for my_power_func" ,answer)
"""