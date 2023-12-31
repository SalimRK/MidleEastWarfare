import customtkinter as ctk
import tkintermapview
import assets
from PIL import ImageTk


class MapFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.map_widget = tkintermapview.TkinterMapView(self, width=1230, height=690, corner_radius=10)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")  # OpenStreetMap (default)
        self.map_widget.set_position(33.0724127, 35.3335531)
        self.map_widget.set_zoom(10)

        self.map_widget.add_left_click_map_command(self.do_nothing)

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

        icon = self.master.options_frame.markers_frame.selected_icon
        color = self.master.options_frame.markers_frame.selected_color
        tk_icon = None
        if icon == "soldier":
            if color == "black":
                tk_icon = ImageTk.PhotoImage(assets.soldier_black_image)
            elif color == "white":
                tk_icon = ImageTk.PhotoImage(assets.soldier_white_image)
            elif color == "blue":
                tk_icon = ImageTk.PhotoImage(assets.soldier_blue_image)
            elif color == "green":
                tk_icon = ImageTk.PhotoImage(assets.soldier_green_image)
            elif color == "red":
                tk_icon = ImageTk.PhotoImage(assets.soldier_red_image)
            elif color == "yellow":
                tk_icon = ImageTk.PhotoImage(assets.soldier_yellow_image)
        elif icon == "tank":
            if color == "black":
                tk_icon = ImageTk.PhotoImage(assets.tank_black_image)
            elif color == "white":
                tk_icon = ImageTk.PhotoImage(assets.tank_white_image)
            elif color == "blue":
                tk_icon = ImageTk.PhotoImage(assets.tank_blue_image)
            elif color == "green":
                tk_icon = ImageTk.PhotoImage(assets.tank_green_image)
            elif color == "red":
                tk_icon = ImageTk.PhotoImage(assets.tank_red_image)
            elif color == "yellow":
                tk_icon = ImageTk.PhotoImage(assets.tank_yellow_image)
        elif icon == "marker":
            tk_icon = None

        self.text = self.master.options_frame.markers_frame.marker_text.get()
        self.new_marker = self.map_widget.set_marker(coords[0], coords[1], text=self.text,
                                                     marker_color_outside=color,
                                                     marker_color_circle=None,
                                                     text_color=color,
                                                     icon=tk_icon
                                                     )

    def do_nothing(self, coords):
        print(coords)

    def add_polygon(self, coords, color):
        self.polygon = self.map_widget.set_polygon(coords, fill_color=color, outline_color=color)

    def reset_polygon(self):
        self.map_widget.delete_all_polygon()

    def reset_marker(self):
        self.map_widget.delete_all_marker()
