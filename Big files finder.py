# Big files finder.py
import os

def check(current_size, given_size):
	if(current_size >= given_size*1024**2):
		print(os.path.join(root, name)) 

# finding files bigger than 1GB on your disk D
given_size = 1000
current_size = 0
disk_letter = 'D'

for root, dirs, files in os.walk(f"{disk_letter.upper()}:\\", topdown=False): 
	for name in files:
		current_size = os.path.getsize(os.path.join(root, name))
		check(current_size, given_size)

	for name in dirs:
		current_size = os.path.getsize(os.path.join(root, name))
		check(current_size, given_size)
