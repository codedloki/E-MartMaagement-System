# --- START OF FILE Otptake.py ---

import tkinter as tk
from tkinter import ttk, messagebox
import pyotp
from StoreManagement import StoreManagementSystem
from tkinter import *


class OTPWindow:
    def __init__(self, root_to_replace, secret_key, callback_on_success): # Added callback_on_success
        self.root_to_replace = root_to_replace # This is the main Tkinter root window
        self.secret_key_data = secret_key # Store the secret key from login
        self.callback_on_success = callback_on_success # Store the callback function

        self.otp_toplevel = tk.Toplevel(root_to_replace) # Create a Toplevel for the OTP window
        self.otp_toplevel.title("OTP Verification")
        self.otp_toplevel.geometry("400x300")
        self.otp_toplevel.configure(bg="#1e1e2f")

        # ====== Title ======
        title = tk.Label(
            self.otp_toplevel, # Use otp_toplevel here
            text="Enter OTP",
            font=("Segoe UI", 18, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        title.pack(pady=20)

        # ====== Instruction ======
        instruction = tk.Label(
            self.otp_toplevel, # Use otp_toplevel here
            text=f"We have sent an OTP to your registered email/phone",
            font=("Segoe UI", 10),
            bg="#1e1e2f",
            fg="gray"
        )
        instruction.pack(pady=5)

        # ====== OTP Entry Boxes ======
        self.otp_vars = [tk.StringVar() for _ in range(6)]
        otp_frame = tk.Frame(self.otp_toplevel, bg="#1e1e2f") # Use otp_toplevel here
        otp_frame.pack(pady=20)

        self.otp_entries = []
        for i in range(6):
            entry = ttk.Entry(
                otp_frame,
                textvariable=self.otp_vars[i],
                font=("Segoe UI", 18, "bold"),
                width=2,
                justify="center"
            )
            entry.grid(row=0, column=i, padx=5)
            entry.bind("<KeyRelease>", lambda e, idx=i: self.focus_next(e, idx))
            self.otp_entries.append(entry)

        self.otp_entries[0].focus()

        # ====== Verify Button ======
        verify_btn = ttk.Button(
            self.otp_toplevel, # Use otp_toplevel here
            text="Verify OTP",
            command=self.verify_otp
        )
        verify_btn.pack(pady=20)

        # ====== Resend ======
        resend = tk.Label(
            self.otp_toplevel, # Use otp_toplevel here
            text="Resend OTP",
            font=("Segoe UI", 10, "underline"),
            bg="#1e1e2f",
            fg="#4cc9f0",
            cursor="hand2"
        )
        resend.pack()
        resend.bind("<Button-1>", lambda e: messagebox.showinfo("Resend", "OTP Resent Successfully!"))

        # ====== Style ======
        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 12), padding=6)

    def focus_next(self, event, idx):
        if len(self.otp_vars[idx].get()) == 1 and idx < 5:
            self.otp_entries[idx + 1].focus()

    def verify_otp(self):
        otp = "".join([var.get() for var in self.otp_vars])
        totp = pyotp.TOTP(self.secret_key_data)
        print(f"Generated OTP (for comparison): {totp.now()}") # For debugging
        print(f"Entered OTP: {otp}") # For debugging
        print(f"OTP verification result: {totp.verify(otp)}") # For debugging

        if totp.verify(otp):
            messagebox.showinfo("Success", "OTP Verified Successfully!")
            self.otp_toplevel.destroy() # Close the OTP Toplevel window
            self.callback_on_success() # Execute the callback function
        else:
            messagebox.showerror("Error", "Invalid OTP! Try again.")

# --- END OF FILE Otptake.py ---