import math

def my_power_func(x, func_params):

   """
    my_power_funx = (x+x0)^n + y0

   """
   x0 = func_params["x_shift"]
   n = func_params["power"]
   y0 = func_params["y_shift"]

   a=0
   res=x+x0
   if n==0:
      res=1+y0
   elif n<0:
       n=-1*n
       while a<(n-1):
          res=res*(x+x0)
          a+=1
       res=(1/res)+y0
   else:
      while a<(n-1):
         res=res*(x+x0)
         a+=1
      res = res +y0
               
   return res


def analytical_integral_my_power_func(left_endpoint, right_endpoint, func_params):
   """
analytical_integral = ((x+x0)^(n+1))/(n+1) + y0*x
   """
   x0 = func_params["x_shift"]
   n = func_params["power"]
   y0 = func_params["y_shift"]

   res = (((right_endpoint + x0) ** (n+1))/(n+1) + y0*right_endpoint) - (((left_endpoint + x0) ** (n+1))/(n+1) + y0 * left_endpoint)
   return (res)




def general_power_func (x, func_params):
   """
general_power_func = A* (x+x0)^n + y0
   """
   A = func_params["x_multiple"]
   x0 = func_params["x_shift"]
   n = func_params["power"]
   y0 = func_params["y_shift"]
   res = A* (x+x0)**n + y0
   return (res)

def analytical_general_power_func (left_endpoint, right_endpoint, func_params):
   """
general_power_func =[ A * (x+x0)^(n+1)]/(n+1) + y0*x
   """
   A = func_params["x_multiple"]
   x0 = func_params["x_shift"]
   n = func_params["power"]
   y0 = func_params["y_shift"]
   res =(((A* (right_endpoint+x0)**(n+1))/(n+1)) + y0*right_endpoint) - (((A* (left_endpoint+x0)**(n+1))/(n+1)) + y0*left_endpoint)
   return (res)

def new_func(x,func_params):
   """
new_func = C/(x^2 + a^2)
   """

   c = func_params["multiple"]
   a = func_params["shift"]

   return (c/(x**2 + a**2))

def analytical_new_func(left_endpoint, right_endpoint,func_params):
   """
c * arctan (x/a)/a + c
   """
   c = func_params["multiple"]
   a = func_params["shift"]
   res = (c/a) * ((math.atan(right_endpoint/a)) - (math.atan(left_endpoint/a)))
   return (res)  

   

   
    
def sin_of_power_func (x, f, func_params , sin_params):
   """
sin_of_power_func = A * f (x, fun_params) + B
   """
   A = sin_params["multiplicity"]
   B = sin_params["shift"]
   res = A * math.sin (f(x, func_params)) + B
   return (res)

 
my_res = my_power_func (1,{"x_shift":3.0 ,"power":2, "y_shift":3 } )
print (my_res)
my_res = my_power_func (3,{"x_shift":2.0 ,"power":4, "y_shift":10 } )
print (my_res)
my_res = my_power_func (-2,{"x_shift":2 ,"power":4, "y_shift":10 } )
print (my_res)
my_res = my_power_func (-2,{"x_shift":-2 ,"power":-3, "y_shift":10 } )
print (my_res)


my_res = general_power_func (-2, {"x_multiple": 3, "x_shift":-3.0 ,"power":3, "y_shift":10 })
print(my_res)

my_res = sin_of_power_func (1,general_power_func,{"x_multiple": 2, "x_shift":3.0 ,"power":2, "y_shift":3 }, {"multiplicity": 2 , "shift" :10})
print (my_res)
