import customtkinter as ctk
import optioinsFrame
import mapFrame

height = 610
width = 800


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{width}x{height}")
        self.title("Middle East Warfare")

        self.options_frame = optioinsFrame.OptionsFrame(self, width=260, height=590)
        self.options_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.options_frame = mapFrame.MapFrame(self, width=620, height=590)
        self.options_frame.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")


app = App()
app.mainloop()
