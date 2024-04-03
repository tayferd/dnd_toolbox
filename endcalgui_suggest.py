import tkinter as tk
from tkinter import ttk, scrolledtext
import requests

def send_request():
    # Read values from the GUI
    party_level = party_level_entry.get()
    num_players = num_players_entry.get()
    difficulty = difficulty_combobox.get()

    # Prepare data for the POST request
    data = {
        "party_level": party_level,
        "num_players": num_players,
        "difficulty": difficulty
    }

    # Send POST request
    response = requests.post(url, json=data)
    response_data = response.json()

    # Check if the response includes an error
    if 'error' in response_data:
        response_text = f"Error: {response_data['error']}"
    else:
        total_xp = response_data.get('total_xp', 'No XP calculated')
        suggestions = response_data.get('suggestions', [])
        suggestion_text = ', '.join(suggestions)
        response_text = f"Total XP: {total_xp}\nSuggestions: {suggestion_text}"

    # Display response
    response_text_area.config(state=tk.NORMAL)  # Enable editing of text area
    response_text_area.delete('1.0', tk.END)  # Clear the text area
    response_text_area.insert(tk.END, response_text)  # Insert new response text
    response_text_area.config(state=tk.DISABLED)  # Disable editing of text area

# Setup Tkinter window
window = tk.Tk()
window.title("D&D Encounter XP Calculator")

# URL of the Flask API
url = 'http://127.0.0.1:5000/calculate_xp'

# Create and place the input fields
tk.Label(window, text="Party Level:").grid(row=0, column=0)
party_level_entry = tk.Entry(window)
party_level_entry.grid(row=0, column=1)

tk.Label(window, text="Number of Players:").grid(row=1, column=0)
num_players_entry = tk.Entry(window)
num_players_entry.grid(row=1, column=1)

tk.Label(window, text="Difficulty:").grid(row=2, column=0)
difficulty_combobox = ttk.Combobox(window, values=["easy", "medium", "hard", "deadly"])
difficulty_combobox.grid(row=2, column=1)

# Send request button
send_request_button = tk.Button(window, text="Calculate XP", command=send_request)
send_request_button.grid(row=3, column=0, columnspan=2)

# Text area to display the response
response_text_area = scrolledtext.ScrolledText(window, width=40, height=10, wrap=tk.WORD, state=tk.DISABLED)
response_text_area.grid(row=4, column=0, columnspan=2)

window.mainloop()
