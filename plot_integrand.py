from order_statistic_functions import pdf_q_order_statistic_in_group
import matplotlib.pyplot as plt
import numpy as np



n = 1000
k = 1
u = 0
mu = 10**(-4)

t = np.linspace(1./(k-u), (k+10)*(n-k+10)*5./((k-u)*n*mu*(n-k+1))+1./(k-u),500)


# define a function for the integration to calculate the expected runtime
def expected_value_function(t,k):
	return t*(k-u)*pdf_q_order_statistic_in_group((k-u)*t,k,n,mu)


plt.plot(t,expected_value_function(t,k))
plt.show()

