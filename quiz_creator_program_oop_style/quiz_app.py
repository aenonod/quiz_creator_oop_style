# quiz_app.py -> to get the filename and questions also serves as the main menu

# import the Question class
from question import Question
# import the QuizFileManager class
from quiz_file_manager import QuizFileManager

class QuizApp:
    # def for constructor to initialize new object
    def __init__(self):
        self.current_filename = None
        
    # def to get the filename
    def get_filename_from_user(self):
        filename = input("\nInput your filename (w/o extension): ").strip()
        if not filename.endswith(".txt"):
            filename += ".txt"
        return filename
    
    # def to get the data (question, choices, and correct answer) from the user
    def get_data_from_user(self):
        print("\n>>> QUIZ CREATOR <<<")
        question = input("Input question: ")

        choices = []
        print("\nNote: Input 4 choices. No need to put letters. Let the quiz creator run its magic!✨")
        choices.append(input("Choice 1: ").strip())
        choices.append(input("Choice 2: ").strip())
        choices.append(input("Choice 3: ").strip())
        choices.append(input("Choice 4: ").strip())
        
        correct_ans = input("\nCorrect answer (type exactly as one of the choices): ").strip()

        return Question(question_text, choices, correct_ans)
    
    # def to create/edit a quiz
    # def to view a quiz
    # def to run the program (main menu)