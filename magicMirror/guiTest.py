from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


if __name__ == '__main__':
    main()

#from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
#
# class Calculator:
#
#     def __init__(self, master):
#         self.master = master
#         master.title("Calculator")
#
#         self.total = 0
#         self.entered_number = 0
#
#         self.total_label_text = IntVar()
#         self.total_label_text.set(self.total)
#         self.total_label = Label(master, textvariable=self.total_label_text)
#
#         self.label = Label(master, text="Total:")
#
#         vcmd = master.register(self.validate) # we have to wrap the command
#         self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
#
#         self.add_button = Button(master, text="+", command=lambda: self.update("add"))
#         self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
#         self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
#
#         # LAYOUT
#
#         self.label.grid(row=0, column=0, sticky=W)
#         self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
#
#         self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
#
#         self.add_button.grid(row=2, column=0)
#         self.subtract_button.grid(row=2, column=1)
#         self.reset_button.grid(row=2, column=2, sticky=W+E)
#
#     def validate(self, new_text):
#         if not new_text: # the field is being cleared
#             self.entered_number = 0
#             return True
#
#         try:
#             self.entered_number = int(new_text)
#             return True
#         except ValueError:
#             return False
#
#     def update(self, method):
#         if method == "add":
#             self.total += self.entered_number
#         elif method == "subtract":
#             self.total -= self.entered_number
#         else: # reset
#             self.total = 0
#
#         self.total_label_text.set(self.total)
#         self.entry.delete(0, END)
#
# root = Tk()
# my_gui = Calculator(root)
# root.mainloop()

import tkinter as tk
import time

# def update_timeText():
#     # Get the current time, note you can change the format as you wish
#     current = time.strftime("%H:%M")
#     # Update the timeText Label box with the current time
#     timeText.configure(text=current)
#     # Call the update_timeText() function after 1 second
#     root.after(1000, update_timeText)
#
# root = tk.Tk()
# root.wm_title("Simple Clock Example")
#
# # Create a timeText Label (a text box)
# timeText = tk.Label(root, text="", font=("Helvetica", 150))
# timeText.pack()
# update_timeText()
# root.mainloop()

# import feedparser
#
# rss = 'http://feeds.bbci.co.uk/news/rss.xml?edition=uk'
# feed = feedparser.parse(rss)
# print(feed['entries'][0]['title'])

