# quiz_app.py -> to get the filename and questions also serves as the main menu

# import the Question class
from question import Question
# import the QuizFileManager class
from quiz_file_manager import QuizFileManager

class QuizApp:
    # constructor to initialize new object
    def __init__(self):
        self.current_filename = None
        
    # to get the filename
    def get_filename_from_user(self):
        filename = input("\nInput your filename (w/o extension): ").strip()
        if not filename.endswith(".txt"):
            filename += ".txt"
        return filename
    
    # to get the data (question, choices, and correct answer) from the user
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

        return Question(question, choices, correct_ans)
    
    # create/edit a quiz
    def create_or_edit_quiz(self):
        self.current_filename = self.get_filename_from_user()
        file_manager = QuizFileManager(self.current_filename)

        while True:
            new_question = self.get_data_from_user()
            if new_question:
                file_manager.save_question(new_question)
            else:
                print("Question creation cancelled or invalid input. Not saving this question.")

            add_more = input("\nDo you want to add more questions? (yes/no): ").lower()
            if add_more != "yes":
                break
        
    # view a quiz
    def view_quiz_file(self):
        filename_to_view = input("\nEnter filename to open (with extension): ").strip()
        if not filename_to_view.endswith(".txt"):
            filename_to_view += ".txt"
            
        file_manager = QuizFileManager(filename_to_view)
        content = file_manager.load_quiz_content()
        
        print(f"\n>>> QUIZ ({filename_to_view}) <<<")
        print(content)
        
        input("Press Enter to go back to main menu...")
        
    # run the program (main menu)
    def run(self):
        while True:
                print("\n===== MAIN MENU =====")
                print("👆 Press 1 to create new or edit an existing quiz file")
                print("👆 Press 2 to view a quiz file")
                print("👆 Press 3 to exit")

                try:
                    choice = int(input("\n⭐ Enter your choice: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if choice == 1:
                    self.create_or_edit_quiz()
                elif choice == 2:
                    self.view_quiz_file()
                elif choice == 3:
                    print("\nGoodbye, user!👋")
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")