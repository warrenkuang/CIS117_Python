##
# Warren Kuang
# Course: CIS 117 PythonProgramming
# Lab #3: The Web and Search
# Application: Program that will take the URL of the National Academy of Science 
# and a list of topics and count how many instances of each topic
# Description: The code accesses the HTML, calculates the frequency of specific 
# words, and prints out how many times each topic has occured
# Input: Words from nasonline.org that match a topic from topic_list
# Requirements: Use case insensitive matches, use f-string to display report
# Output: How many times each topic has occured
# Development Environment: Ubuntu 17.0
# Version:  Python 3.7
# Solution File: CIS117_WarrenKuangLab3.py
# Date: 07/25/23

from datetime import date
import urllib.request
import re

def main():
    
    from urllib.request import urlopen
    from re import findall

    print ("Today's date is", date.today())

    #Access and validate HTML url
    try: 
        response = urlopen('http://www.nasonline.org/')
        html = response.read()
        html = html.decode()
    except Exception as e:
        print("URL is not accessessible")

    #List of topics
    topic_list = ["research", "climate", "evolution", "cultural", "leadership", \
                  "nation", "physical", "science", "biological", "Web", "engineer"]

    #Calculate the frequency of words
    def frequency(word_list):
        freq = {}  #Create an empty dictionary to store word frequencies

        for word in word_list:
            #Convert the word to lowercase
            word_lower = word.lower()

            #Find all occurrences of the word
            occurrences = re.findall(word_lower, html)

            #Store the occurrences in the dictionary for the word
            freq[word] = occurrences

        return freq

    #Calculate the frequency of each topic in the topic_list
    topic_freq = frequency(topic_list)

    #Print the count of occurrences for each topic
    for topic, freq in topic_freq.items():
        print(f"{topic} appears {len(freq)} times.")

main()

