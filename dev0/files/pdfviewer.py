from PyQt5 import QtCore, QtGui, QtWidgets

from os import listdir
from os.path import isfile, join
import re

import csv

    
class PDFViewer(QtWidgets.QLabel):
    clicked=QtCore.pyqtSignal()
    def __init__(self, parent):
        QtWidgets.QLabel.__init__(self, parent)
        
        self.setScaledContents(True)
        
        self.current_path = "../Media/books/history/Bauhaus/"
        self.current_page = 0
        self.set_book(path=self.current_path)
        self.data=[]

    def mousePressEvent(self, ev):
        self.clicked.emit()
        
    def get_book_name(self):
        # Return the name of the current book in the format: the_mythical_man_month
        return self.current_path.split('/')[4].lower()
        
    def set_book(self, path):
        # Set current path to book
        self.current_path = path
        
        # Read page data
        self.read_page_data()
        
        # Update the page
        self.change_page(page_dif=0)
        
    def read_page_data(self):
        # Empty data list
        self.data = []
        
        # Read csv file
        with open('../data/books/book_data.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                current_book = row["book"]
                current_page_number = row["page"]
                
                #Load data into list
                self.data.append({'book': current_book, 'page': current_page_number})
                
                # Update current page variable
                if(current_book == self.get_book_name()):
                    self.current_page = int(current_page_number)
                
                
                
    def write_page_data(self):
        # Write the data list to the data file
        with open('../data/books/book_data.csv', mode='w') as csv_file:
            fieldnames = ['book', 'page']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)
    
        
    def change_page(self, page_dif):
        # Change current page
        self.current_page += page_dif
        
        # if page number is negative then set it to 0
        if(self.current_page < 0): self.current_page = 0
        
        # Get a list of files in the current path
        files = [f for f in listdir(self.current_path) if isfile(join(self.current_path, f))]
        
        # Sort list of files
        files.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
        
        # Create path to specific page number
        page_path = self.current_path + files[self.current_page][2:]
        
        # Display page
        self.setPixmap(QtGui.QPixmap(page_path))
        
        # Change the page in the data list
        for row in self.data:
            if(row['book'] == self.get_book_name()):
                row['page'] = self.current_page
        
        # Write the data to the file
        self.write_page_data()
        