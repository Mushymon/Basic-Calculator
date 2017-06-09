"""Basic Calculator by Calvin Liu"""
from __future__ import print_function
from Tkinter import *
import ttk
import math


class Calculator(object):
    """Calculator is the class defined to run the program"""

    # Stores the value to be used in a calculation
    calc_value = 0.0

    # Lets the program know which math button was previously pressed
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False
    pow_trigger = False

    def button_press(self, value):
        """Whenever a number or the decimal button is pressed"""

        # Get the current value in the entry
        entry_val = self.number_entry.get()

        # Concatenates the current value in the entry with the value of the button pressed
        entry_val += value

        # Clears the entry box
        self.number_entry.delete(0, "end")

        # Inserts new value into entry box
        self.number_entry.insert(0, entry_val)

    @staticmethod
    def isfloat(str_val):
        """Returns true if number is is a float;
        Returns false if number is not a float"""

        try:

            float(str_val)
            return True

        # Catches an exception if the value is not a float
        except ValueError:

            return False

    def math_button_press(self, value):
        """Whenever a math button is pressed, for example, / * - +"""

        if self.isfloat(str(self.number_entry.get())):

            # Cancels out previous math button presses
            self.add_trigger = False
            self.sub_trigger = False
            self.mult_trigger = False
            self.div_trigger = False
            self.pow_trigger = False

            # Get the value out of the entry box for the calculation
            self.calc_value = float(self.entry_value.get())

            # Set the math button presses so when the equal button is pressed
            # that function will know which calculation to use
            if value == "/":
                print("/ Pressed")
                self.div_trigger = True
            elif value == "*":
                print("* Pressed")
                self.mult_trigger = True
            elif value == "+":
                print("+ Pressed")
                self.add_trigger = True
            elif value == "-":
                print("- Pressed")
                self.sub_trigger = True
            else:
                print("^ Pressed")
                self.pow_trigger = True

            # Clears the entry box
            self.number_entry.delete(0, "end")

    def equal_button_press(self):
        """Whenever the equal button is pressed, it performs a mathematical operation by taking the
        value before the math button is pressed and the current value, then chooses the correct
        calculation to perform based on which was the last math button pressed"""

        # Make sure a math button was clicked
        if (self.add_trigger or self.sub_trigger or self.mult_trigger or
                self.div_trigger or self.pow_trigger):

            if self.add_trigger:

                solution = self.calc_value + float(self.entry_value.get())
                print(self.calc_value, "+", float(self.entry_value.get()), "=", solution)

            elif self.sub_trigger:

                solution = self.calc_value - float(self.entry_value.get())
                print(self.calc_value, "-", float(self.entry_value.get()), "=", solution)

            elif self.mult_trigger:

                solution = self.calc_value * float(self.entry_value.get())
                print(self.calc_value, "*", float(self.entry_value.get()), "=", solution)

            elif self.div_trigger:

                solution = self.calc_value / float(self.entry_value.get())
                print(self.calc_value, "/", float(self.entry_value.get()), "=", solution)
            else:

                solution = math.pow(self.calc_value, float(self.entry_value.get()))
                print(self.calc_value, "^", float(self.entry_value.get()), "=", solution)

            # Clear the entry box
            self.number_entry.delete(0, "end")

            # Inserts the solution into the entry box
            self.number_entry.insert(0, solution)

    def clear_button_press(self, clear_type):
        """Whenever the AC or DEL button is pressed"""

        if clear_type == 'DEL':

            # Get the current value in the entry
            entry_val = self.number_entry.get()

            # Removes the last character from the current value in the entry
            entry_val = entry_val[:-1]

            # Clear the entry box
            self.number_entry.delete(0, "end")

            # Insert the new value
            self.number_entry.insert(0, entry_val)

        else:

            # Cancels out previous math button presses
            self.add_trigger = False
            self.sub_trigger = False
            self.mult_trigger = False
            self.div_trigger = False
            self.pow_trigger = False

            # Clear the entry box
            self.number_entry.delete(0, "end")

    def negate_button_press(self):
        """Whenever the negate button is pressed (+/-)"""

        entry_val = self.number_entry.get()

        # Make sure that there is a current value in the entry
        if entry_val:

            # If there is a negative sign
            # This function gets rid of it to make the current value positive
            # Otherwise the function concatenates a negative sign and the current value in the entry
            if entry_val[0] == '-':

                entry_val = entry_val[1:]

            else:

                entry_val = '-' + entry_val

            # Clear the entry box
            self.number_entry.delete(0, "end")

            # Insert the new value
            self.number_entry.insert(0, entry_val)

    def __init__(self, root):

        # Will hold the changing value stored in the entry
        self.entry_value = StringVar(root, value="")

        # Define title for the app
        root.title("Calculator")

        # Defines the width and height of the window (can vary for different computers)
        root.geometry("596x294")

        # Stops resizing of the window
        root.resizable(width=False, height=False)

        # Customize the styling for the buttons and entry
        style = ttk.Style()

        style.configure("TButton", font="Serif 15", padding=10)
        style.configure("TEntry", font="Serif 18", padding=10)

        # Create the text entry box
        self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=95)
        self.number_entry.grid(row=0, columnspan=4)

        # ----- 1st Row of Buttons -----

        self.button7 = ttk.Button(
            root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)

        self.button8 = ttk.Button(
            root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)

        self.button9 = ttk.Button(
            root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)

        self.button_div = ttk.Button(
            root, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=3)

        # ----- 2nd Row of Buttons -----

        self.button4 = ttk.Button(
            root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)

        self.button5 = ttk.Button(
            root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)

        self.button6 = ttk.Button(
            root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)

        self.button_mult = ttk.Button(
            root, text="*", command=lambda: self.math_button_press('*')).grid(row=2, column=3)

        # ----- 3rd Row of Buttons -----

        self.button1 = ttk.Button(
            root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)

        self.button2 = ttk.Button(
            root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)

        self.button3 = ttk.Button(
            root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)

        self.button_sub = ttk.Button(
            root, text="-", command=lambda: self.math_button_press('-')).grid(row=3, column=3)

        # ----- 4th Row of Buttons -----

        self.button0 = ttk.Button(
            root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=0)

        self.button_dot = ttk.Button(
            root, text=".", command=lambda: self.button_press('.')).grid(row=4, column=1)

        self.button_negate = ttk.Button(
            root, text="+/-", command=lambda: self.negate_button_press()).grid(row=4, column=2)

        self.button_add = ttk.Button(
            root, text="+", command=lambda: self.math_button_press('+')).grid(row=4, column=3)

        # ----- 5th Row of Buttons ------

        self.button_all_clear = ttk.Button(
            root, text="AC", command=lambda: self.clear_button_press('AC')).grid(row=5, column=0)

        self.button_delete = ttk.Button(
            root, text="DEL", command=lambda: self.clear_button_press('DEL')).grid(row=5, column=1)

        self.button_power = ttk.Button(
            root, text=(u"X\u207F"), command=lambda: self.math_button_press('p')).grid(
                row=5, column=2)

        self.button_equal = ttk.Button(
            root, text="=", command=lambda: self.equal_button_press()).grid(row=5, column=3)

# Increases compatability with Linux
if __name__ == '__main__':

    # Get the root window object
    ROOT = Tk()

    # Create the calculator
    CALC = Calculator(ROOT)

    # Run the app until exited
    ROOT.mainloop()
