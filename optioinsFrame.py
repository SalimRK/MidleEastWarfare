import customtkinter as ctk


class OptionsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.button = ctk.CTkButton(self, command=self.button_click)
        self.button.pack()

    # add methods to app
    def button_click(self):
        print("button click")