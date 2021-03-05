import socket
import pygame
import time

UDP_IP = "192.168.86.33" # The IP that is printed in the serial monitor from the ESP32
SHARED_UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
sock.connect((UDP_IP, SHARED_UDP_PORT))

c = "/home/pi/Downloads/68441__pinkyfinger__piano-c.wav"
cSharp = "/home/pi/Downloads/68440__pinkyfinger__piano-c.wav"
d = "/home/pi/Downloads/68442__pinkyfinger__piano-d.wav"
dSharp = "/home/pi/Downloads/68444__pinkyfinger__piano-eb.wav"
e = "/home/pi/Downloads/68443__pinkyfinger__piano-e.wav"
f = "/home/pi/Downloads/68446__pinkyfinger__piano-f.wav"
fSharp = "/home/pi/Downloads/68445__pinkyfinger__piano-f.wav"
g = "/home/pi/Downloads/68448__pinkyfinger__piano-g.wav"
gSharp = "/home/pi/Downloads/68447__pinkyfinger__piano-g.wav"
a = "/home/pi/Downloads/68437__pinkyfinger__piano-a.wav"
aSharp = "/home/pi/Downloads/68439__pinkyfinger__piano-bb.wav"
b = "/home/pi/Downloads/68438__pinkyfinger__piano-b.wav"

notes = []

def loop():
    while True:
        data = sock.recv(2048)
        c_val = chr(data[0])
        d_val = chr(data[1])
        e_val = chr(data[2])
        f_val = chr(data[3])
        g_val = chr(data[4])
        a_val = chr(data[5])
        b_val = chr(data[6])
        play_val = chr(data[7])
        sharp_val = chr(data[8])
        print("%c %c %c %c %c %c %c %c %c" %(sharp_val, c_val, d_val, e_val, f_val, g_val, a_val, b_val, play_val))
        if play_val == '0':
            if c_val  == '0' and sharp_val == '0':
                notes.append(c)
            if d_val  == '0' and sharp_val == '0':
                notes.append(d)
            if e_val  == '0' and sharp_val == '0':
                notes.append(e)
            if f_val  == '0' and sharp_val == '0':
                notes.append(f)
            if g_val  == '0' and sharp_val == '0':
                notes.append(g)
            if a_val  == '0' and sharp_val == '0':
                notes.append(a)
            if b_val  == '0' and sharp_val == '0':
                notes.append(b)

            if c_val  == '0' and sharp_val == '1':
                notes.append(cSharp)
            if d_val  == '0' and sharp_val == '1':
                notes.append(dSharp)
            if f_val  == '0' and sharp_val == '1':
                notes.append(fSharp)
            if g_val  == '0' and sharp_val == '1':
                notes.append(gSharp)
            if a_val  == '0' and sharp_val == '1':
                notes.append(aSharp)

        else:
            pygame.mixer.init()
            for x in notes:
                pygame.mixer.music.load(x)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue

if __name__ == "__main__":
    sock.send('Hello ESP32'.encode())
    loop()
