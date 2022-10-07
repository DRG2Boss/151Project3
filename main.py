import arcade

arcade.open_window(1200, 900, "Master Chief Helmet")
arcade.set_background_color(arcade.color.PURPLE)

arcade.start_render()
# My Name:
author = arcade.Text("Isaiah Marshall", 25, 875, arcade.color.WHITE, 14)
author.draw()
# Halo Ring:
arcade.draw_circle_outline(1200, 800, 600, arcade.color.BLUE_GRAY, 40)
arcade.draw_circle_outline(1200, 800, 570, arcade.color.FOREST_GREEN, 20)
# Pew Pew Human Ship
arcade.draw_line(900, 700, 940, 700, arcade.color.BLACK, 7)
arcade.draw_line(950, 690, 940, 670, arcade.color.BLACK, 6)
arcade.draw_line(960, 700, 980, 680, arcade.color.BLACK, 7)
arcade.draw_circle_filled(950, 720, 20, arcade.color.ORANGE)
arcade.draw_circle_filled(950, 720, 10, arcade.color.YELLOW)
# Agressive Alien Ships
arcade.draw_line(1000, 730, 1080, 730, arcade.color.DEEP_PINK, 10)
arcade.draw_circle_filled(1050, 730, 20, arcade.color.DEEP_PINK)
arcade.draw_line(1050, 650, 1170, 650, arcade.color.DEEP_PINK, 15)
arcade.draw_circle_filled(1125, 650, 30, arcade.color.DEEP_PINK)
arcade.draw_line(1120, 690, 1200, 690, arcade.color.DEEP_PINK, 12)
arcade.draw_circle_filled(1180, 690, 25, arcade.color.DEEP_PINK)
# Green Mask - Base:
arcade.draw_xywh_rectangle_filled(250, 200, 650, 465, arcade.color.LIME_GREEN)
arcade.draw_arc_filled(575, 625, 625, 550, arcade.color.GOLD, -180, 0)
arcade.draw_arc_outline(575, 625, 635, 560, arcade.color.BLACK, -180, 0, 20)
# Green Mask - Lower Half Shaping:
arcade.draw_triangle_filled(250, 550, 300, 390, 250, 340, arcade.color.PURPLE)
arcade.draw_triangle_filled(900, 550, 850, 390, 900, 340, arcade.color.PURPLE)
arcade.draw_arc_filled(575, 200, 550, 100, arcade.color.LIME_GREEN, -180, 0)
# Green Mark - Lower Half, Left Side Detailing:
arcade.draw_circle_filled(280, 300, 20, arcade.color.BLACK)
arcade.draw_circle_filled(280, 250, 20, arcade.color.BLACK)
arcade.draw_circle_filled(350, 275, 30, arcade.color.LIGHT_GREEN)
arcade.draw_line(500, 150, 500, 300, arcade.color.BLACK, 10)
arcade.draw_line(380, 335, 505, 300, arcade.color.BLACK, 10)
for ylocleft in range(200, 305, 35):
    arcade.draw_line(400, ylocleft, 480, ylocleft, arcade.color.BLACK, 15)
# Green Mark - Lower Half, Right Side Detailing:
arcade.draw_circle_filled(870, 300, 20, arcade.color.BLACK)
arcade.draw_circle_filled(870, 250, 20, arcade.color.BLACK)
arcade.draw_circle_filled(800, 275, 30, arcade.color.LIGHT_GREEN)
arcade.draw_line(650, 150, 650, 300, arcade.color.BLACK, 10)
arcade.draw_line(645, 300, 770, 335, arcade.color.BLACK, 10)
for ylocright in range(200, 305, 35):
    arcade.draw_line(670, ylocright, 750, ylocright, arcade.color.BLACK, 15)
# Green Mask - Upper Half:
arcade.draw_arc_filled(575, 665, 525, 200, arcade.color.LIME_GREEN, 0, 180)
arcade.draw_line(262, 625, 888, 625, arcade.color.BLACK, 10)
arcade.draw_xywh_rectangle_filled(250, 625, 270, 50, arcade.color.DARK_GRAY)
arcade.draw_xywh_rectangle_filled(630, 625, 270, 50, arcade.color.DARK_GRAY)
# Tagline:
tagline = arcade.Text("Finish The Fight", 425, 50, arcade.color.WHITE_SMOKE, 30)
tagline.draw()

arcade.finish_render()
arcade.run()
