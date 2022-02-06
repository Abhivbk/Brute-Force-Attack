from msilib.schema import Error
import random
import pyautogui

guess = "abcdefghijklmnopqrstuvwxyz1234567890"
char_list = list(guess)
guesspswd = ""
while True:
    try:
        password = pyautogui.password('Enter the password').strip().lower()
        guesspswd = random.choices(char_list, k=len(password))
        print(guesspswd)
        if guesspswd == list(password):
            print("Successfullyy Broke into the access \n Password: {}".format(guesspswd))
            break
    except Exception as e:
        print(f"Erorr")
