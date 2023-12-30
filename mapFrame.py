import customtkinter as ctk
import tkintermapview


class MapFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.map_widget = tkintermapview.TkinterMapView(self, width=1230, height=690, corner_radius=10)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")  # OpenStreetMap (default)
        self.map_widget.set_position(33.0724127, 35.3335531)
        self.map_widget.set_zoom(10)

    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                            max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                            max_zoom=22)

    def add_marker(self, coords):
        self.text = self.master.options_frame.markers_frame.marker_text.get()
        self.new_marker = self.map_widget.set_marker(coords[0], coords[1], text=self.text )

    def do_nothing(self, coords):
        print(coords)

