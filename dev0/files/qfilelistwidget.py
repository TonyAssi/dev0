from PyQt5 import QtCore, QtGui, QtWidgets, Qt, QtTest

import os
from os import listdir
from os.path import isfile, join
import re

    
class QFileListWidget(QtWidgets.QListWidget):
    #clicked=QtCore.pyqtSignal()
    def __init__(self, parent):
        QtWidgets.QListWidget.__init__(self, parent)
        
        # Populate the list
        self.load_list()

    def load_list(self):
        #print("load_list()")
        
        # Get a list of files in the current path
        files = [f for f in listdir("/home/pi/Desktop/dev0/data/diary/") if isfile(join("/home/pi/Desktop/dev0/data/diary/", f))]
        
        # Sort list of files
        files.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
        #print(files)
        
        # Add files to list
        for f in files: self.addItem(f)

    def save_file(self, name, text, status):
        # Show saving alert
        status.show()
        
        # Create file
        file= open("/home/pi/Desktop/dev0/data/diary/" + name,"w+")
        # Write text to file
        file.write(text)
        # Close the file
        file.close
        
        # Check to see if item is already in the list
        items = self.findItems(name, QtCore.Qt.MatchExactly)
        # Add item to list, if it is not already in the list
        if len(items) == 0: self.addItem(name)
        
        # Delay to show saving alert
        QtTest.QTest.qWait(1000)
        # Hide saving alert status
        status.hide()
        
    def get_selected_text(self):
        file = open("/home/pi/Desktop/dev0/data/diary/" + self.get_selected_name(),'r')
        file_text = file.read()
        file.close()
        return file_text
    
    def get_selected_name(self):
        return self.currentItem().text()
    
    def delete_selected(self):
        os.remove("/home/pi/Desktop/dev0/data/diary/" + self.get_selected_name())
        
        self.takeItem(self.currentRow())
    

        
        
        
