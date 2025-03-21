# MACROPAD Hotkeys: Altium Schematic validation queries for Windows
# BRECHTVE 11/02/2025

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Altium SchmCheck 2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x202000, 'Text',   ["(ObjectKind = 'Text String') And ((Color <> '0') Or (Font <> 'Times New Roman, 10, Bold'))"]),
        (0x202000, 'Note',   ["(ObjectKind = 'Note') And ((TextColor <> '0') Or (FillColor <> '9895935') Or (Font <> 'Times New Roman, 10'))"]),
        (0x202000, 'Note2',  ["(ObjectKind = 'Text Frame') And ((TextColor <> '0') Or (FillColor <> '9895935') Or (Font <> 'Times New Roman, 10') Or (BorderWidth <> 'Smallest'))"]),
        # 2nd row ----------
        (0x202000, 'tBox',   ["(ObjectKind = 'Text Frame') And ((TextColor <> '0') Or (FillColor <> '14737663') Or (Font <> 'Times New Roman, 16, Bold') Or (Alignment <> 'Center') Or (BorderWidth <> 'Small'))"]),
        (0x202000, 'DesPar', ["((ObjectKind = 'Parameter') Or (ObjectKind = 'Designator')) And ((Font <> 'Times New Roman, 8') Or (Color <> '8388608')) And (IsHidden = 'False') And Not (ParameterName = 'CrossRef')"]),
        (0x202000, 'PrtTxt', ["((ObjectKind = 'Parameter') And (ParameterName = 'CrossRef')) And ((Color <> '8388608') Or (Font <> 'Times New Roman, 10'))"]),
        # 3rd row ----------
        (0x000000, '',       []),
        (0x000000, '',       []),
        (0x000000, '',       []),
        # 4th row ----------
        (0x000000, '',       []),
        (0x000000, '',       []),
        (0x000000, '',       []),
        # Encoder button ---
        (0x000000, '',       [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'c'])  # Tools > Cross Probe
    ]
}
