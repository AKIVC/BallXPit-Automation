## BallXPit Automation ##

BallXPit Automation Script
A fully automated gameplay engine for the game Ball X Pit, built in Python using a virtual Xbox 360 controller. This script simulates real controller input to move left/right, spam buttons, and automatically skip fusion reactors—allowing the game to run indefinitely without user interaction.

### What It Does ###
- Simulates a virtual Xbox 360 controller using vgamepad
- Automatically moves left and right in timed intervals
- Spams the A button to skip reactors and progress faster
- Optionally triggers upgrade actions (X + A spam)
- Runs in a continuous loop for multi‑hour or multi‑day sessions
- Achieves extremely deep runs far beyond normal human play
This project was built as a fun automation challenge and a way to push the game’s mechanics to their limits.

### How It Works ###
The script uses the vgamepad library to create a persistent virtual controller instance:
- left_joystick_float() handles movement
- press_button() and release_button() simulate A/X presses
- A main loop coordinates movement + button timing
- All actions are sent as real XInput signals, so the game treats them as genuine controller input
Because the controller object persists for the entire session, the script remains stable even during very long runs.
Running the Script (Python Version)
- Install Python 3.10+
- Install dependencies:
  
    `pip install vgamepad`

- Run the script:
python ballxpit_automation.py


Make sure the game is open and focused before starting.
Using the EXE Version (Important)
If you are using the PyInstaller‑built EXE, you should manually install the vgamepad driver/library first.
PyInstaller sometimes fails to bundle the underlying virtual driver correctly, which can cause the EXE to run but not send controller input.
To avoid issues:

    pip install vgamepad

Then run the EXE normally.
This ensures the required driver is already present on the system.


### Notes ###
- This script is for educational and personal use only
- It does not modify the game or memory; it only simulates controller input
- Works best on the Steam version of Ball X Pit
 ### Future Improvements ###
- Randomized timing to appear more human
- Hotkey to pause/stop the automation
- Pixel‑based detection for smarter reactor skipping
