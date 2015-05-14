def num(s):
	try: 
		return float(s)
	except ValueError:
		raise TypeError

print("Skriv två tal")
n1 = input()
n2 = input()
try:
	n1 = num(n1)
	n2 = num(n2)
	print(n1 + n2)
except TypeError:
	print("Det måste vara tal, forihilvide...")