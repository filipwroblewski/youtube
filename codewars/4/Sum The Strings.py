def sum_str(a, b):
    if a == "" and b != "":
    	return f'{b}'
    if a != "" and b == "":
    	return f'{a}'
    if a == "" and b == "":
    	return f'0'
    return f'{int(a) + int(b)}'


sum_str("4","5")	#"9"
sum_str("34","5")	#"39"

sum_str("9","")		#"9"	because: "x + empty = x"
sum_str("","9")		#"9"	because: "empty + x = x"
sum_str("","")		#"0"	because: "empty + empty = 0"