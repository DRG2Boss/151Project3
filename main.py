import arcade

arcade.open_window(1200, 900, "Windows 95 Desktop")

arcade.start_render()
# Monitor Border
arcade.draw_xywh_rectangle_outline(25, 25, 1150, 850, arcade.color.BEIGE, 30)

# Green Grass

arcade.finish_render()

arcade.run()