# quiz_file_manager.py -> to handle file naming as well as saving and loading questions

# import the Question class
from question import Question
# import the Utilities class
from utilities import Utilities

class QuizFileManager:
    # constructor to initialize new object
    def __init__(self, filename):
        self.filename = self.ensure_txt_extension(filename)
        
    # ensure filename should have txt extension
    def ensure_txt_extension(self, filename):
        if not filename.endswith(".txt"):
            filename += ".txt"
        return filename
    
    # to save question
    def save_question(self, question):
        try:
            with open(self.filename, "a") as file:
                file.write(question.file_format())
            Utilities.display_message(f"Question saved to {self.filename}", delay=1.5)
        except IOError as e:
            Utilities.display_message(f"Error saving question: {e}", delay=2)

    # to load/read the quiz
    def load_quiz_content(self):
        questions = []
        try:
            with open(self.filename, "r") as file:
                lines = [line.strip() for line in file if line.strip()]
            
            index = 0
            while index < len(lines):
                if index + 5 < len(lines):
                    question_block = lines[index : index + 6]
                    try:
                        q_obj = Question.from_file_lines(question_block)
                        questions.append(q_obj)
                    except Exception as e:
                        Utilities.display_message(f"Error parsing question block starting at line {index}: {e}. Skipping this block.", delay=2)
                else:
                    Utilities.display_message(f"Incomplete question block found at line {index}. Skipping.", delay=2)
                index += 6
        
        except FileNotFoundError:
            Utilities.display_message(f"Error: File '{self.filename}' not found.", delay=2)
        except Exception as e:
            Utilities.display_message(f"An error occurred while loading the quiz: {e}", delay=2)
            
    # to read and return the entire content as a single string
    def get_raw_file_content(self):
        try:
            with open(self.filename, "r") as file:
                return file.read()
            
        except FileNotFoundError:
            return f"Error: File '{self.filename}' not found."
        except Exception as e:
            return f"An error occurred while reading the file: {e}"