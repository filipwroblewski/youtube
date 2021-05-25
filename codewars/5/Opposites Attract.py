def lovefunc( flower1, flower2 ):
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0):
    	return True
    return False

lovefunc(1,4)	#True
lovefunc(2,2)	#False
lovefunc(0,1)	#True
lovefunc(0,0)	#False