#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.scrolledtext as tkscrolledtext
from tkinter import StringVar, Tk, Frame
from src.config import ConfigFile

def main():
    # Create UI
    root = ttk.Window(themename="sandstone")
    # Create the StringVar
    global prev_ips_var
    prev_ips_var = StringVar()

    # Load settings
    global conf
    global entry_ip
    global entry_device
    conf = ConfigFile()

    # Layout
    # Use saved geometry if available
    geometry = conf.get(key='geometry.main')
    #if geometry == None:
    geometry = "550x700+100+100" # default size
    root.geometry(geometry)
    root.title("Market Auto Search Tool")

    engineName = conf.get(key='engineName')
    if engineName is None:
        engineName = ''

    # Group 1
    #   search engine: [Combobox] [x]
    frame_engine = ttk.Frame(root, border=5)
    frame_engine.pack(side="top",fill="both",anchor="nw", padx=5, pady=(5,0))
    
    label_engine = ttk.Label(frame_engine, text='Current search engine:', padding=5)
    label_engine.pack(side='left')

    # Get the list of previous engine names
    prev_engine = conf.get(key='engine_list')
    if prev_engine is not None and prev_engine.strip() != '':
        prev_engine = prev_engine.split(',')
    else:
        prev_engine = []
    # The dropdown list (Combobox) containing the previous engine names
    entry_engine = ttk.Combobox(frame_engine, values=prev_engine)
    if engineName:  # if there is a current engine name
        entry_engine.set(engineName)  # set it as the default value
    entry_ip.pack(side='left', fill='x', expand=True)

    # The clear button that clears the previous IP addresses
    button_clear = ttk.Button(frame_engine, text='x', padding=5, command=clear_engine, bootstyle='danger-solid')
    button_clear.pack(side='left')
    frame_buttons = ttk.Frame(root, border=5)
    frame_buttons.pack(side="top",fill="both",anchor="nw", padx=5, pady=(5,0))

    separator1 = ttk.Separator(frame_buttons, orient='horizontal')
    separator1.pack(side='top', fill='x', pady=5, expand=True)

    #button_show = ttk.Button(frame_buttons, text='Show Printer UI', bootstyle='primary-solid')
    #button_show.pack(side='top', padx=15, pady=5, fill='both')

    frame_nav = ttk.Frame(frame_buttons)
    frame_nav.pack(side="top",fill="both", padx=0, pady=8, anchor="nw")

    button_show = ttk.Button(frame_nav, text='Show Printer UI', bootstyle='primary-solid')
    button_show.pack(side='left', ipadx=35, pady=5, expand=True)
    button_home = ttk.Button(frame_nav, text='Home', command=lambda: ui_go('HOME', entry_ip.get(), button_home), bootstyle='primary-solid')
    button_home.pack(side='left', ipadx=15, expand=True)
    button_back = ttk.Button(frame_nav, text='Back', command=lambda: ui_go('BACK', entry_ip.get(), button_back), bootstyle='primary-solid')
    button_back.pack(side='left', ipadx=15, expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()