def greet(name, owner):
    greeting = ''
    if name == owner:
    	greeting = 'Hello boss'
    else:
    	greeting = 'Hello guest'
    return greeting


greet('Daniel', 'Daniel')	#'Hello boss'
greet('Greg', 'Daniel')	#'Hello guest'