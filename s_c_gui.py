#!/usr/bin/env python3
# coding=utf-8

import tkinter as tk
from tkinter import ttk, Menu, Label, DISABLED, NORMAL, END
import sys

from server_client_wrapper import clientThread, serverThread
import functions
import rules
from CellAuto_Cryptography import Automaton


class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Send Secret Messages")
        self.info = tk.StringVar()
        self.createWidgets()
        self.protocol("WM_DELETE_WINDOW", self._quit)

    def recieve(self):
        self.server_thread = serverThread()
        recieved = self.server_thread.start()

    def send(self):
        automaton = Automaton()
        seed = automaton.seed
        ip = self.ip.get()
        print(type(seed))
        plaintext = self.plaintext.get()
        ciphertext = automaton.getCipherText(plaintext)
        l = []
        l.append("Sending data: ")
        l.append("(ciphertext " + ciphertext + ") ")
        l.append("(seed " + str(seed) + ") ")
        l.append("(destination_ip " + ip + ")")
        self.add_info(''.join(l))

        client_thread = clientThread(ip, ciphertext)
        client_thread.start()

    def createWidgets(self):
        """Make window, with all parts."""
        # Menu Bar
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Tab Bar
        tab_control = ttk.Notebook(self)

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

        info_box = ttk.Frame(send_tab, borderwidth=1)
        self.info_text = tk.Text(info_box, bg="grey")
        self.info_text.insert(
            END, "Welcome to cryptpgraphy with cellular automata!\n")
        self.info_text.config(state=DISABLED)
        self.info_text.grid(column=1, row=1)

        info_box.grid(column=2, row=1, rowspan=3)

        # Recieve tab
        recieve_button = ttk.Button(
            recieve_tab, text="Recieve", command=self.recieve)
        recieve_button.grid(column=1, row=1, rowspan=2)

    def _quit(self):
        """Exit script and close window."""
        self.quit()
        self.destroy()
        self.server_thread.stop()
        sys.exit(0)

    def add_info(self, info):
        """Add informational message to info box. Use instead of print().
        arguments: (str) info
        effects: add line with info printed to screen in info box"""

        self.info_text.config(state=NORMAL)
        info = "> " + str(info) + "\n"
        self.info_text.insert(END, info)
        self.info_text.config(state=DISABLED)


if __name__ == '__main__':
    app = Application()
    app.mainloop()
