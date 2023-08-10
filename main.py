#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
import ttkbootstrap as ttk
import tkinter.scrolledtext as tkscrolledtext
from tkinter import StringVar, Tk, Frame
from src.config import ConfigFile
from src.redirectIO import *

global entry_keywords
global conf
global prev_keywords_var
global redirectors


# Clear the list in the config file and the dropdown list
def clear_list():
    global entry_keywords
    conf.set(key='keywords_list', value='')
    conf.write()
    prev_keywords_var.set('')
    entry_keywords['values'] = []  # Clear the values from the combobox


def main():
    # Create UI
    root = ttk.Window(themename="sandstone")

    # Load settings
    global conf
    conf = ConfigFile()
    global entry_keywords
    global prev_keywords_var
    prev_keywords_var = StringVar()

    engine_list = []
    for i in search.Engine:
        engine_list.append(i.name)

    # Layout
    # Use saved geometry if available
    geometry = conf.get(key='geometry.main')
    if geometry is None:
        geometry = "800x700+100+100"  # default size
        root.geometry(geometry)
        root.title("Market Auto Search Tool -- Get news based on keywords")

    # Group 1
    # search engine: [Combobox]
    frame_engine = ttk.Frame(root, border=5)
    frame_engine.pack(side="top", fill="both", anchor="nw", padx=5, pady=(5, 0))

    label_engine = ttk.Label(frame_engine, text='Current search engine:', padding=5)
    label_engine.pack(side='left')

    # The dropdown list (Combobox) containing the previous engine names
    entry_engine = ttk.Combobox(frame_engine, values=engine_list, foreground='black')
    engine_name = conf.get(key='engine_name')
    if engine_name is None:
        engine_name = 'GOOGLE'

    if engine_name:  # if there is a current engine name
        entry_engine.set(engine_name)  # set it as the default value
    entry_engine.pack(side='left', fill='x', expand=True)

    # Group 2
    # search keywords: [Combobox] [x]
    frame_keywords = ttk.Frame(root, border=5)
    frame_keywords.pack(side="top", fill="both", anchor="nw", padx=5, pady=(5, 0))

    label_keywords = ttk.Label(frame_keywords, text='Keyword:', padding=5)
    label_keywords.pack(side='left')

    # Get the list of previous search history
    prev_keywords = conf.get(key='keywords_list')
    if prev_keywords is not None and prev_keywords.strip() != '':
        prev_keywords = prev_keywords.split(',')
    else:
        prev_keywords = []

    # The dropdown list (Combobox) containing the previous engine names
    entry_keywords = ttk.Combobox(frame_keywords, values=prev_keywords, foreground='black')
    keyword = conf.get(key='keyword')
    if keyword is None:
        keyword = ''

    if keyword:  # if there is a current engine name
        entry_keywords.set(keyword)  # set it as the default value
    entry_keywords.pack(side='left', fill='x', expand=True)

    # The clear button that clears the previous engine lists
    button_clear = ttk.Button(frame_keywords, text='x', padding=5, command=clear_list, bootstyle='danger-solid')
    button_clear.pack(side='left')
    frame_buttons = ttk.Frame(root, border=5)
    frame_buttons.pack(side="top", fill="both", anchor="nw", padx=5, pady=(5, 0))

    separator1 = ttk.Separator(frame_buttons, orient='horizontal')
    separator1.pack(side='top', fill='x', pady=5, expand=True)

    frame_nav = ttk.Frame(frame_buttons)
    frame_nav.pack(side="top", fill="both", padx=0, pady=8, anchor="nw")

    button_show = ttk.Button(frame_nav, text='Find & Sort', bootstyle='primary-solid')
    button_show.pack(side='left', ipadx=35, pady=5, expand=True)
    button_show['command'] = lambda: search_sort(entry_keywords.get(), navlist)

    # Group 6
    #    Text Output
    frame_text = ttk.Frame(root, border=5)
    frame_text.pack(side="top", fill="both", padx=0, pady=0, anchor="nw")
    scroll_text = tkscrolledtext.ScrolledText(frame_text, wrap='word', font=('Mono', 9))
    scroll_text.pack(side="top", fill="both", expand=True, ipadx=10, padx=2, pady=2)
    # Set the state to DISABLED to prevent user typing
    scroll_text.configure(state=DISABLED)

    # Redirect stdout and stderr to the Text widget
    global redirectors
    redirectors = {
        'stdout': StdoutRedirector(scroll_text),
        'stderr': StderrRedirector(scroll_text)
    }
    sys.stdout = redirectors['stdout']
    sys.stderr = redirectors['stderr']

    # Update the list of keywords in the Combobox
    def update_keywords():
        # Get the current list of keywords
        new_keywords = prev_keywords_var.get().split(',')

        # Update the values in the Combobox
        entry_keywords['values'] = new_keywords

    # Trace the StringVar to update the Combobox whenever it changes
    prev_keywords_var.trace('w', update_keywords)

    # Watch for changes to geometry
    def save_settings_geometry(event):
        conf.set(key='geometry.main', value=root.geometry())
        conf.write()

    root.bind("<Configure>", save_settings_geometry)

    root.mainloop()


if __name__ == '__main__':
    main()
