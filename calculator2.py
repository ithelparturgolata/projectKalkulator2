"""calculator.py: Opis modułu
__name__ = "Calculator ver.2"
__author__ = "Artur Gołata"
__license__ = "MIT"
__version__ = "1.0"
__status__ = "production"
"""
from tkinter import *
import tkinter as tk
import requests
from tkinter import messagebox


class Calculator():
    """
    Nowsza wersja kalkulatora
    Przede wszystkim docstringsy
    dokumentacja modułu
    """
    def buttonClick(self, numbers):
        """
        Metoda buttonClick

        :param operator: pobiera operator działania
        :param number: pobiera liczby
        :returns: zawraca wartość klikniętego buttona
        :raises ZeroDivisionError:
        :raises ValueError:
        """
        global operator
        self.numbers = numbers
        self.operator = self.operator + str(self.numbers)
        self.textInput.set(self.operator)

    def buttonClearDisplay(self):
        """
        Metoda ClearDisplay

        :param operator:
        :param text: czyści okno wynikow
        :returns: czyści okno
        :raises ZeroDivisionError:
           :raises ValueError:
        """
        global operator
        self.operator = ""
        self.textInput.set("")

    def buttonEquals(self):
        """
        Metoda buttonEquals

        :param total: operator
        :param b: int dzielnik
        :returns: wynik
        :raises ZeroDivisionError:
           :raises ValueError:
        """
        global operator
        try:
            self.total = str(eval(self.operator))
        except ZeroDivisionError:
            messagebox.showwarning("Uwaga", "Nie dzielimy przez 0")
        self.textInput.set(self.total)
        self.operator = ""

    def __init__(self):
        """
        konstruktor
        oraz GUI
        """
        self.root = tk.Tk()
        self.root.geometry("250x250")
        self.root.title("Kalkulator ver.2")
        self.root.resizable(0,0)
        self.font = ("arial", 10, "bold")
        self.operator = ""
        self.textInput = StringVar()

        self.display = Entry(self.root, width = "22", textvariable = self.textInput, justify = "right", font = self.font)
        self.display.place(x = 40, y = 10)

        self.button7 = Button(self.root, text = "7", width = "4", height = "2", activebackground = "yellow", command = lambda:  self.buttonClick(7), font = self.font, anchor = "center")
        self.button7.place(x = 40, y = 40)

        self.button4 = Button(self.root, text = "4", width = "4", height = "2", activebackground = "yellow", command = lambda:self.buttonClick(4), font = self.font, anchor = "center")
        self.button4.place(x = 40, y = 80)

        self.button1 = Button(self.root, text = "1", width = "4", height = "2", activebackground = "yellow", command = lambda:self.buttonClick(1), font = self.font, anchor = "center")
        self.button1.place(x = 40, y = 120)

        self.buttonC = Button(self.root, text = "C", width = "4", height = "2", activebackground = "yellow", command = lambda: self.buttonClearDisplay(), font = self.font, anchor = "center")
        self.buttonC.place(x = 40, y = 160)

        self.button8 = Button(self.root, text = "8", width = "4", height = "2", activebackground = "yellow", command = lambda: self.buttonClick(8), font = self.font, anchor = "center")
        self.button8.place(x = 80, y = 40)

        self.button5 = Button(self.root, text = "5", width = "4", height = "2", activebackground = "yellow", command = lambda: self.buttonClick(4), font = self.font, anchor = "center")
        self.button5.place(x = 80, y = 80)

        self.button2 = Button(self.root, text = "2", width = "4", height = "2", activebackground = "yellow", command = lambda: self.buttonClick(2), font = self.font, anchor = "center")
        self.button2.place(x = 80, y = 120)

        self.button0 = Button(self.root, text = "0", width = "4", height = "2", activebackground = "yellow", command = lambda: self.buttonClick(0), font = self.font, anchor = "center")
        self.button0.place(x = 80, y = 160)

        self.button9 = Button(self.root, text = "9", width = "4", height = "2", activebackground = "yellow", command = lambda: self.buttonClick(9), font = self.font, anchor = "center")
        self.button9.place(x = 120, y = 40)

        self.button6 = Button(self.root, text = "6", width = "4", height = "2", activebackground = "yellow", command = lambda: self.buttonClick(6), font = self.font, anchor = "center")
        self.button6.place(x=120, y=80)

        self.button3 = Button(self.root, text = "3", width = "4", height = "2", activebackground = "yellow", font = self.font, anchor = "center", command = lambda: self.buttonClick(3))
        self.button3.place(x=120, y=120)

        self.buttonEqual = Button(self.root, text = "=", width = "4", height = "2", activebackground = "yellow", command = self.buttonEquals, font = self.font, anchor = "center")
        self.buttonEqual.place(x=120, y=160)

        self.buttonadd = Button(self.root, text = "+", width = "4", height = "2", activebackground = "yellow", command = lambda: self.buttonClick("+"), font = self.font, anchor = "center")
        self.buttonadd.place(x = 160, y = 40)

        self.buttonsub = Button(self.root, text = "-", width = "4", height = "2", activebackground = "yellow", command = lambda: self.buttonClick("-"), font = self.font, anchor = "center")
        self.buttonsub.place(x=160, y=80)

        self.buttonmul = Button(self.root, text = "*", width = "4", height = "2", activebackground = "yellow", command = lambda: self.buttonClick("*"), font = self.font, anchor = "center")
        self.buttonmul.place(x=160, y=120)

        self.buttondiv = Button(self.root, text = "/", width = "4", height = "2", activebackground = "yellow", command=lambda:self.buttonClick("/"), font = self.font, anchor = "center")
        self.buttondiv.place(x=160, y=160)


        self.root.mainloop()

if __name__ == '__main__':
    Calculator()
