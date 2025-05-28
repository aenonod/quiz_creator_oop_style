# quiz_file_manager.py -> to handle file naming as well as saving and loading questions

# import the Question class
from question import Question

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
        with open(self.filename, "a") as file:
            file.write(question.file_format())
        print(f"Question saved to {self.filename}")
    
    # to load/read the quiz
    def load_quiz_content(self):
        try:
            with open(self.filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: File '{self.filename}' not found."
        except Exception as e:
            return f"An error occurred while reading the file: {e}"