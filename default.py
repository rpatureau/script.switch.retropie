# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:31:20 2024

@author: remi
"""

import xbmc
import subprocess
import sys
import time
import os

def close_kodi():
    # xbmc.executebuiltin('XBMC.Quit()')
    xbmc.executebuiltin('Quit()')

def is_kodi_running():
    return xbmc.getCondVisibility('System.IsKodiRunning')

def open_retropie():
    subprocess.run(['emulationstation'])

close_kodi()

timeout = 60  # Set a timeout value in seconds
start_time = time.time()

while is_kodi_running() and (time.time() - start_time) < timeout:
    time.sleep(1)  # Wait for 1 second

# Check if Kodi is still running after the timeout
if is_kodi_running():
    print("Kodi did not close within the timeout")
    os.system("pkill -f kodi")

open_retropie()

sys.exit()
