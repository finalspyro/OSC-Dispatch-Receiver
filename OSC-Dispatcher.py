import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client

def osc_sync():

    client = udp_client.SimpleUDPClient("127.0.0.1", 57120)

    for x in range(10) :
        number = random.random()
        client.send_message("/filter", [number])
        print("hello world")
        time.sleep(0.1)

osc_sync()

print("DONE")

#SuperCollider code to go with this:
#OSCFunc({ | args |
#     "OSCFunc received the following values from message '/filter':".postln;
#     args[1..].postln;
#}, '/filter');