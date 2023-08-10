from ttkbootstrap.constants import *


class IORedirector(object):
    # A general class for redirecting I/O
    def __init__(self, text_area):
        self.text_area = text_area


# Redirects stdout
class StdoutRedirector(IORedirector):
    def write(self, string):
        self.text_area.configure(state=NORMAL)
        self.text_area.insert(END, string)
        self.text_area.see(END)
        self.text_area.configure(state=DISABLED)


# Redirects stderr
class StderrRedirector(IORedirector):
    def write(self, string):
        self.text_area.configure(state=NORMAL)
        self.text_area.insert(END, string)
        self.text_area.see(END)
        self.text_area.configure(state=DISABLED)
