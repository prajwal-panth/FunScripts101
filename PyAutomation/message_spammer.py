import pyautogui
import time

def spam_message(message, repeat_count, interval_ms):
    """
    Spam a message with a specified interval in milliseconds.

    Args:
    message (str): The message to spam.
    repeat_count (int): The number of times to repeat the message.
    interval_ms (int): The interval in milliseconds between each message.
    """
    try:
        for i in range(1, repeat_count + 1):
            pyautogui.typewrite(message)
            pyautogui.press("enter")
            time.sleep(interval_ms / 1000)  # Convert milliseconds to seconds
    except Exception as e:
        print(f"An error occurred while spamming: {str(e)}")


if __name__ == "__main__":
    message_to_spam = input("Enter the message to spam: ")

    while True:
        try:
            spam_count = int(input("Enter the number of times to spam the message: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Get interval in milliseconds
    while True:
        try:
            spam_interval_ms = int(input("Enter the interval (in ms) between each message (minimum 96ms): "))
            if spam_interval_ms < 96:
                print("Interval must be at least 96 milliseconds. Please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    input("Press Enter when Ready, then quickly focus on the target input field...")
    print("Starting in 5 seconds...")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    try:
        # Run the spam function
        spam_message(message_to_spam, spam_count, spam_interval_ms)
        print("Spamming completed!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

''' //OR
import time
import logging
import pyperclip
from pynput.keyboard import Key, Controller

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
keyboard = Controller()

def spam_message(message, repeat_count, interval_ms):
    try:
        pyperclip.copy(message)
        for i in range(1, repeat_count + 1):
            logging.info(f"Sending message {i}/{repeat_count}: {message}")
            
            with keyboard.pressed(Key.ctrl):
                keyboard.press('v')
                keyboard.release('v')
                
            time.sleep(0.1)  # Small delay after pasting
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            
            time.sleep(interval_ms / 1000)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        message_to_spam = input("Enter the message to spam: ")
        
        # Get number of times to spam
        while True:
            try:
                spam_count = int(input("Enter the number of times to spam the message: "))
                break
            except ValueError:
                print("Please enter a valid integer for number of times.")

        # Get interval in milliseconds
        while True:
            try:
                spam_interval_ms = int(input("Enter the interval (in milliseconds, minimum 96ms) between each message: "))
                if spam_interval_ms < 96:
                    print("Interval must be at least 96 milliseconds. Please try again.")
                else:
                    break
            except ValueError:
                print("Please enter a valid integer for interval in milliseconds.")


        input("Press Enter when Ready, then quickly focus on the target input field...")
        print("Starting in 5 seconds...")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)

        spam_message(message_to_spam, spam_count, spam_interval_ms)
        print("Spamming completed!")
    except Exception as e:
        logging.error(f"An error occurred in main: {str(e)}")
'''
