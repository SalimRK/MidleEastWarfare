import customtkinter as ctk
import assets


class MapTypeFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        zoom_slider = ctk.CTkSlider(self, from_=0, to=19, command=self.slide_zoom)
        zoom_slider.pack(pady=10)

        option_menu = ctk.CTkOptionMenu(self, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                        command=self.option_menu_callback)
        option_menu.set("OpenStreetMap")

        option_menu.pack(pady=10)

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
        self.Longitude_text.grid(row=2, column=0)

        self.Latitude_entry.grid(row=1, column=0, pady=10, padx=10)
        self.Longitude_entry.grid(row=3, column=0, pady=10, padx=10)
        self.search_button.grid(row=4, column=0, pady=10, padx=10)

    def button_event(self):
        try:
            latitude = self.Latitude_entry.get()
            longitude = self.Longitude_entry.get()
            self.master.master.map_frame.map_widget.set_position(float(latitude), float(longitude))
        except ValueError:
            latitude = 33.0724127
            longitude = 35.3335531
            self.master.master.map_frame.map_widget.set_position(float(latitude), float(longitude))


class MarkersFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.selected_icon = "marker"
        self.selected_color = "red"

        self.add_marker_button = ctk.CTkButton(self, text="Add Marker", command=self.toggle_marker_button)
        self.add_marker_button.pack(pady=5, padx=5, anchor=ctk.CENTER)

        self.marker_text = ctk.CTkEntry(self, placeholder_text="")
        self.marker_text.pack(pady=5, padx=5, anchor=ctk.CENTER)

        self.color_frame = ctk.CTkFrame(self)
        self.color_frame.pack(pady=5, padx=5, anchor=ctk.CENTER)

        self.icon_frame = ctk.CTkFrame(self)
        self.icon_frame.pack(pady=5, padx=5, anchor=ctk.CENTER)

        # icons
        self.marker_icon_button = ctk.CTkButton(self.icon_frame, text="", width=50, height=50,
                                                image=assets.marker_image_ctk,
                                                command=lambda: self.icon_select("marker"))
        self.marker_icon_button.grid(row=0, column=0, pady=5, padx=5)
        self.soldier_icon_button = ctk.CTkButton(self.icon_frame, text="", width=50, height=50,
                                                 image=assets.soldier_black_image_ctk,
                                                 command=lambda: self.icon_select("soldier"))
        self.soldier_icon_button.grid(row=0, column=1, pady=5, padx=5)
        self.tank_icon_button = ctk.CTkButton(self.icon_frame, text="", width=50, height=50,
                                              image=assets.tank_black_image_ctk,
                                              command=lambda: self.icon_select("tank"))
        self.tank_icon_button.grid(row=1, column=0, pady=5, padx=5)

        # colors
        self.black_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                          fg_color="black",
                                          command=lambda: self.color_select("black"))
        self.black_button.grid(row=0, column=0)

        self.white_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                          fg_color="white",
                                          command=lambda: self.color_select("white"))
        self.white_button.grid(row=0, column=1)

        self.blue_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                         fg_color="blue",
                                         command=lambda: self.color_select("blue"))
        self.blue_button.grid(row=0, column=2)
        self.green_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                          fg_color="green",
                                          command=lambda: self.color_select("green"))
        self.green_button.grid(row=0, column=3)

        self.red_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                        fg_color="red",
                                        command=lambda: self.color_select("red"))
        self.red_button.grid(row=0, column=4)

        self.yellow_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                           fg_color="yellow",
                                           command=lambda: self.color_select("yellow"))
        self.yellow_button.grid(row=0, column=5)

    def icon_select(self, icon):
        self.selected_icon = icon
        print("icon selected: " + self.selected_icon)

    def color_select(self, color):
        self.selected_color = color
        print("color selected: " + self.selected_color)

    def toggle_marker_button(self):
        self.master.master.master.master.map_frame.map_widget.add_left_click_map_command(
            self.master.master.master.master.map_frame.add_marker)
        self.add_marker_button.configure(text="stopMarker", command=self.stop_add)

    def stop_add(self):
        self.add_marker_button.configure(text="Add Marker", command=self.toggle_marker_button)
        self.master.master.master.master.map_frame.map_widget.add_left_click_map_command(
            self.master.master.master.master.map_frame.do_nothing)


class PolygonsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.polygon_coords = []
        self.selected_color = "red"

        self.add_polygon_button = ctk.CTkButton(self, text="Add Polygon", command=self.toggle_polygon_button)
        self.add_polygon_button.pack(pady=5, padx=5, anchor=ctk.CENTER)

        self.color_frame = ctk.CTkFrame(self)
        self.color_frame.pack(pady=5, padx=5, anchor=ctk.CENTER)

        # colors
        self.black_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                          fg_color="black",
                                          command=lambda: self.color_select("black"))
        self.black_button.grid(row=0, column=0)

        self.white_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                          fg_color="white",
                                          command=lambda: self.color_select("white"))
        self.white_button.grid(row=0, column=1)

        self.blue_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                         fg_color="blue",
                                         command=lambda: self.color_select("blue"))
        self.blue_button.grid(row=0, column=2)
        self.green_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                          fg_color="green",
                                          command=lambda: self.color_select("green"))
        self.green_button.grid(row=0, column=3)

        self.red_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                        fg_color="red",
                                        command=lambda: self.color_select("red"))
        self.red_button.grid(row=0, column=4)

        self.yellow_button = ctk.CTkButton(self.color_frame, text="", width=25, height=25,
                                           fg_color="yellow",
                                           command=lambda: self.color_select("yellow"))
        self.yellow_button.grid(row=0, column=5)

    def toggle_polygon_button(self):
        # Toggle the left-click event to either add or stop adding polygon coordinates
        if self.add_polygon_button.cget("text") == "Add Polygon":
            self.master.master.master.master.map_frame.map_widget.add_left_click_map_command(
                self.add_polygon_coord)
            self.add_polygon_button.configure(text="Stop Adding", command=self.stop_add_polygon)
        else:
            self.stop_add_polygon()  # Stop adding polygon coordinates when "Stop Adding" is clicked

    def add_polygon_coord(self, coords):
        # Add the clicked coordinates to the list
        self.polygon_coords.append((coords[0], coords[1]))

    def stop_add_polygon(self):
        # Stop adding polygon coordinates
        self.master.master.master.master.map_frame.map_widget.add_left_click_map_command(
            self.master.master.master.master.map_frame.do_nothing)
        self.create_polygon()
        self.add_polygon_button.configure(text="Add Polygon", command=self.toggle_polygon_button)

    def create_polygon(self):
        # Create a polygon on MapFrame using stored coordinates and selected color
        self.master.master.master.master.map_frame.add_polygon(self.polygon_coords, self.selected_color,)

        # Clear the stored coordinates for the next polygon
        self.polygon_coords = []

    def color_select(self, color):
        self.selected_color = color
        print("Polygon color selected: " + self.selected_color)

class ResetFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.reset_marker_button = ctk.CTkButton(self, text="reset marker", command=self.reset_marker_click)
        self.reset_marker_button.pack(pady=5, padx=5, anchor=ctk.CENTER)

        self.reset_polygon_button = ctk.CTkButton(self, text="reset_polygon", command=self.reset_polygon_click)
        self.reset_polygon_button.pack(pady=5, padx=5, anchor=ctk.CENTER)

    def reset_marker_click(self):
        pass

    def reset_polygon_click(self):
        pass


class OptionsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.search_frame = SearchFrame(self)
        self.search_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.map_type_frame = MapTypeFrame(self)
        self.map_type_frame.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

        self.label_tabs = ctk.CTkTabview(self, width=100)
        self.label_tabs.add("Markers")
        self.label_tabs.add("Polygons")
        self.label_tabs.add("Reset")

        self.label_tabs.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")

        self.markers_frame = MarkersFrame(master=self.label_tabs.tab("Markers"))
        self.markers_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.polygons_frame = PolygonsFrame(master=self.label_tabs.tab("Polygons"))
        self.polygons_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.reset_frame = ResetFrame(master=self.label_tabs.tab("Reset"))
        self.reset_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
