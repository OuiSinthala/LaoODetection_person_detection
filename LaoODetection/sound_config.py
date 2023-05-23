import keyboard
import pygame

def default_sound():
    mp3_file = "LaoODetection_person_detection\LaoODetection\sounds\game_sound.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()
    # Allow time for the sound to play
    pygame.time.wait(3000)
    # Stop the sound
    pygame.mixer.music.stop()

def play_sound1():
    mp3_file = "LaoODetection_person_detection\LaoODetection\sounds\hello2.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()
    # Allow time for the sound to play
    pygame.time.wait(1000)
    # Stop the sound
    pygame.mixer.music.stop()


def play_sound2():
    mp3_file = "LaoODetection_person_detection\LaoODetection\sounds\hello3.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()
    # Allow time for the sound to play
    pygame.time.wait(2000)
    # Stop the sound
    pygame.mixer.music.stop()

function_mappings = {
    "1": play_sound1,
    "2": play_sound2,
}

def run_with_key_control(default_function, function_mappings):
    # Global variable to store the current active function
    current_function = default_function

    # Event handler for key press
    def key_press(event):
        nonlocal current_function

        if event.name == "a":
            current_function = default_function
        elif event.name in function_mappings:
            current_function = function_mappings[event.name]

    # Set the initial default function
    current_function = default_function

    # Register the key press event
    keyboard.on_press(key_press)

    # Main program loop
    while True:
        current_function()

def sound_config_func():
    run_with_key_control(default_sound, function_mappings)
