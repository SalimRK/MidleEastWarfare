from PIL import Image
import customtkinter as ctk

soldier_black_image = Image.open("assets/Soldier/Soldier_Black.png").resize((50, 50))
soldier_white_image = Image.open("assets/Soldier/Soldier_White.png").resize((50, 50))
soldier_blue_image = Image.open("assets/Soldier/Soldier_Blue.png").resize((50, 50))
soldier_green_image = Image.open("assets/Soldier/Soldier_Green.png").resize((50, 50))
soldier_red_image = Image.open("assets/Soldier/Soldier_Red.png").resize((50, 50))
soldier_yellow_image = Image.open("assets/Soldier/Soldier_Yellow.png").resize((50, 50))

soldier_black_image_ctk = ctk.CTkImage(light_image=soldier_black_image,
                                       size=(50, 50))

marker_image_ctk = ctk.CTkImage(light_image=Image.open("assets/mark.png"),
                                size=(50, 50))
