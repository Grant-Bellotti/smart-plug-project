import tkinter as tk

# Simulate a plug's state (ON/OFF)
plug_status = {"Plug 1": False, "Plug 2": False}

# Toggle plug function
def toggle_plug(plug_name):
    plug_status[plug_name] = not plug_status[plug_name]
    button_text = f"{plug_name} is {'ON' if plug_status[plug_name] else 'OFF'}"
    buttons[plug_name].config(text=button_text)

# Initialize main window
root = tk.Tk()
root.title("Smart Plug Controller")
root.geometry("300x200")
root.configure(bg="black")  # Set background to black

# Create a dictionary to store button references
buttons = {}

# Sample plugs (add more plugs as needed)
plug_names = ["Plug 1", "Plug 2"]

# Define button styles
button_style = {
    "bg": "#333333",        # Dark gray background for buttons
    "fg": "white",          # White text for contrast
    "activebackground": "#555555",  # Lighter gray on hover/active
    "font": ("Helvetica", 14),      # Modern font and size
    "relief": "flat",       # Flat button style for modern feel
    "width": 20,            # Button width
    "pady": 10              # Padding inside the button
}

# Create buttons for each plug
for i, plug_name in enumerate(plug_names):
    # Toggle button with modern style
    button = tk.Button(root, text=f"{plug_name} is OFF", **button_style, command=lambda name=plug_name: toggle_plug(name))
    button.pack(pady=10)  # Add spacing between buttons
    
    # Store button reference
    buttons[plug_name] = button

# Start the Tkinter event loop
root.mainloop()
