import time

start_time = time.time()
print('what is your name?')
myname = input()
while myname != 'Jude':
	if myname == 'your name':
		print('Ha ha, very funny. Seriously, who are you?')
		myname = input()
	else:
		print('this is not your name. Please type your real name?')
		myname = input()
print('Hello, '+myname + '. That is a good name. How old are you?')
myAge = int(input())
if myAge < 13:
	print("learning young, that's good")
elif myAge == 13:
	print("you're a tennager now... that's cool, I guess")
elif myAge > 13 and myAge < 30:
	print("Still young, still learning...")
elif myAge >= 30 and myAge < 65:
	print("Now you're adulting.")
else:
	print("... you've lived a long time?")
programAge = int(time.time() - start_time)
print('%s? That\'s funny, I\'m only %s.' % (myAge, programAge))
print('I wish I was %s years old' % (int(myAge) * 2))
time.sleep(3)
print('I\'m tired. I go sleep sleep now.')