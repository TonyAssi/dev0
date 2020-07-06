from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
import os
import socket
import simpleaudio as sa
import threading
import time
import sys

class Wifi(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        
        # Create roamer thread
        roamer = threading.Thread(target=self.run_roamer, args=())
        roamer.daemon = True
        roamer.start()
       
    
    def run_roamer(self):
        start_time = time.time()
        current_time = start_time
        interval = 1
        
        while True:
            current_time = time.time() - start_time
            #print(current_time)
            time.sleep(interval)
    
    def reboot(self):
        # reboot
        os.system('sudo reboot')
        
    def log_out(self):
        sys.exit(0)
        
    
    def update_status(self, status):
        # if socket can connect to internet then update status to "CONNECTED"
        # else "NOT CONNECTED"
        try:
            socket.create_connection(("www.google.com", 80))
            status.setText("CONNECTED")
        except OSError:
            status.setText("NOT CONNECTED")
            
    def dial_up(self):
        filename = '../Media/sound/dial_up.wav'
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing
        
        
    def sign_in(self, network, pw, status):
        # Wait cursor
        self.setCursor(QCursor(QtCore.Qt.WaitCursor))
        
        # Formatting wpa_supplicant file
        config_lines = [
            'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev',
            'update_config=1',
            'country=US',
            '\n',
            'network={',
            '\tssid="{}"'.format(network),
            '\tpsk="{}"'.format(pw),
            '\tkey_mgmt=WPA-PSK',
            '}',
            '\n'
          ]

        # Add a new line
        config = '\n'.join(config_lines)

        # Open wpa_supplicant.conf in write mode
        with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w+") as wifi:
            wifi.write(config)
        
        # Update wifi configuration
        os.system('wpa_cli -i wlan0 reconfigure')
        
        # Play dial up sound
        self.dial_up()
        
        # Update wifi status
        self.update_status(status)
        
        # Wait cursor
        self.setCursor(QCursor(QtCore.Qt.ArrowCursor))
