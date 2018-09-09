Program to track commercial time when watching CFB streams.
It works by continuously checking the color value at a defined pixel (coordinate), against a set color value (colorVal).
Whenever the pixel is not the chosen color, the program starts a timer. The timer stops when the pixel returns to the set color value.
The total commercial time in seconds is printed every 15ish seconds.