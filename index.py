import tkinter as tk
from tkinter import scrolledtext, messagebox
import datetime
import nltk
from nltk.chat.util import Chat, reflections

# Ensure nltk data is downloaded
nltk.download('punkt')

# Simple patterns for chatbot responses
pairs = [
    (r'hi|hello|hey', ['or bhai!', 'kya haal!', 'he he!']),
    (r'how are you(.*)', ['I\'m a bot, but I\'m doing well!', 'Doing great! How can I assist you?']),
    (r'what is your name(.*)', ['I am a sophisticated chatbot.', 'You can call me ChatBot!']),
    (r'bye|exit', ['Goodbye!', 'See you later!', 'Take care!']),
    (r'(.*)', ['I don\'t understand that. Can you please rephrase?', 'Could you say that differently?'])
]

chatbot = Chat(pairs, reflections)

# Get response from the chatbot
def get_response(user_input):
    return chatbot.respond(user_input)

# Send Message Function
def send_message():
    user_input = user_entry.get()
    if user_input.strip():
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "You: " + user_input + "\n")
        response = get_response(user_input)
        chat_area.insert(tk.END, "Bot: " + response + "\n\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)
        user_entry.delete(0, tk.END)
        log_conversation(user_input, response)

# Log conversation to a file
def log_conversation(user_input, response):
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - You: {user_input}\n")
        log_file.write(f"{datetime.datetime.now()} - Bot: {response}\n")

# Clear Chat Area
def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete(1.0, tk.END)
    chat_area.config(state=tk.DISABLED)

# Show About Information
def show_about():
    messagebox.showinfo("About", "Chatbot Application\nVersion 1.0\nDeveloped by Aman")

# Create the GUI
root = tk.Tk()
root.title("Chatbot")

# Create Menu
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Clear Chat", command=clear_chat)
file_menu.add_command(label="Exit", command=root.quit)
help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

# Chat Frame
chat_frame = tk.Frame(root)
chat_frame.pack(padx=10, pady=10)

chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=60, height=20, state=tk.DISABLED)
chat_area.pack()

# User Entry Frame
user_entry_frame = tk.Frame(root)
user_entry_frame.pack(padx=10, pady=5, side=tk.BOTTOM, fill=tk.X)

user_entry = tk.Entry(user_entry_frame, width=50)
user_entry.pack(padx=10, pady=5, side=tk.LEFT, expand=True, fill=tk.X)

send_button = tk.Button(user_entry_frame, text="Send", command=send_message)
send_button.pack(padx=10, pady=5, side=tk.RIGHT)

root.bind('<Return>', lambda event: send_message())

# Run the GUI main loop
root.mainloop()