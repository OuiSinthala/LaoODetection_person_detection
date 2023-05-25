import subprocess
import time

def play_sound():
    mp3_file_path1 = r'LaoODetection/sounds/hello_ceit.wav'
    mp3_file_path2 = r'LaoODetection/sounds/hello_CE.wav'
    mp3_file_path3 = r'LaoODetection/sounds/hell0_CE_president.wav'
    mp3_file_path4 = r"LaoODetection/sounds/president_iceit.wav"

    try:
        subprocess.run(['afplay', mp3_file_path4])
    except FileNotFoundError:
        print("afplay command not found. Make sure you're running macOS.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

