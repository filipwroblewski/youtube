import os
import re

nums = []
file_names = []
schemaRegex = re.compile(r'file \d+.txt') # file num.txt
path = 'files'
for root, dirs, files in os.walk(path, topdown=False): 
	for name in files:
		schema = schemaRegex.search(name)
		
		if(schema != None):
			file_names.append(name)
			file_name = schema.group()
			numRegex = re.compile(r'\d+')
			num = numRegex.search(file_name)
			nums.append(num.group())

gaps = []
# finding gap
for i in range(len(nums)):
	if i != 0 and int(nums[i - 1]) + 1 != int(nums[i]):
		gaps.append(i)

old_file_names = file_names.copy()

ealier_num = 0
for i in range(len(file_names)):
	start_index = int(str(file_names[i]).find('file '))
	end_index = int(str(file_names[i]).find('.txt'))
	n = int(file_names[i][start_index + 5:end_index])

	if ealier_num != 0 and n != ealier_num + 1:
		counter = 1
		for j in range(gaps[0], len(file_names)):
			file_names[j] = f'file {ealier_num + counter}.txt'
			counter += 1
		gaps.pop(0)
	ealier_num = n

for i in range(len(file_names)):
	if old_file_names[i] != file_names[i]:
		print(f'{file_names[i]} => {old_file_names[i]}')
		
		old_file = os.path.join(path, old_file_names[i])
		new_file = os.path.join(path, file_names[i])
		os.rename(old_file, new_file)
	

