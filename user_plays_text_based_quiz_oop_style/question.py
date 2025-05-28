# question.py -> to format or organize provided questions by the user

class Question:
    # constructor to initialize new object
    def __init__(self, item, choices, correct_ans_text):
        self.item = item
        self.choices = choices
        self.correct_ans_text = correct_ans_text
        self.correct_ans_letter = self.get_correct_ans_letter()
    
    # determine the letter (a, b, c, d) for the correct answer
    def get_correct_ans_letter(self):
        choice_letters = ['a', 'b', 'c', 'd']
        for i, choice in enumerate(self.choices):
            if choice.lower() == self.correct_ans_text.lower():
                return choice_letters[i]
        return ""
        
    # format the question data for writing to a text file
    def file_format(self):
        output = f"\nQuestion: {self.item}\n"
        for i, choice in enumerate(self.choices):
            output += f"{chr(97 + i)}) {choice}\n" # chr(97) = 'a'
        output += f"Correct answer: {self.correct_ans_letter}) {self.correct_ans_text}\n"
        return output
        
    # easy printing of a question object
    def __str__(self):
        return f"Q: {self.item}, Choices: {self.choices}, Correct: {self.correct_ans_text}"