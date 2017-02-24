#!/usr/bin/env python3
"""GUI for cellular automata cryptographic messaging."""

import tkinter as tk
from tkinter import ttk, DISABLED, NORMAL, END
import sys
import os

from server_client_wrapper import ClientThread, ServerThread
from CellAuto_Cryptography import Automaton


class CryptoGUI(tk.Tk):
    """GUI for sending and recieving messages securely via CAs."""
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Send Secret Messages")
        self.info = tk.StringVar()
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self._quit)

        # If .buf exists, clear it.
        with open('.buf', 'w'):
            pass
        # Set stdout to output to .buf
        # This allows us to display a virtual terminal
        # that intercepts print(info) statements from imported classes
        sys.stdout = open(".buf", 'a')

        # Check and refresh buf -- see function for details
        self.read_std_out()

    def receive(self):
        """Prepare for reception of data."""
        server_thread = ServerThread(self.receive_key.get())
        server_thread.start()

    def send_data(self):
        """Send ciphered(plaintext, key) to ip."""
        key = [int(k) for k in self.send_key.get()]
        automaton = Automaton(key=key)
        destination_ip = self.destination_ip.get()
        plaintext = self.plaintext.get()
        try:
            ciphertext = automaton.getCipherText(plaintext)
        except IndexError as _:
            print("No message entered. Sending \"Hello, World\"")
            ciphertext = automaton.getCipherText("Hello, World")

        info = ("Sending data: " + "(ciphertext " +
                ciphertext + ") " + "(destination_ip " + destination_ip + ")")
        self.add_info(info)

        client_thread = ClientThread(destination_ip, ciphertext)
        client_thread.start()

    def create_widgets(self):
        """Make window, with all parts."""

        plaintext_frame = ttk.Frame(self)
        plaintext_box_label = ttk.Label(plaintext_frame, text="Plaintext: ")
        plaintext_box_label.grid(column=1, row=1)

        self.plaintext = tk.StringVar()
        plaintext_box = ttk.Entry(plaintext_frame, width=20,
                                  textvariable=self.plaintext)
        plaintext_box.grid(column=1, row=2)
        plaintext_frame.grid(column=1, row=1)

        send_key_frame = ttk.Frame(self)
        send_key_label = ttk.Label(send_key_frame, text="Key: ")
        send_key_label.grid(column=1, row=1)

        self.send_key = tk.StringVar()
        send_key_box = ttk.Entry(send_key_frame, width=20,
                                 textvariable=self.send_key)
        send_key_box.grid(column=1, row=2)
        send_key_frame.grid(column=1, row=2)

        ip_frame = ttk.Frame(self)
        ip_box_label = ttk.Label(ip_frame, text="Destination IP: ")
        ip_box_label.grid(column=1, row=1)

        self.destination_ip = tk.StringVar()
        ip_box = ttk.Entry(ip_frame, width=20,
                           textvariable=self.destination_ip)
        ip_box.grid(column=1, row=2)
        ip_frame.grid(column=1, row=3)

        send_button = ttk.Button(self, text="Send", command=self.send_data)
        send_button.grid(column=1, row=4)

        info_box = ttk.Frame(self, borderwidth=1)
        self.info_text = tk.Text(info_box, bg="grey")

        self.info_text.insert(
            END, "Welcome to cryptpgraphy with cellular automata!\n")
        self.info_text.config(state=DISABLED)
        self.info_text.grid(column=1, row=1)

        info_box.grid(column=2, row=1, rowspan=7)

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(
            column=1, row=5, sticky="ew")

        receive_key_frame = ttk.Frame(self)
        receive_key_label = ttk.Label(receive_key_frame, text="Key: ")
        receive_key_label.grid(column=1, row=1)

        self.receive_key = tk.StringVar()
        receive_key_box = ttk.Entry(receive_key_frame, width=20,
                                    textvariable=self.receive_key)
        receive_key_box.grid(column=1, row=2)
        receive_key_frame.grid(column=1, row=6)

        receive_button = ttk.Button(
            self, text="Receive", command=self.receive)
        receive_button.grid(column=1, row=7)

    def _quit(self):
        """Exit script and close window."""
        self.quit()
        self.destroy()
        # self.server_thread.stop()
        os.remove('.buf')
        sys.exit(0)

    def add_info(self, info):
        """Add informational message to info box. Use instead of print().
        arguments: (str) info
        effects: add line with info printed to screen in info box"""

        self.info_text.config(state=NORMAL)
        info = "> " + str(info) + "\n"
        self.info_text.insert(END, info)
        self.info_text.see(END)
        self.info_text.config(state=DISABLED)

    def read_std_out(self):
        """Put stdout messages into the info_box. Called once, auto-refreshes"""

        sys.stdout.flush()  # Force write
        with open('.buf', 'r') as buf:
            read = buf.read()
            if read:  # Do not write if empty
                self.add_info(read)
        with open('.buf', 'w'):
            pass  # Clear file

        sys.stdout = open(".buf", 'a')
        self.after(1000, self.read_std_out)  # Call this again soon


if __name__ == '__main__':
    CRYPTO_GUI = CryptoGUI()
    CRYPTO_GUI.mainloop()
