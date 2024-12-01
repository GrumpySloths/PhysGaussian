import os

def debug_print(message):
    if os.getenv('DEBUG_PRINT') == 'True':
        print(message)