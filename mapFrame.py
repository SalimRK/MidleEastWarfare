import customtkinter as ctk
import tkintermapview


class MapFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.map_widget = tkintermapview.TkinterMapView(self, width=620, height=590, corner_radius=10)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
