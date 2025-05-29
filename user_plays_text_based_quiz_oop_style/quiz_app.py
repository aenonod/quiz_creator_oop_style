# quiz_app.py -> to get the filename and questions also serves as the main menu

# import random module
import random
# import the Question class
from question import Question
# import the QuizFileManager class
from quiz_file_manager import QuizFileManager
# import the Utilities class
from utilities import Utilities

class QuizApp:
    # constructor to initialize new object
    def __init__(self):
        self.current_filename = None
        self.quiz_questions = []
        
    # to get the filename
    def get_filename_from_user(self, prompt_message="\nInput your filename (w/o extension): "):
        filename = input(prompt_message).strip()
        if not filename.endswith(".txt"):
            filename += ".txt"
        return filename
    
    # to get the data (question, choices, and correct answer) from the user
    def get_data_from_user(self):
        Utilities.clear_screen()
        print("\n>>> QUIZ CREATOR <<<")
        question = input("Input question: ").strip()

        choices = []
        print("\nNote: Input 4 choices. No need to put letters. Let the quiz creator run its magic!✨")
        choices.append(input("Choice 1: ").strip())
        choices.append(input("Choice 2: ").strip())
        choices.append(input("Choice 3: ").strip())
        choices.append(input("Choice 4: ").strip())
        
        while True:
            correct_ans_letter = input("\nCorrect answer (a/b/c/d): ").strip().lower()
            if correct_ans_letter in ["a", "b", "c", "d"]:
                # Basic check if the corresponding choice actually exists
                choice_index = ord(correct_ans_letter) - ord('a')
                if choice_index < len(choices):
                    return Question(question, choices, correct_ans_letter)
                else:
                    print("🚫 Error: Correct answer letter refers to a choice that doesn't exist.")
            else:
                print("🚫 Invalid choice. Please enter only 'a', 'b', 'c', or 'd'.")
    
    # create/edit a quiz
    def create_or_edit_quiz(self):
        self.current_filename = self.get_filename_from_user()
        file_manager = QuizFileManager(self.current_filename)

        while True:
            new_question = self.get_data_from_user()
            if new_question:
                file_manager.save_question(new_question)
            else:
                Utilities.display_message("Question creation cancelled or invalid input. Not saving this question.", delay=2)

            add_more = input("\nDo you want to add more questions? (yes/no): ").lower()
            if add_more != "yes":
                break

        while True: # Inner loop for "add more questions"
            Utilities.clear_screen()
            add_more = input("\nDo you want to add more questions? (yes/no): ").strip().lower()
            if add_more == "yes":
                break
            elif add_more == "no":
                Utilities.display_message(f"\n📝 Quiz '{self.current_filename}' created or updated successfully!", delay=2)
                return # Exit function entirely
            else:
                Utilities.display_message("🚫 Invalid input. Please answer with 'yes' or 'no'.", delay=2)
        
    # view a quiz
    def view_quiz_file(self):
        filename_to_view = get_filename_from_user("\nEnter filename to open (with extension): ").strip()
        Utilities.pause(1.5)
        Utilities.clear_screen()
            
        file_manager = QuizFileManager(filename_to_view)
        content = file_manager.get_raw_file_content()
        
        print(f"\n>>> QUIZ ({filename_to_view}) <<<")
        print(content)
        
        input("Press Enter to go back to main menu...")
        
        while True:
            Utilities.display_message("\n❗ Entering 'no' will exit the program.", delay=0)
            back = input("Go back to main menu? (yes/no): ").strip().lower()
            if back == "yes":
                Utilities.pause(1)
                Utilities.clear_screen()
                break
            elif back == "no":
                Utilities.display_message("\nExiting...", delay=1)
                exit()
            else:
                Utilities.display_message("\n🚫 Invalid input. Returning to main menu...", delay=1)
                break
        
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