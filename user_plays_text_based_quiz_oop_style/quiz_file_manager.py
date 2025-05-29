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
            Utilities.display_message(f"Error saving question: {e}", delay=1.5)

    # to load/read the quiz
    def load_quiz_content(self):
        with open(self.filename, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
            
        quiz = []
        index = 0
        while index < len(lines):
            question = lines[index]
            choices = [lines[index+1], lines[index+2], lines[index+3], lines[index+4]]
            answer_line = lines[index+5]
            answer = answer_line.split(":")[1].strip()
            quiz.append({
                "question": question,
                "choices": choices,
                "answer": answer
            })
            index += 6
        return quiz