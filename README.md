Name: Jack Hurley (jth2165)

For hardware setup, lineup 7 push buttons and have a switch on the left and a switch on the right.
The push buttons should each have one pin connected to ground and the other connected to an esp32 output pin.
In my code/design, I have the keys arranged as C, D, E, F, G, A, B and
the output pins on the esp32 being 25, 23, 12, 13, 18, 4, 5 respectively.
As for the switches, the middle pins will each connect to an esp32 output pin and
the left pins will connect to ground and the right pins will connect to 5V.
Have the left switch be used to change to playing sharps and have the right switch used to play the notes.
In my code/design, I have the left switch connected to pin 22 on the esp32 and the right switch connected to pin 27.
For the optional part, the esp32 can be powered by the battery by connecting it to the esp32's ground and 5V pins.
Then, for the raspberry pi, connect it to a monitor with a speaker.
This is where you'll see and hear the notes being played.

video link: https://youtu.be/CRvM9g38wiM
