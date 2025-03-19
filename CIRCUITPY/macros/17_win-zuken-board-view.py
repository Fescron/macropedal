# MACROPAD Hotkeys: Windows "shortcuts" for Zuken - Design View
# BRECHTVE 26/07/2024

# SETTINGS: GoToMyPC = windowed, OCE-PC = 2560x1440 (100%), Dekimo-PC = 3440x1440 (100%), PowerToys>FancyZones: left-zone = 2400x1400

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'CR-8000 BrdView  2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        # (0x002000, 'Layers',  [Kc.ALT, 'v', 's']), # View > Layer Settings
        (0x002000, '*LyCol',  [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+600}]),
        # (0x200000, 'Cond1',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+573}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x202000, 'Cond2',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+592}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x200020, 'Cond3',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+610}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x000020, 'Cond4',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+630}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x002000, 'LayOrd',  [Kc.ALT, 'v', 'l']), # View > Layer Display Order
        (0x002000, '*LyOrd',  [{'x':-3000}, {'y':-1000}, {'x':+87}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1035}, {'y':+600}]),
        # (0x002000, '%LyOrd',  [{'x':-3000}, {'y':-1000}, {'x':+87}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1003}, {'y':+678}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON},
                            #    {'x':+175}, {'y':-138}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-175}, {'y':+138}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON},
                            #    {'x':+175}, {'y':-138}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-175}, {'y':+30},  {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON},
                            #    {'x':+175}, {'y':-30},  {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON},
                            #    ]),
        # (0x002000, 'NetCol',  [Kc.ALT, 'v', 'n']), # View > Net Displayed Color Settings
        (0x002000, '*NtCol',  [{'x':-3000}, {'y':-1000}, {'x':+115}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1035}, {'y':+600}]),
        # (0x002020, '-NtClr',  [{'x':-3000}, {'y':-1000}, {'x':+115}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1048}, {'y':+465}, {'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.ENTER, -Kc.ENTER, {'x':-83}, {'y':+310}, {'buttons':Mouse.LEFT_BUTTON}]),
        # 2nd row ----------
        # (0x002000, 'Lay OK',  [{'x':-3000}, {'y':-1000}, {'x':+1060}, {'y':+905}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x202000, '(TP=A)',  [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+600}]),
        (0x202020, '(BT=B)',  [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+600}]),
        # (0x002000, 'PreVw',   [Kc.ALT, 'v', 'r']), # View > Previous View
        # (0x202020, 'PreVw',   [{'x':-3000}, {'y':-1000}, {'x':+315}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x000020, '8_BOT',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+635}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+195}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'y':-160}]),
        # 3rd row ----------
        # (0x200000, '1_TOP',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+572}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+368}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x200000, '1_TOP',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+498}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+332}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'y':-160}]),
        # (0x202000, '2_MID',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+590}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+350}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x202000, '2_MID',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+517}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+313}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'y':-160}]),
        # (0x002020, '3_MID',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+608}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+332}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x002020, '3_MID',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+535}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+295}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'y':-160}]),
        # 4th row ----------
        # (0x000020, '4_BOT',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+626}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+314}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x000020, '4_BOT',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+555}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+275}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'y':-160}]),
        # (0x200020, '5_MID',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+643}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+297}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x200020, '5_MID',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+575}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+255}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'y':-160}]),
        # (0x002000, '6_BOT',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+663}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+280}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x002000, '6_BOT',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+595}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+235}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'y':-160}]),
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
