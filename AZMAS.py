print("\tWelcome to the python self assement unit\n".upper())
SCORE = 0
loop_count = 0
print("INSTRUCTIONS: Note, every questions marks varies and each questions answered wrongly atttracts negative score.you can also decide to skip any question at anytime\n")
print("NOTE: YOU CAN ONLY ANSWER ONLY 3 TIMES")

#function for questions
def user():
		
		user_choice= input("\nchoose a question from set of questions ranging from 1  - 10 : ".upper())
		if user_choice.isdigit():
			user_choice = int(user_choice)
			if user_choice >= 11:
				print("wrong input")
				return user()
			else:
			
				if user_choice == 1:
					Question1()
				elif user_choice == 2:
					Question2()
					
				"""
				elif user_choice == 3:
					Question3()
				elif user_choice == 4:
					Question4()
				elif user_choice == 5:
					Question5()
				elif user_choice == 6:
					Question6()
				elif user_choice == 7:
					Question7()
				elif user_choice == 8:
					Question8()
				elif user_choice == 9:
					Question9()
				elif user_choice == 10:
					Question10()
				else:
					break
	"""
#function for question 1
def Question1():
	global SCORE
	Q1 = input("How many continent are there in the world? : ".lower())
	Ans1= "7" or "seven"
	if Q1 == Ans1:
		SCORE += 2
		#print('your score is ', SCORE)
		#user()
	else:
		SCORE -= 2
		#user()
		#print('your score is ', SCORE)

#function for question 2
def Question2():
	global SCORE
	Q2 = input("what's the longest river in the world? :".lower())
	if Q2 == "mississippi" or "MISSISSIPPI":
	#Ans2 = "mississippi" or "MISSISSIPPI"
	#Q2 = Ans2
	#if Q2 == Ans2:
		SCORE += 3
		#print('your score is ', SCORE)
		#user()
	else:
		SCORE -= 3
		#print('your score is ', SCORE)
		#user()


		"""
def Question3():
	Q3 = input("which country won the 2006 worldcup? : ".lower())

def Question4():
	Q4 = input("who hosted the 2014 worldcup? : " .lower())

def Question5():
	Q5 = input("what is the fifth planent closest to sun? : ".lower())

def Question6():
	Q6 = input("a triangle with all side equal is called? : ".lower())

def Question7():
	Q7 = input("the diameter of a circle is also know as  its ? : ".lower())

def Question8():
	Q8 = input("who was the first man ever be buried? : ".lower())

def Question9():
	Q9 =input("who was the first human ever killed? : ".lower())
def Question10():
	Q10 = input("what is the name of the bone located in the wrist region? : ".lower())




	"""

	
	
	
#this would make the program only 3 question and end	
for loop_count in range(1,4):
	
	user()
print("your score is ", SCORE)
