import random
import pyautogui

guess = "abcdefghijklmnopqrstuvwxyz1234567890"
char_list = list(guess)
guesspswd = ""

def crack_password():
    password = pyautogui.password('Enter the password').strip().lower()
    while True:
        guesspswd = random.choices(char_list, k=len(password))
        print(guesspswd)
        if guesspswd == list(password):
            print("Successfullyy Broke into the access \n Password: {}".format(guesspswd))
            break 

if __name__ == '__main__':
    try:  
        crack_password()    
    except Exception as e:
        if str(e) == "'NoneType' object has no attribute 'strip'":
            print("CLOSED")
        else:
            print(f"Erorr: {e}")
            crack_password
