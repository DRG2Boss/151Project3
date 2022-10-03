import arcade

arcade.open_window(1200, 900, "Windows 95 Desktop")
arcade.set_background_color(arcade.color.CYAN)

arcade.start_render()
# Monitor Border
arcade.draw_xywh_rectangle_outline(25, 25, 1150, 850, arcade.color.BEIGE, 50)

# Green Grass


arcade.finish_render()

arcade.run()
