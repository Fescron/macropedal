"""
[19/03/2025 BRECHTVE]

A macro/hotkey program for the Adafruit QT Py RP2040 connected to a (mono)
pedal and/or buttons, based on the (modified) Adafruit Macropad example
(see also https://learn.adafruit.com/macropad-hotkeys?view=all).

Pinout 3.5mm audio-jack:
 - Tip    = A0
 - Ring1  = A1
 - Ring2  = A2
 - Sleeve = GND

Macro setups for pedal presses are configured using the variables
PEDAL_SHORT_PRESS, PEDAL_LONG_PRESS, PEDAL_SHORT_DOUBLE_PRESS
and PEDAL_SHORT_LONG_PRESS. If a mono pedal is connected, which shorts
"Ring1" and "Ring2" to ground, the program configures itself to execute
these macros.The corresponding sequences can be activated by pressing
the pedal in a specific way.

The used keyboard-layout can also be configured ("KEYBOARD_LAYOUT")
(see also https://github.com/Neradoc/Circuitpython_Keyboard_Layouts).
"""

# Select the used keyboard-layout
#  - 0 = US QWERTY
#  - 1 = Belgian AZERTY
#  - 2 = Modified Belgian AZERTY (numbers and characters on number-row swapped)
KEYBOARD_LAYOUT = 1


import time
import board
import digitalio
import neopixel
from adafruit_debouncer import Button, Debouncer
from adafruit_ticks import ticks_ms, ticks_add, ticks_less
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control import ConsumerControl
# from adafruit_hid.consumer_control_code import ConsumerControlCode # Example: ConsumerControlCode.VOLUME_DECREMENT


if KEYBOARD_LAYOUT == 2:
    from keycode_win_be import Keycode as Kc
    from keyboard_layout_win_be_custom import KeyboardLayout
elif KEYBOARD_LAYOUT == 1:
    from keycode_win_be import Keycode as Kc
    from keyboard_layout_win_be import KeyboardLayout
elif KEYBOARD_LAYOUT == 0:
    from adafruit_hid.keycode import Keycode as Kc
    from adafruit_hid.keyboard_layout_us import KeyboardLayout


# Define the sequences to be activated when pressing the pedal
PEDAL_SHORT_PRESS        = [Kc.ENTER]
PEDAL_LONG_PRESS         = [Kc.UP_ARROW, -Kc.UP_ARROW, Kc.ENTER]
PEDAL_SHORT_DOUBLE_PRESS = ["PEDAL_SHORT_DOUBLE_PRESS"]
PEDAL_SHORT_LONG_PRESS   = ["PEDAL_SHORT_LONG_PRESS"]


# Define the sequences to be activated when using buttons
BUTTON_TIP   = [Kc.UP_ARROW, -Kc.UP_ARROW, Kc.ENTER]
BUTTON_RING1 = ["BUTTON_RING1"] # Unused
BUTTON_RING2 = ["BUTTON_RING2"] # Unused

# Select which functionality to use when no pedal is detected
#  - True:  Use "Debouncer()" (properties: value, fell, rose, current_duration, last_duration)
#  - False: Use "Button()"    (properties: short_count, long_press, pressed, released)
DEBOUNCER = False


# Configure the on-board Neopixel
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
stored_rgb = (0, 50, 0)
pixel.fill(stored_rgb)

# Function for lighting the Neopixel in another color (100ms busy wait)
def light_neopixel(rgb, store_and_keep_value=False):
    global stored_rgb

    pixel.fill(rgb)
    if store_and_keep_value:
        stored_rgb = rgb
    else:
        time.sleep(0.1)
        pixel.fill(stored_rgb)

# Configure the pins as inputs
PIN_LUT = [board.A0, board.A1, board.A2] # 3.5mm jack pinout: [Tip, Ring, Ring] (Sleeve = GND)
pin = []
switch = []
for i in range(3):
    pin.append(digitalio.DigitalInOut(PIN_LUT[i]))
    pin[i].direction = digitalio.Direction.INPUT
    pin[i].pull = digitalio.Pull.UP

# Check if a pedal is connected, configure the inputs accordingly
pedal_connected = False
if (pin[1].value == 0) and (pin[2].value == 0):
    print("## (MONO) PEDAL CONNECTED ##")
    pedal_connected = True

    # Configure the first input as a button-input
    #  - Properties: short_count, long_press:, pressed, released
    switch.append(Button(pin[0]))
else:
    print("## NO PEDAL CONNECTED ##")

    if DEBOUNCER:
        # Configure the inputs to be debounced
        #  - Properties: value, fell, rose, current_duration, last_duration
        for i in range(3):
            switch.append(Debouncer(pin[i]))
    else:
        # Configure the first input as a button-input
        #  - Properties: short_count, long_press, pressed, released
        switch.append(Button(pin[0]))

# Configure USB-HID
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayout(keyboard)
mouse = Mouse(usb_hid.devices)
consumer_control = ConsumerControl(usb_hid.devices)


def combined_send(sequence):
    # (Based on the Adafruit Macropad code)
    # "sequence" is an arbitrary-length list, each item is one of:
    #  - Positive integer (e.g. Kc.KEYPAD_MINUS): key pressed
    #  - Negative integer: (absolute value) key released
    #  - Float (e.g. 0.25): delay in seconds
    #  - String (e.g. "Foo\n"): corresponding keys pressed and released
    #  - List []: one or more Consumer Control codes (can also do float delay)
    #  - Dict {}: mouse buttons/motion
    for item in sequence:
        if isinstance(item, int):
            if item >= 0:
                keyboard.press(item)
            else:
                keyboard.release(-item)
        elif isinstance(item, float):
            time.sleep(item)
        elif isinstance(item, str):
            keyboard_layout.write(item)
        elif isinstance(item, list):
            for code in item:
                if isinstance(code, int):
                    consumer_control.release()
                    consumer_control.press(code)
                if isinstance(code, float):
                    time.sleep(code)
        elif isinstance(item, dict):
            if 'buttons' in item:
                if item['buttons'] >= 0:
                    mouse.press(item['buttons'])
                else:
                    mouse.release(-item['buttons'])
            mouse.move(item['x'] if 'x' in item else 0,
                       item['y'] if 'y' in item else 0,
                       item['wheel'] if 'wheel' in item else 0)
    # Release any still-pressed keys, consumer codes, mouse buttons
    # Keys and mouse buttons are individually released this way (rather
    # than release_all()) because pad supports multi-key rollover, e.g.
    # could have a meta key or right-mouse held down by one macro and
    # press/release keys/buttons with others. Navigate popups, etc.
    for item in sequence:
        if isinstance(item, int):
            if item >= 0:
                keyboard.release(item)
        elif isinstance(item, dict):
            if 'buttons' in item:
                if item['buttons'] >= 0:
                    mouse.release(item['buttons'])
    consumer_control.release()


waiting = False
deadline = None
while True:
    for i in range(len(switch)):
        switch[i].update()

    if pedal_connected:
        # Check button (pedal) presses on the first input
        if (switch[0].short_count == 1) and (switch[0].long_press):
            light_neopixel((0, 0, 50))
            combined_send(PEDAL_SHORT_LONG_PRESS)
        elif switch[0].long_press:
            light_neopixel((0, 0, 50))
            combined_send(PEDAL_LONG_PRESS)
        elif switch[0].short_count != 0:
            if switch[0].short_count == 2:
                light_neopixel((0, 0, 50))
                combined_send(PEDAL_SHORT_DOUBLE_PRESS)
            else:
                light_neopixel((0, 0, 50))
                combined_send(PEDAL_SHORT_PRESS)
    else:
        if DEBOUNCER:
            # Check if the first input is held down
            if not switch[0].value:
                if not waiting:
                    light_neopixel((50, 50, 0), True)
                    light_neopixel((50, 50, 50))
                    combined_send(BUTTON_TIP)

                    # Wait for 10 seconds before doing another sequence
                    deadline = ticks_add(ticks_ms(), 10000)
                    waiting = True
                else:
                    if not ticks_less(ticks_ms(), deadline):
                        waiting = False
            else:
                light_neopixel((0, 50, 0), True)
                waiting = False
        else:
            # Check if the input is shorted to ground
            if switch[0].pressed and not waiting:
                light_neopixel((0, 0, 50), True)
                time.sleep(0.75)
                light_neopixel((50, 0, 0))
                combined_send(BUTTON_TIP)
                waiting = True

            # Wait until the short to ground is removed
            if waiting and switch[0].released:
                light_neopixel((0, 50, 0), True)
                waiting = False
