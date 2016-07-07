#!/bin/bash

while true
do
    livestreamer http://ustream.tv/channel/iss-hdev-payload best --player omxplayer --fifo --player-args "--win 640,360,1920,1080 {filename} --layer 1"
done

