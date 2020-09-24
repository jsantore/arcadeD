import  arcade

def main():
    arcade.open_window(700, 700, "Smile Demo")
    arcade.set_background_color(arcade.color.CERULEAN)
    face = arcade.create_ellipse(350, 350, 300, 300, arcade.color.GOLD)
    nose_points = [(300, 350), (400, 350), (350, 460)]
    nose = arcade.create_polygon(nose_points, arcade.color.ELECTRIC_CRIMSON)
    eye1 = arcade.create_ellipse(175, 450, 50, 50, arcade.color.IMPERIAL_BLUE)
    eye2 = arcade.create_ellipse(525, 450, 50, 50, arcade.color.IMPERIAL_RED)
    arcade.start_render()

    face.draw()
    nose.draw()
    eye1.draw()
    eye2.draw()
    arcade.draw_arc_outline(350, 175, 250, 100, arcade.color.LAPIS_LAZULI, 189, 351, 3)
    arcade.finish_render()


    arcade.run()


main()