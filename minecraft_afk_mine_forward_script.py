import threading
import time
from pynput import keyboard, mouse

# Flags to control the actions
is_running = False
stop_script = False
pause_actions = False  # New flag to pause actions during rotation

# Initialize mouse and keyboard controllers
mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

# Function to hold 'W' and click the left mouse button
def hold_w_and_click():
    global is_running, pause_actions
    while is_running:
        if not pause_actions:  # Only hold W and click Mouse1 if not paused
            keyboard_controller.press('w')
            mouse_controller.press(mouse.Button.left)
            time.sleep(0.01)  # Adjust for how fast you want the clicks
            mouse_controller.release(mouse.Button.left)
        else:
            time.sleep(0.1)  # Small delay while paused

def rotate_and_click():
    global is_running, pause_actions
    while is_running:
        time.sleep(60)  # Wait for 1 minute before performing the rotation

        if not is_running:  # Stop if not running
            break

        # Pause the actions while we rotate and click
        pause_actions = True

        # Rotate the mouse 90 degrees to the left (adjust sensitivity as needed)
        print("Looking 90 degrees left")
        mouse_controller.move(-500, 0)  # Adjust this value depending on your sensitivity

        # Simulate right mouse click (placing a block or using an item)
        mouse_controller.press(mouse.Button.right)
        time.sleep(0.2)  # Slight delay to simulate the click action
        mouse_controller.release(mouse.Button.right)

        # Rotate the mouse back to the original position
        print("Looking back to original position")
        mouse_controller.move(500, 0)  # Move the mouse back to original position

        print("Resuming W key and Mouse1 click")
        pause_actions = False  # Resume holding W and clicking Mouse1

def on_press(key):
    global is_running, stop_script

    try:
        # Detect if Alt + * is pressed to start the action
        if key == keyboard.KeyCode.from_char('*') and keyboard.Key.alt_l in pressed_keys:
            if not is_running:
                print("ALT + * pressed: auto")
                is_running = True
                threading.Thread(target=hold_w_and_click).start()
                threading.Thread(target=rotate_and_click).start()  # Start the rotating action
                
        # Detect if Alt + - is pressed to stop the action
        elif key == keyboard.KeyCode.from_char('-') and keyboard.Key.alt_l in pressed_keys:
            print("ALT + - pressed: stopping auto")
            is_running = False
            keyboard_controller.release('w')  # Release 'W' when stopping
            mouse_controller.release(mouse.Button.left)
        
        # Detect if Alt + K is pressed to exit the script
        elif key == keyboard.KeyCode.from_char('k') and keyboard.Key.alt_l in pressed_keys:
            print("Alt + K pressed. Exiting script...")
            stop_script = True
            return False  # Stop the listener and exit the program
    except AttributeError:
        pass

# List to track pressed keys
pressed_keys = set()

# Start tracking when a key is pressed
def on_press_wrapper(key):
    pressed_keys.add(key)
    on_press(key)

# Track when a key is released
def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press_wrapper, on_release=on_release) as listener:
    print("script running!")
    listener.join()
