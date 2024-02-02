"""
This is an automation for this game: https://45p3r4.itch.io/i-hate-spider-eggs
"""

import time
import keyboard
import pyautogui
from PIL import ImageGrab


def get_screen_coords():
    """Finds the coordinates of the game area on the screen"""

    # Store the top left and bottom right corners
    left = 0
    top = 0
    bottom = 0
    right = 0
    # Each corner should be this color pixel
    brick_color = (113, 65, 59)

    # Find the top left corner
    while left == 0:
        # Get image of the whole screen
        screenshot = ImageGrab.grab()
        # Search every 4 pixels to speed up the search
        for y in range(0, screenshot.height, 4):
            for x in range(0, screenshot.width, 4):
                # Get pixel color
                pixel = screenshot.getpixel((x, y))
                # If it is the right color we can stop looping
                if pixel == brick_color:
                    # Set variables for the top left corner
                    left = x
                    top = y
                    break
            # If break statement is reached, also break, otherwise continue
            else:
                continue
            break
        # If break statement is reached, also break, otherwise continue with some delay
        else:
            # Tell user we did not find the screen yet and sleep for half a second
            print("Screen not found, trying again")
            time.sleep(0.5)
            continue
        break
    # Find the bottom right corner (loop probably not required, but fuck it)
    while right == 0:
        # Get another image of whole screen (also probably unnecessary)
        screenshot = ImageGrab.grab()
        # Iterate through every 4 pixels backwards
        for y in reversed(range(0, screenshot.height, 4)):
            for x in reversed(range(0, screenshot.width, 4)):
                # Get pixel color
                pixel = screenshot.getpixel((x, y))
                # If it is the right color we can stop looping
                if pixel == brick_color:
                    # Set variables for the bottom right corner
                    right = x
                    bottom = y
                    break
            # If break statement is reached, also break, otherwise continue
            else:
                continue
            break
        # If break statement is reached, also break, otherwise continue
        else:
            # No delay needed because top left corner has already been found
            # and thus the game has begun already
            continue
        break

    # Tell the user we found the game
    print("Screen found")
    # Return the coordinates
    return (left, top, right, bottom)


def click_eggs(coords):
    """Function to find and click on spider eggs"""

    # Take a screenshot of game area
    screenshot = ImageGrab.grab(coords)

    # Pixel colors in the egg pixel art
    egg_colors = [
        (155, 173, 183),
        (132, 126, 135),
        (105, 106, 106),
        (89, 86, 82),
        (34, 32, 52),
    ]

    # Iterate through pixels in steps of 16 pixels for speed
    for y in range(0, screenshot.height, 16):
        for x in range(0, screenshot.width, 16):
            # Get pixel color
            pixel = screenshot.getpixel((x, y))
            # Check if pixel color matches the egg pixel art
            if pixel in egg_colors:
                # Click in correct position
                pyautogui.click(x=x + coords[0], y=y + coords[1])


if __name__ == "__main__":
    # Make pyautogui run faster because python is slow :(
    pyautogui.MINIMUM_DURATION = 0
    pyautogui.MINIMUM_SLEEP = 0
    pyautogui.PAUSE = 0
    pyautogui.FAILSAFE = False

    # Get the screen coordinates of the game
    screen_coords = get_screen_coords()
    # Hold Esc to stop the program
    while not keyboard.is_pressed("esc"):
        click_eggs(screen_coords)
