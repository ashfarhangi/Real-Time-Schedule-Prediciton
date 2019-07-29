"""creating simulated dataset for our code.
"""
import random

list_range = 360
def create_ran_df():
	with open('data/random.csv','w') as f:
		for i in range(list_range):
			arg = [i,random.randint(0,10),random.randint(0,2)]
			f.write("{},{},{}\n".format(arg[0],arg[1],arg[2]))
create_ran_df()