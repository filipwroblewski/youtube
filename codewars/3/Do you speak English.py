def sp_eng(sentence): 
	if sentence.lower().find('english') != -1:
		print('True')
		return True
	print('False')
	return False


sp_eng("english")#, True)
sp_eng("egnlish")#, False)
sp_eng("1234egn lis;h")#, False);
sp_eng("1234english ;k")#, True);
sp_eng("English")#, True);
sp_eng("eNgliSh")#, True);
sp_eng("1234#$%%eNglish ;k9")#, True);
sp_eng("EGNlihs")#, False);
sp_eng("1234englihs**")#, False);