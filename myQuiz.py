# My Quiz
blank = ["__1__","__2__","__3__","__4__","__5__","__6__"]

easy_question = "There are __1__ champions in the game __2__, each with their own __3__. The game was created by __4__."

medium_question = "In the year __1__ the game __2__ was created, based out of __3__ and in a __4__ setting"

hard_question = "__1__ was the __2__ of the game __3__, released in the year __4__. The game was released from __5__ and has a __6__ setting."

easy_answer = ['137', 'League of Legends', 'abilities', 'Riot Games']
medium_answer = ['2011', 'Dark Souls', 'Japan', 'Medieval']
hard_answer = ['$25,000,000', 'Dark Souls 3', '2016', 'Japan', 'Medieval']
#Introduction
print "Evan's Quiz"
#This prompts the user to choose which difficulty they want
question = raw_input("Easy, Medium, or Hard?")
#Defines answers for each difficulty
def answer_List(question):
    if question == "Easy" or question == "easy":
        return easy_answer
    elif question == "Medium" or question == "medium":
        return medium_answer
    elif question == "Hard" or question == "hard":
        return hard_answer
#Defines difficulty level
def difficulty(question):
    #if input is not equal to these values, asks them to try again
    #if input equals the value, return the value chosen
    """
    Input:
    Question that asks for get_Difficulty
    Behavior:
    Prints the respective quiiz based in input.
    Returns:
    Quiz level
    """
    if question == "Easy" or question == "easy":
        return easy_question
    elif question == "Medium" or question == "medium":
        return medium_question
    elif question == "Hard" or question == "hard":
        return hard_question
    else:
        question = raw_input("Oops! Remember to only input Easy, Medium, or Hard!")
    print difficulty

def easy_Level_blank(easy_question,easy_answer):
    if user_input==easy_answer[0]:
        print "Correct!"
        return medium_question

def play_Quiz():
    difficulty = get_Difficulty()
    quiz = game_data[level]['quiz']
    print quiz
    answer_List = game_data[leve]['answers']
    count = 0
    answers_index = 0
#Defines input answers
def answer_Question(difficulty):
    """
    Input:
    difficulty selected by users.
    Behavior:
    uses answers that relates to difficulty users suggest.
    loops through and sees if answers are the same as the list of answers and prompts users
    """
    answer_Count = 0
    next_answer_Count = 1
    index = 1

    answer_Choice = answer_List(question)
#if question number is less than number of questions run the following
    while index < len(blank) + 1:
        answer = raw_input("Go ahead and answer!" + str(index) + ":" +"\n")
        if answer_Question != answer_Choice[answer_Count]: #if answers is not equal to defined answers, asks to try again
            answer = raw_input("Try again! Answer with a number or capital letter!")
        if answer_Question == answer_Choice[answer_Count]:
            print "\nGood job! Next question!\n"
            quiz = play_Quiz.replace(blank[count], answer_Choice.upper())
            count += 1
            answers_Count = answers_Count + 1
            next_answer_Count = next_answer_Count + 1

            print quiz
            if count == len(blank):
                return you_win()



def replaceQuiz():
    answer_Choice = answer_List(question)
    newlist = []
    count = 0
    maxblank = 6

    if count < maxblank:
        count = count + 1
        print count

def correctanswer():
    """
    Input:
    None
    Behavior:
    Loops answers and prints out.
    Return:
    None

    maxcount = 6
    answer_Count = 0
    answer_Choice = answer_List(question)
    while answer_Count < maxcount:
        print "Yes! The correct answers are"
        for answer in answer_Choice:
            print answer_Choice[answer_Count]
            answer_Count = answer_Count + 1
    """
#Defines the rest of the functions
def main():
    """
    Input:
    None
    Behavior:
