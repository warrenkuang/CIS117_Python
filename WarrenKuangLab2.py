##
# Warren Kuang
# Course: CIS 117 PythonProgramming
# Lab #2: Object Oriented Programming
# Application: Design, implement and test your own class called Message
# that models a basic email application
# Description: Initialization and validation of objects in a class
# that are accessed in a test code
# Input: Sender, recipient, and body that is accessed from 
# wish_list from the test code
# Requirements: Sender and Recipient are printable and 
# less than 50 characters
# Output: Sender, Recipient, and Body of an Email
# Development Environment: Ubuntu 17.0
# Version:  Python 3.7
# Solution File: CIS117_ExampleSolnLab2.py
# Date: 07/18/23

class Message():

    #Class constants
    MAX_LEN = 50 
    EMPTY_STR = ""

    #Constructor that intializes sender and recipient 
    def __init__(self, sender, recipient):
        self.set_sender(sender) #set method for each attribute
        self.set_recipient(recipient)
        self._body = Message.EMPTY_STR #initialize body as an empty string

    #Set the sender of the message
    def set_sender(self, sender):
        if self.str_ok(sender): #checks is sender is valid
            self._sender = sender
            return True
        else:
            self._sender = Message.EMPTY_STR
            return False
    
    #Set the recipient of the message
    def set_recipient(self, recipient):
        if self.str_ok(recipient): #checks if recipient is valid
            self._recipient = recipient
            return True
        else:
            self._recipient = Message.EMPTY_STR
            return False
        
    #Checks if input_string is less than 50 characters and printable
    def str_ok (self, input_string):
        if len(input_string) <= Message.MAX_LEN and input_string.isprintable():
            return True
        else:
            return False
    
    #Function to append the body of text
    def append (self, line_text):
        if self._body == Message.EMPTY_STR: #If empty, starts on the same line
            self._body = line_text + "\n"
        else: #If body already has text, starts on the next line
            self._body += line_text + "\n"

    #Converts message to a formatted string for sender, recipient and body
    # on different lines
    def to_string (self):
        return "From: " + self._sender + "\n" \
            + "To: " + self._recipient + "\n" \
            + self._body
        

            
                