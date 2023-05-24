import subprocess

def play_sound():
    mp3_file_path = '/Users/mac/Desktop/LaoODetection_1_project/LaoODetection/sounds/hello3.mp3'
    try:
        subprocess.run(['afplay', mp3_file_path])
    except FileNotFoundError:
        print("afplay command not found. Make sure you're running macOS.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

