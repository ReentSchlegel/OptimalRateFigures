import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import pickle

filename = 'koptTopt12:56PM_on_March_23_2018'		# Name of file with stored data


with open(filename,'r') as f:						# Open the file with stored data
	u,mu,kopt,Topt = pickle.load(f)					# Load the data
	

fig, (ax1,ax2) = plt.subplots(2,1)					# Open a figure

for i in range(int(u.size)):						# One plot for every value in u
	ax1.plot(mu,Topt[i],Label = 'Normalized Security = ' + str(u[i]))
	ax2.plot(mu,kopt[i],Label = 'Normalized Security = ' + str(u[i]))

# First plot Tn
ax1.set_xscale('log')								# Logarithmic mu axis
ax1.set_xlim([0.1,10])								# Range of mu values
ax1.set_ylim([0,16])								# Range of Tn values
ax1.set_yticks([2*x for x in range(0,9)])			# Ticks of Tn in 0.1 steps
ax1.grid(which = 'both')							# Show a fine grid
ax1.set_xlabel('$\mu$, Straggling parameter')		# Label for mu axis
ax1.set_ylabel('$nT^*$')							# Label for Tn axis
ax1.set_title(r'$T^* \times n$ as a function of $\mu$')		# Title
ax1.legend()

# Second plot k/n
ax2.set_xscale('log')								# Logarithmic mu axis
ax2.set_yticks([0.1*x for x in range(0,11)])		# Ticks of k over n in 0.1 steps
ax2.grid(which = 'both')							# Show a fine grid
ax2.set_xlabel('$\mu$, Straggling parameter')		# Label for mu axis
ax2.set_ylabel('$k^*/n$')							# Label for k over n axis
ax2.set_title(r'$\frac{k^*}{n}$ as a function of $\mu$')	# Title
ax2.legend()

plt.show()											# Show the plot