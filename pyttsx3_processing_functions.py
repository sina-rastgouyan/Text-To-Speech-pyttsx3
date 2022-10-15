import platform
import pyttsx3


def user_operating_system_detector():
    client_operating_system = platform.system().lower()

    return client_operating_system

def set_engine_driver_properties(os_type):
    if os_type == 'windows':
        windows_configuration = pyttsx3.init('sapi5')
        return windows_configuration
    elif os_type == 'darwin':
        mac_os_configuration = pyttsx3.init('nsss')
        return mac_os_configuration
    else:
        other_os_configuration = pyttsx3.init('espeak')
        return other_os_configuration

def finall_function():
    os_type = user_operating_system_detector()
    return set_engine_driver_properties(os_type)




