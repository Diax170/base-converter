import bases
from tkinter import *  # Import everything from tkinter
from tkinter import messagebox as msg


class Root(Tk):
    def __init__(self):
        super().__init__()  # Initialize tkinter
        self.title("Base converter")

        # Create frame for input fields (Entry)
        entryFrame = Frame(self)

        Label(entryFrame, text="Number:").grid(row=0, column=0)
        self.num = Entry(entryFrame)
        self.num.grid(row=0, column=1)

        Label(entryFrame, text="Start base:").grid(row=1, column=0)
        self.startBase = Entry(entryFrame)
        self.startBase.grid(row=1, column=1)

        Label(entryFrame, text="Base:").grid(row=2, column=0)
        self.base = Entry(entryFrame)
        self.base.grid(row=2, column=1)

        entryFrame.pack()

        resultFrame = Frame(self)

        # Create label with information about result and button to copy it
        self.resultLabel = Label(resultFrame, text="Result: None")
        self.resultLabel.grid()

        self.result = None  # Variable which result (not label) is stored in

        Button(resultFrame, text="Copy", command=self.copy).grid(row=0, column=1)

        resultFrame.pack()

        # Create new frame with action buttons
        buttonFrame = Frame(self)

        Button(buttonFrame, text="Calculate", command=self.calculate).grid()
        Button(buttonFrame, text="Swap", command=self.swap).grid(row=0, column=1)  # Swap start base and base
        Button(buttonFrame, text="Exit", command=self.destroy).grid(row=0, column=2)
        Button(buttonFrame, text="?", command=self.help, width=1, height=1).grid(row=0, column=3)

        buttonFrame.pack()

        self.after(50, self.setMinSize)

    def calculate(self):
        try:  # Try to calculate, if failed inform user about an error
            self.result = bases.to_base(self.num.get(), eval(self.startBase.get()), eval(self.base.get()))
            self.resultLabel.configure(text="Result: " + self.result)  # Update result label
        except Exception as e: msg.showerror("Failed to calculate", "Error: " + str(e))

    def help(self):
        try:
            # Read help from text file
            with open("help.txt", "r") as file:
                msg.showinfo("Help", "Reading from 'help.txt':\n\n" + file.read())
        except Exception as e: msg.showerror("Unable to fetch help", "Error: " + str(e))

    def copy(self):
        try:  # Try to copy result to clipboard, if failed inform user about an error
            self.clipboard_clear()
            self.clipboard_append(str(self.result))
            self.update()  # Update clipboard content
            msg.showinfo("Copied", "Result copied to clipboard!")
        except Exception as e: msg.showerror("Failed to copy result to clipboard", "Error: " + str(e))

    def swap(self):
        # Get Entry text
        startBase = self.startBase.get()
        base = self.base.get()

        # Delete Entry text
        self.startBase.delete(0, END)
        self.base.delete(0, END)

        # Swap values
        self.startBase.insert(0, base)
        self.base.insert(0, startBase)

    def setMinSize(self):
        self.minsize(width=300, height=self.winfo_height())


root = Root()
root.mainloop()
