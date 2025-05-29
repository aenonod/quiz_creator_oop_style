# utilities.py -> for clear screen, time sleep, and display message

# import os module
import os
# import time module
import time

class Utilities:
    # def to clear screen
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
        
    # def for time sleep
    @staticmethod
    def pause(seconds):
        time.sleep(seconds)
        
    # def for display message with time of delay
    @staticmethod
    def display_message(message, delay=1.5):
        print(message)
        Utilities.pause(delay)