import customtkinter as ctk
from tkinter import messagebox

# --- Appearance ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- Caesar Cipher Function ---
def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                shifted = (ord(char) - base + shift) % 26
            else:
                shifted = (ord(char) - base - shift) % 26

            result += chr(base + shifted)
        else:
            result += char

    return result


# --- Button Functions ---
def encrypt_text():
    try:
        text = input_box.get("1.0", "end").strip()
        shift = int(shift_entry.get())

        result = caesar_cipher(text, shift, "encrypt")
        output_box.delete("1.0", "end")
        output_box.insert("end", result)

    except ValueError:
        messagebox.showerror("Error", "Shift must be a number!")


def decrypt_text():
    try:
        text = input_box.get("1.0", "end").strip()
        shift = int(shift_entry.get())

        result = caesar_cipher(text, shift, "decrypt")
        output_box.delete("1.0", "end")
        output_box.insert("end", result)

    except ValueError:
        messagebox.showerror("Error", "Shift must be a number!")


# --- App Window ---
app = ctk.CTk()
app.title("Caesar Cipher Tool")
app.geometry("600x520")

# --- Title ---
title = ctk.CTkLabel(
    app,
    text="🔐 Caesar Cipher Tool",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)

# --- Input Label ---
ctk.CTkLabel(app, text="Enter Message:", font=("Arial", 13)).pack()

# --- Input Box ---
input_box = ctk.CTkTextbox(
    app,
    width=520,
    height=110,
    corner_radius=10
)
input_box.pack(pady=10)

# --- Shift Input ---
ctk.CTkLabel(app, text="Shift Value:", font=("Arial", 13)).pack(pady=5)

shift_entry = ctk.CTkEntry(
    app,
    width=200,
    height=35,
    justify="center",
    placeholder_text="Enter shift (e.g. 3)"
)
shift_entry.pack(pady=5)

# --- Buttons ---
button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=20)

encrypt_btn = ctk.CTkButton(
    button_frame,
    text="🔒 Encrypt",
    width=160,
    height=45,
    font=("Arial", 14, "bold"),
    fg_color="#00c853",      # green
    hover_color="#009624",
    corner_radius=12,
    command=encrypt_text
)

decrypt_btn = ctk.CTkButton(
    button_frame,
    text="🔓 Decrypt",
    width=160,
    height=45,
    font=("Arial", 14, "bold"),
    fg_color="#d50000",      # red
    hover_color="#9b0000",
    corner_radius=12,
    command=decrypt_text
)

encrypt_btn.grid(row=0, column=0, padx=20)
decrypt_btn.grid(row=0, column=1, padx=20)

# --- Output Label ---
ctk.CTkLabel(app, text="Result:", font=("Arial", 13)).pack()

# --- Output Box ---
output_box = ctk.CTkTextbox(
    app,
    width=520,
    height=110,
    corner_radius=10
)
output_box.pack(pady=10)

# --- Run ---
app.mainloop()