# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:34:14 2017

@author: Altair47
"""
from bs4 import BeautifulSoup
import random
import datetime
import string
import requests
import textwrap
import time
'''8'''
import getpass
import sys

'''1)'''
def CHARACTER_INPUT():
	name = input("What is your name: ")
	age = int(input("How old are you: "))
	now = datetime.datetime.now()
	year = str((now.year - age)+100)
	print(name + " will be 100 years old in the year " + year)

'''2)'''
def EVEN_OR_ODD():
	A = int(input('Pick a number:'))
	if A%2 == 0:
	    print("even")
	else:
	    print("odd")


'''3)'''
def LESS_THAN():
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

	num = int(input("Choose a number: "))

	new_list = []

	for i in a:
		if i < num:
			new_list.append(i)

	print(new_list)


'''4)'''
def DIVISORS():
	num = int(input("Choose a number: "))
	for i in range(1,num):
		if num%i == 0:
			print(i)



'''5)'''
def LIST_OVERLAP():

	a = (random.choices(range(0,10),k=random.randint(1,17)))

	b = (random.sample(range(0,100),random.randint(1,17)))

	c = []

	for i in a:
		if i in b:
			if i not in c:
				c.append(i)

	print(f"\n {c} \n {a} \n {b}")


'''6)'''
def PALINDROME_WORD():
	a = int(input('Choose method 1 or 2 : '))
	if a == 1:
		word = str(input("Choose a word: "))
		print(len(word))
		for i in range(0,len(word)):
			print(i)
			if word[i] == (word[::-1])[i]:
				if i == len(word)-1:
					print('palindrome ')
			else:
				print('not palindrome')
				break
	else:
		wrd=input("Please enter a word")
		wrd=str(wrd)
		rvs=wrd[::-1]
		print(rvs)
		if wrd == rvs:
		    print("This word is a palindrome")
		else:
			print("This word is not a palindrome")





'''7)'''
def LIST_COMPREHESIONS():
	numlist = []
	list_length = random.randint(5,15)


	while len(numlist) < list_length:
	    numlist.append(random.randint(1,75))
	    

	evenlist = [number for number in numlist if number % 2 == 0] 

	print(numlist)
	print(evenlist)


'''8)'''

def ROCK_PAPPER_SCISSORS():
	user1 = input("What's your name?")
	user2 = input("And your name?")
	user1_answer = getpass.getpass("%s, do yo want to choose rock, paper or scissors?" % user1)
	user2_answer = getpass.getpass("%s, do you want to choose rock, paper or scissors?" % user2)

	def compare(u1, u2):
	    if u1 == u2:
	        return("It's a tie!")
	    elif u1 == 'rock':
	        if u2 == 'scissors':
	            return("%s with Rock wins!" %user1)
	        else:
	            return("%s with Paper wins!" %user2)
	    elif u1 == 'scissors':
	        if u2 == 'paper':
	            return("%s with Scissors win!" %user1)
	        else:
	            return("%s with Rock wins!" %user2)
	    elif u1 == 'paper':
	        if u2 == 'rock':
	            return("%s with Paper wins!" %user1)
	        else:
	            return("%s with Scissors win!" %user2)
	    else:
	        return("Invalid input! You have not entered rock, paper or scissors, try again.")
	        sys.exit()

	print(compare(user1_answer, user2_answer))


'''9)'''
def GUESS_RANDOM_NUMBER():
	a = int(input("Choose Method 1 or 2 : "))
	if a == 1:
		while True:
			print('NEW GAME')
			c = 0
			r = random.randint(0,9)
			while True:
				a = int(input("Guess the number between 0 to 9 or 'exit' to exit: "))
				if a == r:
					print('Found it! After %d tries' %c)
					break
				elif a == 'exit':
					exit()
				else:
					c = c+1
	else:
			# Awroken
			MINIMUM = int(1)
			MAXIMUM = int(9)
			NUMBER = random.randint(MINIMUM,MAXIMUM)
			GUESS = None
			ANOTHER = None
			TRY = 0
			RUNNING = True

			print ("Alright...")

			while RUNNING:
				GUESS = input("What is your lucky number? ")
				if int(GUESS) < NUMBER:
					print ("Wrong, too low.")
				elif int(GUESS) > NUMBER:
					print ("Wrong, too high.")
				elif GUESS.lower() == "exit":
					print ("Better luck next time.")
				elif int(GUESS) == NUMBER:
					print ("Yes thats the one, %d." %NUMBER)
					if TRY < 2:
						print ("Impressive, only %s tries." % str(TRY))
					elif TRY > 2 and TRY < 10:
						print ("Pretty good, %s tries." % str(TRY))
					else:
						print ("Bad, %s tries." % str(TRY))
					RUNNING = False
				TRY = TRY+1


'''10)'''
def LIST_OVERLAP_COMPREHESNION():
	a = int(input("Choose Method 1 or 2 : "))
	if a == 1:
		a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
		b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
		c = []


		result = [i for i in a if i in b]
		c=[i for i in a if i in b if i not in c]
		print(result)
		print(c)
	else:
		a = random.sample(range(1,30), 12)
		b = random.sample(range(1,30), 16)
		result = [i for i in set(a) if i in b]
		print(result)


'''11)'''
def CHECK_PRIMALITY():
	x = int(input('Give me a number to check if its a Prime :'))
	if x == 2:
		print('%d is prime'%x)
	elif (int(str(x)[-1:]))==2 or x<0:
		print('%d is not prime (last digit 2 or the number is >0)'%x)
	else:
		for i in range(2,x-1):
			if x % i != 0:
				continue
			else:
				print('%d is not prime'%x)
				return
		print('%d is prime'%x)
		return

'''12)'''
def LIST_ENDS():
	a = random.sample(range(1,30), 12)
	b = []
	b.append(a[0])
	b.append(a[-1])
	print(a)
	print(b)

'''13)'''
def FIBONACCI():
	c = int(input("Choose how many Fibonacci numbers to generate:"))
	n = []
	if c == 1:
		n.append(1)
	elif c<0:
		print('Cant generate >0 numbers')
	else:
		n.extend((1,1))
		for i in range(c-2):
			n.append(n[-1]+n[-2])
	print(n)

'''14)'''
def LRD_LOOP(x):
	new = []
	for i in x:
		if i not in new:
			new.append(i)
	return new
def LDR_SETS(x):
	return set(x)


def LIST_REMOVE_DUPLICATES():
	a = (random.choices(range(0,10),k=random.randint(10,50)))
	print(a)
	print('LRD LOOP', LRD_LOOP(a))
	print('LDR_SETS', LDR_SETS(a))

'''15)'''
def REVERSE_WORD_ORDER():
	a = input('Input a long string to have its words reversed.\n>')
	'''
	new = a.split()
	new = new[::-1]
	new = ' '.join(new)
	'''
	new = ' '.join(a.split()[::-1])
	print(new)

'''16)'''
def PASSWORD_GENERATOR():
	def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
		return ''.join(random.choice(chars) for _ in range(size))

	print(pw_gen(int(input('How many characters in your password?'))))

'''17)'''
def DECODE_WEBSITE():
	url = 'https://www.nytimes.com/'
	r = requests.get(url)
	r_html = r.text
	soup = BeautifulSoup(r_html,"html.parser")
	for story_heading in soup.find_all(class_="story-heading"): 
		if story_heading.a: 
			print(story_heading.a.text.replace("\n", " "))
		else: 
			print(story_heading.contents[0])

'''18)'''
def COWS_BULLS():
	numberR = random.sample(range(0,9), 4)
	print(numberR)
	b = input("Welcome to the Cows and Bulls Game!\nEnter a number: ")
	Playing = True
	while Playing:
		cows = 0
		bulls = 0
		for i in range(len(numberR)):
			print(i)
			if int(numberR[i])==int(b[i]):
				cows+=1
			elif int(b[i]) in numberR:
				bulls+=1
		print("%d Cows %d Bulls" % (int(cows),int(bulls)))
		if cows == 4:
			Playing = False
			print('Congratz!\nEnding...')
		else:
			b = input("Try again: ")

'''19)'''
def DECODE_WEBSITE_TWO():
	url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
	r = requests.get(url)
	r_html = r.text
	soup = BeautifulSoup(r_html,"html.parser")
	for paragraph in soup.find_all(class_="content-section"): 
		if paragraph.p: 
#			print (textwrap.fill(paragraph.p.get_text(),64))
			print ('\n'.join(textwrap.wrap(paragraph.p.get_text(), 64)))
		else: 
			print(paragraph.get_text())

'''20)'''
def BINARY_ELEM_SEARCH():
	x = random.sample(range(1,500000), 499999)
	x = sorted(x)
	a = int(input('Select the number you want to find if its in the list: '))
	print(time.ctime())

	ta = time.time()
	if a in x:
		print ("Found it! (if a in x)")
	tb = time.time()
	print(tb-ta)

	ta = time.time()
	for i in range(len(x)):
		if int(x[i])==a:
			print("Found it! (for)")
			break
	tb = time.time()
	print(tb-ta)

	ta = time.time()
	L = 0
	R = len(x)-1
	while L <= R:

		if a>int(x[-1]) or a <int(x[0]):
			print("Not found")
			break
			
		m = (L+R)//2
		if int(x[m]) < a:
			L= m+1
			print(m)
		elif int(x[m]) > a:
			print(m)
			R= m-1
		else:
			print("Found it (BinarySearch)")
			break
	tb = time.time()
	print(tb-ta)


'''21)'''
def WRITE_TO_FILE():
	url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
	r = requests.get(url)
	r_html = r.text
	soup = BeautifulSoup(r_html,"html.parser")

	solut=''

	with open('f.txt', 'w') as open_file:

		for paragraph in soup.find_all(class_="content-section"): 
			if paragraph.p: 

				open_file.write ('\n'.join(textwrap.wrap(paragraph.p.get_text(), 64)) + '\n\n')

	#			print (textwrap.fill(paragraph.p.get_text(),64))
				print ('\n'.join(textwrap.wrap(paragraph.p.get_text(), 64)))
			else: 
				print(paragraph.get_text())

#	open_file = open('file_to_save.txt', 'w')
#			open_file.write('\n'.join(textwrap.wrap(paragraph.p.get_text(), 64)))
#	open_file.close()

'''22)'''
def READ_FROM_FILE():
	a = int(input("Choose Method 1 or 2 : "))
	if a == 1:
		counter_dict = {}
		with open('Training_01.txt') as f:
			line = f.readline()
			while line:
				line = line[3:-26]
				if line in counter_dict:
					counter_dict[line] += 1
				else:
					counter_dict[line] = 1
				line = f.readline()
		print(counter_dict)
	elif a==2:
		b=[]
		with open('Training_01.txt', 'r') as open_file:
			a = open_file.read()
		a = a.splitlines()
		print(len(a))
		for i in range(len(a)):
			b.append(a[i][3::].split('/')[0])
		new = []
		for i in b:
			if i not in new:
				new.append(i)
		with open('f.txt', 'w') as open_file:
			open_file.write('Categories:'+ str(len(new))+ '\n')
			open_file.write('\n'.join(new).replace('_',' '))
		print(new)




#	with open('Training_01.txt', 'r') as f:
#		content = f.readlines()
#	# you may also want to remove whitespace characters like `\n` at the end of each line
#	print (content)
#	content = [x.strip() for x in content]




'''
print(x)
for i in range(len(x)):
	if x[i] in x[i+1::]:
		print (x[i]+'\n\n\n\n\n\n\n')
time.sleep(.0001)
'''


import dis
# define the function blocks

# main():
# map the inputs and the coresponding functions to a dictionary
if __name__=="__main__":

	print("Welcome to Practice Python (https://www.practicepython.org) choose the number of lesson's solution.\nType "exit" to exit.\nType 'info' to show available lessons again.\n")
	options = {1 : CHARACTER_INPUT,
	           2 : EVEN_OR_ODD,
	           3 : LESS_THAN,
	           4 : DIVISORS,
	           5 : LIST_OVERLAP,
	           6 : PALINDROME_WORD,
	           7 : LIST_COMPREHESIONS,
	           8 : ROCK_PAPPER_SCISSORS,
	           9 : GUESS_RANDOM_NUMBER,
	           10: LIST_OVERLAP_COMPREHESNION,
	           11: CHECK_PRIMALITY,
	           12: LIST_ENDS,
	           13: FIBONACCI,
	           14: LIST_REMOVE_DUPLICATES,
	           15: REVERSE_WORD_ORDER,
	           16: PASSWORD_GENERATOR,
	           17: DECODE_WEBSITE,
	           18: COWS_BULLS,
	           19: DECODE_WEBSITE_TWO,
	           20: BINARY_ELEM_SEARCH,
	           21: WRITE_TO_FILE,
	           22: READ_FROM_FILE
	}


	for k,v in options.items():
		print (k,v.__name__)
	'''
	for k,v in options.items():
		print (k,dis.dis(v))
	'''

	while True:
		num = input('\n >>')
		try:
			num = int(num)
			if num in options:
				options[num]()
			else:
				print('%d Not a lesson or not yet completed by the supreme leader Altair77' %num)
		except ValueError:
			if num == 'exit':
				exit()
			elif num == 'info':
				for k,v in options.items():
					print (k,v.__name__)
			else:
				print('Wrong input try again?')