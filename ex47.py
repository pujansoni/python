from pprint import pprint as pp
m = {'H': [1,2,3],
	 'He': [3,4],
	 'Li': [6,7]}
m['H'] += [4,5,6]
print(pp(m))