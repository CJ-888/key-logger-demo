# key-logger-demo
A Python script that listens to keyboard events and logs every 10 key presses to a file. The script stops recording when the 'Esc' key is pressed.

# How it works 
- Listen for Key Presses: The script continuously listens for keyboard events using the pynput library.
- Track Key Presses: Every time a key is pressed, it is added to a list of keys, and a counter is incremented.
- Log Every 10 Key Presses: After 10 key presses, the script writes the logged keys to a file (log.txt), then resets the counter and the list.
- Handle Special Keys: The script handles special keys like space (written as a space) and enter (written as a new line).
- Stop on Esc Key: When the Esc key is pressed, the script stops listening and terminates.
