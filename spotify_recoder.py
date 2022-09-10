import pyautogui
import keyboard
import time


# pyautogui.displayMousePosition()    

#spotify play button
SPOTIFY_PLAY_X = 640
SPOTIFY_PLAY_Y = 1340

#EOT = end of track
SPOTIFY_EOT_X = 627
SPOTIFY_EOT_Y = 1375

#ableton record button
ABLETON_RECORD_X = 1818
ABLETON_RECORD_Y = 70

#ableton record button
ABLETON_STOP_X = 1795
ABLETON_STOP_Y = 70

#top of the screen (for activating window)
ABLETON_WINDOW_X = 2300

#ableton recorded item
ABLETON_ITEM_X = 1660
ABLETON_ITEM_Y = 175

PLAYLIST_SIZE = 36


i = 4
while i < PLAYLIST_SIZE:
    pyautogui.click(ABLETON_RECORD_X, ABLETON_RECORD_Y)
    pyautogui.click(SPOTIFY_PLAY_X, SPOTIFY_PLAY_Y)

    playing = 1
    midpoint = 0
    while playing == 1:
        time.sleep(0.25)
        print("Polling...")
        print(f"1. i = {i}, midpoint = {midpoint}, playing = {playing} Play bar R {pyautogui.pixel(SPOTIFY_EOT_X, SPOTIFY_EOT_Y)[0]} > 110")
        if pyautogui.pixel(SPOTIFY_EOT_X, SPOTIFY_EOT_Y)[0] > 110:
            midpoint = 1
            print(f"2. i = {i}, midpoint = {midpoint}, playing = {playing} Play bar R {pyautogui.pixel(SPOTIFY_EOT_X, SPOTIFY_EOT_Y)[0]} < 110")
        if pyautogui.pixel(SPOTIFY_EOT_X, SPOTIFY_EOT_Y)[0] < 110 and midpoint == 1:
            print("super1")
            pyautogui.click(SPOTIFY_PLAY_X, SPOTIFY_PLAY_Y)
            pyautogui.click(ABLETON_STOP_X, ABLETON_STOP_Y)
            midpoint = 0
            playing = 0

    print("Render and save")
    pyautogui.click(ABLETON_WINDOW_X, 0)
    pyautogui.click(ABLETON_ITEM_X, ABLETON_ITEM_Y)
    keyboard.press_and_release('ctrl+shift+r')
    keyboard.press_and_release('enter')
    keyboard.write(f'track{i}')
    keyboard.press_and_release('enter')
    time.sleep(25)
    pyautogui.click(ABLETON_ITEM_X, ABLETON_ITEM_Y)
    keyboard.press_and_release('backspace')
    i = i + 1




