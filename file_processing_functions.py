import os
import ntpath
from pyttsx3_processing_functions import finall_function as pyttsx3_run
from user_personalization import main_execute as custom_settings

def get_user_path():
    while True:
        user_path = input(r"Enter text file path:   (.txt file)""\n")
        file_name = ntpath.basename(user_path)
        file_extension = os.path.splitext(file_name)[-1] 
        if file_extension == '.txt':
            print("file extension checked. (.txt given)")
            break
        elif len(os.path.splitext(file_name)) > 1 and file_extension != '.txt':
            print("It seems to entered wrong file. Your file must be text file (.txt)")
        
    return user_path


def path_checker():
    while True:
        user_path = get_user_path()
        print('-' * 80)

        if ntpath.isfile(user_path):
            print(f"Everything sounds OK.Directory recieved correctly")
            print('-' * 80)
            # file_existing_checker(user_path)
            break
        else:
            print("Wrong path recieved, please enter valid path")
            print('-' * 80)

    return user_path


def file_process(recieved_file):
    engine = pyttsx3_run()
    custom_settings()
    with open(recieved_file, 'r') as reader:
        engine.say(reader.read())
    engine.runAndWait()
        
    

def run():
    source_file = path_checker()
    file_process(source_file)
    print('-' * 30)
    print("Text To Speech Process Finished.")




