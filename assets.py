from PIL import Image
import customtkinter as ctk

# marker
marker_image_ctk = ctk.CTkImage(light_image=Image.open("assets/mark.png"),
                                size=(50, 50))

# soldier
soldier_black_image = Image.open("assets/Soldier/Soldier_Black.png").resize((50, 50))
soldier_white_image = Image.open("assets/Soldier/Soldier_White.png").resize((50, 50))
soldier_blue_image = Image.open("assets/Soldier/Soldier_Blue.png").resize((50, 50))
soldier_green_image = Image.open("assets/Soldier/Soldier_Green.png").resize((50, 50))
soldier_red_image = Image.open("assets/Soldier/Soldier_Red.png").resize((50, 50))
soldier_yellow_image = Image.open("assets/Soldier/Soldier_Yellow.png").resize((50, 50))

soldier_black_image_ctk = ctk.CTkImage(light_image=soldier_black_image,
                                       size=(50, 50))

# tank
tank_black_image = Image.open("assets/Tank/tank_Black.png").resize((50, 50))
tank_white_image = Image.open("assets/Tank/tank_White.png").resize((50, 50))
tank_blue_image = Image.open("assets/Tank/tank_Blue.png").resize((50, 50))
tank_green_image = Image.open("assets/Tank/tank_Green.png").resize((50, 50))
tank_red_image = Image.open("assets/Tank/tank_Red.png").resize((50, 50))
tank_yellow_image = Image.open("assets/Tank/tank_Yellow.png").resize((50, 50))

tank_black_image_ctk = ctk.CTkImage(light_image=tank_green_image,
                                    size=(50, 50))
