import customtkinter as ctk


class MapTypeFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        zoom_slider = ctk.CTkSlider(self, from_=0, to=20, command=self.slide_zoom)
        zoom_slider.pack()

        option_menu = ctk.CTkOptionMenu(self, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                        command=self.option_menu_callback)
        option_menu.set("OpenStreetMap")

        option_menu.pack()

    def option_menu_callback(self, choice):
        if choice == "OpenStreetMap":
            self.master.master.map_frame.change_map("OpenStreetMap")
        elif choice == "Google normal":
            self.master.master.map_frame.change_map("Google normal")
        elif choice == "Google satellite":
            self.master.master.map_frame.change_map("Google satellite")

    def slide_zoom(self, value):
        value = int(value)
        self.master.master.map_frame.map_widget.set_zoom(value)


class SearchFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.Latitude_text = ctk.CTkLabel(self, text="Latitude:")
        self.Longitude_text = ctk.CTkLabel(self, text="Longitude:")

        self.Latitude_entry = ctk.CTkEntry(self, placeholder_text="Latitude")
        self.Longitude_entry = ctk.CTkEntry(self, placeholder_text="Longitude")
        self.search_button = ctk.CTkButton(self, text="Search", command=self.button_event)

        self.Latitude_text.grid(row=0, column=0)
        self.Longitude_text.grid(row=0, column=1)

        self.Latitude_entry.grid(row=1, column=0, pady=10, padx=10)
        self.Longitude_entry.grid(row=1, column=1, pady=10, padx=10)
        self.search_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

    def button_event(self):
        try:
            Latitude = self.Latitude_entry.get()
            Longitude = self.Longitude_entry.get()
            self.master.master.map_frame.map_widget.set_position(float(Latitude), float(Longitude))
        except ValueError:
            Latitude = 33.0724127
            Longitude = 35.3335531
            self.master.master.map_frame.map_widget.set_position(float(Latitude), float(Longitude))


class OptionsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.search_frame = SearchFrame(self)
        self.search_frame.grid(row=0, column=0, pady=10, padx=10)

        self.map_type_frame = MapTypeFrame(self)
        self.map_type_frame.grid(row=1, column=0, pady=10, padx=10)
