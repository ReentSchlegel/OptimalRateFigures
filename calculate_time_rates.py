from optimal_rates import find_optimal_rate
import numpy as np
import pickle
import datetime



filename = 'koptTopt' + datetime.datetime.today().strftime("%I:%M%p_on_%B_%d_%Y")					# Name of file for the data to store


n = 1000									# Number of groups
u = np.array([0,.1,.5])*n 					# Number of groups that can colaborate
res = 100									# Number of evaluations
mu = np.logspace(-4,4,res)					# res evenly spaced points on log axis 
kopt = np.zeros((u.size,mu.size))			# Allocate memory
Topt = np.zeros((u.size,mu.size))			# Allocate memory


for j in range(0,int(u.size)):				# For all values in u
	for i in range(0,int(mu.size)):			# For all mu
		kopt[j][i],Topt[j][i] = find_optimal_rate(n,u[j],mu[i])		# Calculate the optimal value of k and the achieved time T
		print('Progress: '+ str((i+1)*100./mu.size) + "% of run " + str(j+1) + "/" + str(u.size))	# Output the progress to the console

with open(filename,'wb') as f:				# Open the file
	pickle.dump([u/n,mu,np.array(kopt)*1./n,n*np.array(Topt)],f)	# Store the data


print('Prozess finished. Result is stored in ' + filename)			# Print filename to console