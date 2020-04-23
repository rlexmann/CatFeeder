#!/usr/bin/python3
from gpiozero import LED
from time import sleep
import argparse
import datetime
from pathlib import Path
import subprocess

def feed(duration):
    p = LED(26, active_high = False)
    p.on()
    sleep(duration)
    p.off()

parser = argparse.ArgumentParser(description="Engage cat feeder for specified time.")
parser.add_argument("--duration", "-d", help="feeding duration (in seconds)", default=12.0, type=float, required=False)

args = parser.parse_args()

if args.duration:
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    msg = "{}: engaging for {} seconds.  ".format(now_str, args.duration)
    print(msg)
    with open(Path("~/catfeeder.log").expanduser(),"a") as logfile:
        logfile.write(msg + '\n')
    feed(args.duration)

    rc = subprocess.call(str(Path("~/bin/commit_log.sh").expanduser()))
