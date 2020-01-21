#########################################################################################
#   This training will showcase exploratory data analysis methods in Python using our
#   HEAL lab projects as a context.
#     Coded by Jeff Swigert and Oliver Duncan
#     Last Updated: 1/20/2020
#     Based on material covered in EDA in Python datacamp.com course
#########################################################################################

# Cool snippets of code found by Oliver

import numpy as np

x = [4 , 9 , 6, 3, 1]
y = np.array(x)

high = y > 5
y[high]

print(high)
print(y[high])

# gk_heights = np_heights[np_positions == 'GK']
