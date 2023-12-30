import tkinter
import tkintermapview


def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")


def left_click_event(coords):
    print("Left click event with coordinates:", coords)


root_tk = tkinter.Tk()
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Add a left-click event for adding a marker
map_widget.add_left_click_map_command(left_click_event)

# Add a left-click event for printing coordinates
map_widget.add_right_click_menu_command(label="Add Marker", command=add_marker_event, pass_coords=True)

root_tk.mainloop()
