# question.py -> to format or organize provided questions by the user

class Question:
    # constructor to initialize new object
    def __init__(self, item, choices, correct_ans_letter):
        self.item = item
        self.choices = choices
        self.correct_ans_letter = correct_ans_letter.lower()

        choice_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        if self.correct_ans_letter in choice_map and len(choices) > choice_map[self.correct_ans_letter]:
            self.correct_ans_letter = choices[choice_map[self.correct_ans_letter]]
        else:
            self.correct_ans_text = "N/A"
        
    # format the question data for writing to a text file
    def file_format(self):
        output = f"\nQuestion: {self.item}\n"
        for i, choice in enumerate(self.choices):
            output += f"{chr(97 + i)}) {choice}\n" # chr(97) = 'a'
        output += f"Correct answer: {self.correct_ans_letter}\n"
        return output
    
    # to check if the letter input by the user matches the correct letter
    def check_user_answer(self, user_input_letter):
        return user_input_letter.lower() == self.correct_ans_letter
        
    # parses lines from a file to create object
    @staticmethod
    def from_file_lines(lines):
        question_text = lines[0].replace("Question: ", "").strip()
        
        choices = []
        for i in range(1,5):
            choice_line = lines[i].strip()
            choices.append(choice_line[3:].strip())
            
        correct_ans_line = lines[5].strip()
        correct_ans_letter = correct_ans_line.replace("Correct answer: ", "").strip().lower()
        
        return Question(question_text, choices, correct_ans_letter)
        
    # easy printing of a question object
    def __str__(self):
        return f"Q: {self.item}, Choices: {self.choices}, Correct: {self.correct_ans_text}"