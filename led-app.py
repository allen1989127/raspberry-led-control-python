#!/usr/bin/env python

import socket
import RPi.GPIO as gpio

HOST = ''
PORT = 8888

s = None

LED0 = 18

def turn_led(flag) :
    gpio.setmode(gpio.BOARD)
    gpio.setup(LED0, gpio.OUT)
    if flag == '0x00' :
        gpio.output(LED0, gpio.HIGH)
    else :
        gpio.output(LED0, gpio.LOW)

def create_socket() :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

def main() :
    create_socket()
    while 1 :
        conn, addr = s.accept()
        data = conn.recv(1)
        turn_led(data)
        conn.send('0x00')
        conn.close()

    s.close()

if __name__ == '__main__' :
    main()
