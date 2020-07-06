from PyQt5 import QtCore, QtGui, QtWidgets

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging


class Mindi(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        # Chat display
        self.text = QtWidgets.QWidget
        # Text input
        self.text_input = QtWidgets.QWidget
        # Chat log
        self.chat = []
        # Chat bot
        self.chatbot = ChatBot('Mindi')
        
    def setup(self, text, text_input):
        # Text display
        self.text = text
        # Text input
        self.text_input = text_input
        # Set initial text
        self.text.setText("say something...")
        
        # Set up chat bot
        # Disable info level logging
        logging.basicConfig(level=logging.CRITICAL)

        # Start by training our bot with the ChatterBot corpus data
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train(
            #'chatterbot.corpus.english'
            '/home/pi/Desktop/dev0/data/mindi/data/english/mindy.yml'
        )
        
    
    def update_chat(self):
        chat_text = ""
        for i,line in enumerate(self.chat):
            if(i % 2 == 0):
                chat_text = chat_text + "Me: " + str(line) + "\n"
            else:
                chat_text = chat_text + "Mindi: " + str(line) + "\n"
        
        self.text.setText(chat_text)
        
        self.text.moveCursor(QtGui.QTextCursor.End)
            
    
    def send_message(self):
        # Get user input
        user_input = self.text_input.text()
        
        # Add user input to chat log
        self.chat.append(user_input)
        
        # Get response from bot
        response = self.chatbot.get_response(user_input)
        
        # Add bot response to chat log
        self.chat.append(response)
        
        # Clear text input
        self.text_input.clear()
        
        # Update chat
        self.update_chat()
        
        
        
        
        
        
        