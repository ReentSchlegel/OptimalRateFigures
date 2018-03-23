from scipy.integrate import quad
from order_statistic_functions import pdf_runtime_worker



mu = 1
k = 1
u = 0

def fun(t):
	return t*(k-u)*pdf_runtime_worker((k-u)*t,mu)

limit = [1./(k-u),float("inf")]

I = quad(fun,limit[0],limit[1])

print(I)
