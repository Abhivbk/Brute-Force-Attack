import random
import pyautogui

guess = "abcdefghijklmnopqrstuvwxyz1234567890"
char_list = list(guess)
password = pyautogui.password('Enter the password').strip().lower()
guesspswd = ""
while True:
    guesspswd = random.choices(char_list, k=len(password))
    print(guesspswd)
    if guesspswd == list(password):
        print("Successfullyy Broke into the access \n Password: {}".format(guesspswd))
        break