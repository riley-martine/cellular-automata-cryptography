#!/usr/bin/env python3
# coding=utf-8

import server_client_wrapper
import tkinter as tk
from tkinter import ttk, Menu, Label
import sys

class Application(object):
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Send Secret Messages")
        self.createWidgets()


    def createWidgets(self):
        # Menu Bar
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Tab Bar
        tab_control = ttk.Notebook(self.win)

        send_tab = ttk.Frame(tab_control)
        tab_control.add(send_tab, text='Send Message')

        recieve_tab = ttk.Frame(tab_control)
        tab_control.add(recieve_tab, text='Recieve Message')

        tab_control.pack(expand=1, fill="both")

        # Send Tab
        plaintext_frame = ttk.Frame(send_tab)
        plaintext_box_label = ttk.Label(plaintext_frame, text="Plaintext: ")
        plaintext_box_label.grid(column=1, row=1)

        self.plaintext = tk.StringVar()
        plaintext_box = ttk.Entry(plaintext_frame, width=20,
            textvariable=self.plaintext)
        plaintext_box.grid(column=1, row=2)
        plaintext_frame.grid(column=1, row=1)

        ip_frame = ttk.Frame(send_tab)
        ip_box_label = ttk.Label(ip_frame, text="Destination IP: ")
        ip_box_label.grid(column=1, row=1)

        self.ip = tk.StringVar()
        ip_box = ttk.Entry(ip_frame, width=20,
            textvariable=self.ip)
        ip_box.grid(column=1, row=2)
        ip_frame.grid(column=1, row=2)

        send_button = ttk.Button(send_tab, text="Send", command=self.send)
        send_button.grid(column=1, row=3)

        info_box = tk.Canvas(send_tab, bg="grey")

        info_box.grid(column=3, row=1, rowspan=3)

    def _quit(self):
        """Exit script and close window."""
        self.win.quit()
        self.win.destroy()
        sys.exit(0)

    def send(self):
        print("Sending data: \"" + self.plaintext.get() + "\"")
        print("Sending seed: \"" + self.seed.get() + "\"")




if __name__ == '__main__':
    app = Application()
    app.win.mainloop()
