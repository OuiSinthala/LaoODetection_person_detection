import subprocess
def emit_sound():
  # Get the path to the system beep sound file.
  beep_file = "/Users/mac/Desktop/LaoODetection/LaoODetection/game_sound.mp3"

  # Play the sound file.
  subprocess.Popen(["afplay", beep_file])
