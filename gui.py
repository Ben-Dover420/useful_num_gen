import tkinter as tk
import sv_ttk
from tkinter import ttk, font, messagebox
from num_gen import number_generator
from check_string_func import check_string


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Frontend of GUI
        self.title("Number Generator")
        self.geometry("600x280")
        self.iconbitmap("dice.ico")

        self.fontFamilyH1 = font.Font(size = 40)
        self.fontFamilyH2 = font.Font(size = 25)
        self.fontFamilyH3 = font.Font(size = 15)

        self.appLabel = ttk.Label(self, text = "Number Generator", font = self.fontFamilyH1)        

        # Input fields
        self.inputFrame = ttk.Frame(self, style = 'styledFrame.TFrame')

        self.startValue = tk.StringVar()
        self.startEntry = ttk.Entry(self.inputFrame, textvariable = self.startValue, width = 5, font = self.fontFamilyH2)
        self.startLabel = ttk.Label(self.inputFrame, text = "Start value:", font = self.fontFamilyH2)

        self.endValue = tk.StringVar()
        self.endEntry = ttk.Entry(self.inputFrame, textvariable = self.endValue, width = 5, font = self.fontFamilyH2)
        self.endLabel = ttk.Label(self.inputFrame, text = "End value:", font = self.fontFamilyH2)

        # Generate button
        self.generateButton = ttk.Button(self, text = "Generate", style = 'Accent.TButton', width = 15, command = self.buttonAction) 
        
        # Displays widgets to GUI
        self.appLabel.pack(pady = "15")
        self.inputFrame.pack()
        self.startLabel.grid(column = 0, row = 0)
        self.startEntry.grid(column = 1, row = 0, padx = 2)
        self.endLabel.grid(column = 0, row = 1)
        self.endEntry.grid(column = 1, row = 1)
        self.generateButton.pack(pady = "25")

    def buttonAction(self):
        if not self.startValue.get() or not self.endValue.get(): # Checks if there are any values in startvalue and endvalue
            messagebox.showerror(title = "No value(s)", message = "Please input value(s) for start value and end value.")
            return
        
        if not check_string(self.startValue.get()) or not check_string(self.endValue.get()): # Checks if start value and end value are integers
            messagebox.showerror(title = "Non-integer value(s)", message = "Start value and end value have to be a number, please try again.")
            return
            
        if int(self.startValue.get()) >= int(self.endValue.get()): # Checks if start value is greater than end value
            messagebox.showerror(title = "Invalid intervall", message = "End value has to be greater than start value, please try again.")
            return
            
        numbers = number_generator(int(self.startValue.get()), int(self.endValue.get())) # Initiates when every condition is met
        
        for number in range(len(numbers)):
            messagebox.showinfo(title = "Random numbers", message = f"Random number ({number + 1}): {numbers[number]}")

if __name__ == "__main__":
    root = Application()
    sv_ttk.set_theme("dark")
    root.mainloop()
