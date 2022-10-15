from pyttsx3_processing_functions import finall_function as pyttsx3_func


def user_custom():
    speech_gender = speech_gender_config()
    speech_rate_settings()


    return speech_gender

def speech_rate_settings():
    engin = pyttsx3_func()
    engin.setProperty('rate', 140)
    
    



def engine_gender_settings(gender_selection):
    engine = pyttsx3_func()
    voices = engine.getProperty('voices')
    if gender_selection in ['f', 'female']:
        gender_selected = engine.setProperty('voice', voices[1].id)
    elif gender_selection in ['m', 'male']:
        gender_selected = engine.setProperty('voice', voices[0].id)

    return gender_selected


def speech_gender_config():
    while True:
        speech_gender_selection = input(
            'Please choose speech gender: (f, female: female    m, male: male)\n').lower()
        if speech_gender_selection in ['f', 'female', 'm', 'male']:
            gender_chosen = engine_gender_settings(speech_gender_selection)
            break
        else:
            print("Invalid gender choosen.\nValid input ---> (f,female: female)     m,male: male")
    
    return gender_chosen

def main_execute():
    final_personalized_settings = user_custom()
    return final_personalized_settings

print()