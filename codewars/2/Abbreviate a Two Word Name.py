# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# Patrick Feeney => P.F

def abbrev_name(name):
	initials = ''
	arr = name.split()
	for n in arr:
		initials += n[0].upper() + '.'

	print(initials[0:-1])
	return initials[0:-1]


abbrev_name("Sam Harris") #"S.H"
abbrev_name("Patrick Feenan") #"P.F"
abbrev_name("Evan Cole") #"E.C"
abbrev_name("P Favuzzi") #"P.F"
abbrev_name("David Mendieta") #"D.M"
abbrev_name('bofhSruzP zrPdWHHcpdign') # 'B.Z'