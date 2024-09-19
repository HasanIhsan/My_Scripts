import time
import threading
from pynput import keyboard, mouse

# Initialize mouse and keyboard controllers
mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

# Flags to control the mining
is_mining = False
width = 10  # Width of the mining area
height = 10  # Height of the mining area (how many rows deep)
block_size = 1  # Assuming each block is 1 unit
move_delay = 0.2  # Delay between moves
turn_delay = 0.5  # Time to hold the turn keys for 90 degrees rotation

# Function to hold left click (mining)
def hold_mouse1():
    mouse_controller.press(mouse.Button.left)
    time.sleep(0.1)
    mouse_controller.release(mouse.Button.left)

# Function to move the player forward
def move_forward():
    keyboard_controller.press('w')
    time.sleep(move_delay)
    keyboard_controller.release('w')

# Function to move the player to the right (to start a new row)
def move_right():
    keyboard_controller.press('d')
    time.sleep(move_delay)
    keyboard_controller.release('d')

# Function to move the player to the left (to start a new row in opposite direction)
def move_left():
    keyboard_controller.press('a')
    time.sleep(move_delay)
    keyboard_controller.release('a')

# Function to turn the player 90 degrees to the right using the keyboard
def turn_right():
    keyboard_controller.press(keyboard.Key.right)  # Hold the right arrow key
    time.sleep(turn_delay)  # Hold it for a short time (adjust for your game's sensitivity)
    keyboard_controller.release(keyboard.Key.right)

# Function to turn the player 90 degrees to the left using the keyboard
def turn_left():
    keyboard_controller.press(keyboard.Key.left)  # Hold the left arrow key
    time.sleep(turn_delay)  # Hold it for a short time (adjust for your game's sensitivity)
    keyboard_controller.release(keyboard.Key.left)

# Main mining function that will move the player in a grid, mining the area
def mine_area(width, height):
    global is_mining
    is_mining = True
    
    for row in range(height):  # For each row in the grid (Y-axis)
        if not is_mining:
            break
        
        # Move forward for the entire width of the row
        for block in range(width):
            if not is_mining:
                break
            hold_mouse1()  # Simulate mining the block
            move_forward()  # Move forward one block
        
        if not is_mining:
            break
        
        # At the end of each row, decide whether to turn left or right, based on the row number
        if row % 2 == 0:  # Even rows: Turn right
            turn_right()
            move_right()  # Move one block to the right to the next row
            turn_right()  # Face the opposite direction for the next row
        else:  # Odd rows: Turn left
            turn_left()
            move_left()  # Move one block to the left to the next row
            turn_left()  # Face the opposite direction for the next row

# Function to stop the mining process
def stop_mining():
    global is_mining
    is_mining = False
    print("Mining stopped")

# Keyboard listener to start and stop the mining process
def on_press(key):
    global is_mining
    try:
        if key.char == 'm':  # Start mining when 'm' is pressed
            print("Mining started")
            threading.Thread(target=mine_area, args=(width, height)).start()
        elif key.char == 'x':  # Stop mining when 'x' is pressed
            stop_mining()
    except AttributeError:
        pass

# Listener for key events
def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Start the listener in a separate thread
listener_thread = threading.Thread(target=start_listener)
listener_thread.start()
