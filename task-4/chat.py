import tkinter as tk
from tkinter import scrolledtext

# Define the get_response function
def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        response = "Hello! How can I assist you today?"
    elif "hi" in user_input:
        response = "Hi"
    elif "how are you" in user_input:
        response = "I'm a chatbot. I don't have feelings, but thanks for asking!"
    elif "bye" in user_input:
        response = "Goodbye! Have a great day!"
    elif "help" in user_input:
        response = "I'm here to help you. What do you need assistance with?"
    elif "name" in user_input:
        response = "My name is Chatbot. Nice to meet you!"
    elif "weather" in user_input:
        response = "I'm sorry, I don't have the ability to check the weather."
    elif "joke" in user_input:
        response = "Sure, here's a joke for you: Why don't scientists trust atoms? Because they make up everything!"
    elif "thank you" in user_input:
        response = "You're welcome! If you have any more questions, feel free to ask."
    else:
        response = "I'm sorry, I didn't understand that. Can you please rephrase?"

    return response

# Define the send_message function
def send_message():
    user_input = user_input_text.get("1.0", tk.END).strip()  
    chat_log_text.insert(tk.END, "User: " + user_input + "\n")
    chat_log_text.insert(tk.END, "Chatbot: " + get_response(user_input) + "\n")
    user_input_text.delete("1.0", tk.END)

# Create the main window
window = tk.Tk()
window.title("Chatbot")

# Create chat log and user input text widgets
chat_log_text = scrolledtext.ScrolledText(window, width=50, height=20)
chat_log_text.pack()

user_input_text = tk.Text(window, width=50, height=3)
user_input_text.pack()

# Create a send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Start the main event loop
window.mainloop()
