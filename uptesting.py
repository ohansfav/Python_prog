score= 0
Question_with_answer = [["How many contient does the world contain init?", ["7", "seven"]],["which is the longest river in the world?",["mississippi"]],["which country won the 2006 world cup",["italy"]]]

User_Answered =[[],[]]


//for ask question 
def ask_question(question):
	answer = input(f"{question[0].upper()}: ").lower().strip()
	return answer in question[1]
	
	
while True:
	user_choice = input(f"\nchoose a question from ranging from 1 - {len(Question_with_answer)}".upper())	
	try:
		user_choice = int(user_choice.strip()) - 1
	except ValueError:
		continue
	if ask_question(Question_with_answer[user_choice]):
		score +=2
		New_question = Question_with_answer.pop()
		User_Answered.append(New_question)
	else:
		score -= 2
		New_question = Question_with_answer
