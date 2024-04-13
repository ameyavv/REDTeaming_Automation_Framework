#!/bin/bash

# Clone the repository
git clone https://github.com/smicallef/spiderfoot.git

# Change directory to spiderfoot
#cd spiderfoot

# Start SpiderFoot instance in background and redirect output to sf.log
#python3 ./sf.py -l 127.0.0.1:5001 > sf.log 2>&1 &

# Wait for a moment to ensure SpiderFoot starts up properly
#sleep 5

# Run SpiderFoot CLI
#python3 ./sfcli.py -s http://127.0.0.1:5001

# Optional: Ping command
#ping

#chmod +x run_spiderfoot.sh

#./run_spiderfoot.sh
