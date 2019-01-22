"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Marcus Hughes-Oliver.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------
    rect = rectangle.clone()
    c1x = rect.get_upper_left_corner().x
    print(c1x)
    c2x = rect.get_lower_right_corner().x
    print(c2x)
    c1y = rect.get_upper_left_corner().y
    c2y = rect.get_lower_right_corner().y
    diffx = rect.get_width()
    diffy = rect.get_height()
    rectangle.attach_to(window)
    for i in range(n):
        for j in range(i + 1):
            rect = rg.Rectangle(rg.Point(c1x, c1y), rg.Point(c2x, c2y))
            rect.attach_to(window)
            c1x = c1x + diffx
            c2x = c2x + diffx
            print('this is c1x:', c1x)
            print('this is c2x:', c2x)
        c1x = rectangle.get_upper_left_corner().x - ((i + 1) * diffx/2)
        c2x = rectangle.get_lower_right_corner().x - ((i + 1) * diffx/2)
        c1y = rectangle.get_upper_left_corner().y - ((i + 1) * diffy)
        c2y = rectangle.get_lower_right_corner().y - ((i + 1) * diffy)
    window.render()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
