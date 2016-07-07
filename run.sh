#!/bin/bash

python map.py &
python data.py &
./livestream.sh

