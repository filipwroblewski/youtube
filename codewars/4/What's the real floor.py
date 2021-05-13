""" 
What's the real floor?

With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them.
Basements (negatives) stay the same as the universal level.
Examples
1  =>  0 
0  =>  0
5  =>  4
15  =>  13
-3  =>  -3
"""

def get_real_floor(n):
    if(n > 0):
    	n -= 1
    if(n >= 13):
    	n -= 1
    return n

get_real_floor(1)	# 0
get_real_floor(5)	# 4
get_real_floor(15)	# 13