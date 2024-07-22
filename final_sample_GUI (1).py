from building_new_fit_latest import genetic_algorithm
import threading
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

content=""
# Function to be called when the 'Open File' button is clicked
def open_file():
    global content
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_area.delete(1.0, tk.END)  # Clear previous content
            text_area.insert(tk.END, content)



# Function to be called when the 'Call External Script' button is clicked
def call_external_script():
    global content
    #original_text =""
    """
    with open("inp.txt") as file:
        original_text = file.read()

    """
    
    # Define a function to run the genetic_algorithm in a separate thread
    def run_genetic_algorithm():
        if content.strip():
            oo = genetic_algorithm(content,"english")
            # Clear previous content in text_area2
            text_area2.delete(1.0, tk.END)
            # Update the GUI with the output of the external script
            text_area2.insert(tk.END, oo)
            # Change the button text to "Resummarize"
            call_script_button.config(text="Re-Summarize")
        else:
            # If the content is empty, show an error message
            text_area2.delete(1.0, tk.END)
            text_area2.insert(tk.END, "Error: Empty input text. Please select a file with meaningful content.")
    
    # Start a new thread to run the genetic_algorithm function
    thread = threading.Thread(target=run_genetic_algorithm)
    thread.start()

    # You can also optionally update the GUI to show that the script is running
    text_area2.delete(1.0, tk.END)
    text_area2.insert(tk.END, "Running external script...")




"""
# Function to be called when the 'Call External Script' button is clicked
def call_external_script():
    original_text = ""
    with open("inp.txt") as file:
        original_text = file.read()
    
    # Define a function to run the genetic_algorithm in a separate thread
    def run_genetic_algorithm():
        oo = genetic_algorithm(original_text)
        # Clear previous content in text_area2
        text_area2.delete(1.0, tk.END)
        # Update the GUI with the output of the external script
        text_area2.insert(tk.END, oo)
    
    # Start a new thread to run the genetic_algorithm function
    thread = threading.Thread(target=run_genetic_algorithm)
    thread.start()

    # You can also optionally update the GUI to show that the script is running
    text_area2.delete(1.0, tk.END)
    text_area2.insert(tk.END, "Running external script...")


# Function to be called when the 'Call External Script' button is clicked
def call_external_script():
    original_text = ""
    with open("inp.txt") as file:
        original_text = file.read()
    
    # Define a function to run the genetic_algorithm in a separate thread
    def run_genetic_algorithm():
        oo = genetic_algorithm(original_text)
        # Update the GUI with the output of the external script
        root.after(0, lambda: text_area2.insert(tk.END, oo))
    
    # Start a new thread to run the genetic_algorithm function
    thread = threading.Thread(target=run_genetic_algorithm)
    thread.start()

    # You can also optionally update the GUI to show that the script is running
    text_area2.delete(1.0, tk.END)
    text_area2.insert(tk.END, "Running external script...")
"""



# Create the main application window
root = tk.Tk()
root.title("File Reader")
root.geometry("600x400")  # Set window size

# Center the window on the screen
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Create a frame for organization with a scrollbar
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(main_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text widget with scrollbar for the main frame
text_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, bg="lightgray", fg="black", width=20, height=5)
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, padx=10, pady=10)

# Create the 'Open File' button with rounded edges and light grey color
open_file_button = tk.Button(button_frame, text="upload", command=open_file, bg="lightblue", fg="black", relief=tk.RAISED, bd=2, padx=10, pady=5)
open_file_button.pack(side=tk.TOP, anchor=tk.NW)

# Create a text widget with scrollbar for external script output
text_area2 = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, bg="lightgray", fg="black", width=20, height=5)
text_area2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create the 'Call External Script' button at the bottom of the 'Open File' button
call_script_button = tk.Button(button_frame, text="summarize", command=call_external_script, bg="lightgreen", fg="black", relief=tk.RAISED, bd=2, padx=10, pady=5)
call_script_button.pack(side=tk.TOP, anchor=tk.NW)

# Run the main event loop
root.mainloop()
