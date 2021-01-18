from random import choice

length = int(input("Length of password: "))
count = int(input("How many passwords should be generated ? "))

symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`!@#$%^&*()_+-=':;<>,./?"

def gen_pass(length):
	password = ""
	for i in range(length):
		password += choice(symbols)

	print(password)

try:
	while count:
		gen_pass(length)
		count -= 1
except ValueError:
	pass