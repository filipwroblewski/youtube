def count_sheeps(sheep):
  counter=0
  for i in sheep:
    if i == True:
      counter+=1
  return counter


array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];
              
count_sheeps(array1)   # 17