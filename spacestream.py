#!/usr/bin/python3

import subprocess
import random

from os import system
from time import sleep, time

sources = [
    'file:/home/pi/space1.mp4',
    'https://www.youtube.com/watch?v=nzkns8GfV-I',
    'https://www.youtube.com/watch?v=6VEZctCSJYk',
    'https://www.youtube.com/watch?v=ddFvjfvPnqk',
    'https://www.youtube.com/watch?v=0QH58nc6xGU',
    'https://www.youtube.com/watch?v=xmVT36Axtn0',
    'https://www.youtube.com/watch?v=DyOYBUKxhlA',
    'https://www.youtube.com/watch?v=CLzKl4s_zhA',
    'https://www.youtube.com/watch?v=pHvmGucGm_E',
    'https://www.youtube.com/watch?v=vPbQcM4k1Ys',
    'https://www.youtube.com/watch?v=Hzn2eBdqYWc',
    'https://www.youtube.com/watch?v=Ddef2QUbNGI',
    'https://www.youtube.com/watch?v=IfHbGxDU2xY',
    'https://www.youtube.com/watch?v=3afEX8a2jPg',
    'https://www.youtube.com/watch?v=AyFMPdHU1n0',
    'https://www.youtube.com/watch?v=PPmnFbpnvMQ',
    'https://www.youtube.com/watch?v=YPv9yKC76hE',
    'https://www.youtube.com/watch?v=psfFJR3vZ78'
]

max_stream_time = 90

i = random.randint(0, len(sources))
new_i = i
start_time = time()
while True:
    if time() - start_time > max_stream_time:
        system('ps aux | grep omx | awk \'{print $2}\' | xargs kill -15')
    livestreamer_processes = subprocess.check_output(['ps aux | grep omx'], shell=True).decode('UTF-8')
    omx_processes = subprocess.check_output(['ps aux | grep vestre'], shell=True).decode('UTF-8')
    print(livestreamer_processes)
    print(omx_processes)
    if ('player' in omx_processes or 'livestreamer' in livestreamer_processes):
        print('Running')
        sleep(5)
        continue
    else:
        while new_i == i:
            new_i = random.randint(0, len(sources)-1)
        i = new_i
        source = sources[i]
        if 'http' in source:
            print('live command')
            command = 'livestreamer {} best --verbose-player -np \'omxplayer\''.format(source)
        else:
            print('omx command')
            source = source.strip('file:')
            command = 'omxplayer {}'.format(source)
        print(command)
        command = command.split(' ')
        subprocess.Popen(command)
        start_time = time()
        sleep(10)
