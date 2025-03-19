# MACROPAD Hotkeys: Windows "Clipboard"
# BRECHTVE 19/09/2024

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Clipboard (IBA)  1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x200000, 'Riv1',    ["MEC-140002-101"]), # 1/3 add-on parts instead of "Avtronic 2.5mm rivet 01188-02510"
        (0x200000, 'Riv2',    ["MEC-142000-013"]), # 2/3 add-on parts instead of "Avtronic 2.5mm rivet 01188-02510"
        (0x200000, 'Riv3',    ["MEC-144002-002"]), # 3/3 add-on parts instead of "Avtronic 2.5mm rivet 01188-02510"
        # 2nd row ----------
        (0x202000, 'RivCom',  ["Used for mounting "]),
        (0x200020, 'empGBR',  ["G75*\n%MOIN*%\n%OFA0B0*%\n%FSLAX25Y25*%\n%IPPOS*%\n%LPD*%\n%AMOC8*\n5,1,8,0,0,1.08239X$1,22.5*\n%\nM02*\n"]),
        (0x202000, 'Label',   ["Make a label using the template file JP_SerialNumber_for_label_THT_152_7425_2_SC.btw, see also JP_SerialNumber.png."]),
        # 3rd row ----------
        (0x002020, 'colPP',   ["Refdes\tX (mm)\tY (mm)\tRotation\tValue\tSide\tSMD/TH"]),
        (0x002020, 'NclBOM',  ["LibRef\t***Description -> Function***\tValue\tTol\tMisc\tManufacturer\t***PN -> Ordercode***\t*++Description++*\tDistributor\tDistributer No\tDesignator\tQty"]),
        (0x002020, 'colBOM',  ["Qty\tFunction\tValue\tTol.\tMisc.\t***Reference -> Ordercode***\tBrand\tSMD\tPackage\t*++Description++*\t***Parts -> Refdes***"]),
        # 4th row ----------
        (0x000000, '',        []),
        (0x000020, '=SUBST',  ["=SUBSTITUEREN(SUBSTITUEREN(SUBSTITUEREN(TEKST.SAMENVOEGEN(\"BOARDNAME \",A2,\" \",C2,\" \",E2,\" \",ALS(D2=0,\"\",ALS(D2<0.01,TEKST(D2,\"0.#%\"),TEKST(D2,\"##%\")))),\">=\",\"\"),\"; \",\" \"),\"  \",\" \")"]),
        (0x000020, '=SUBST',  ["=SUBSTITUEREN(SUBSTITUEREN(SUBSTITUEREN(TEKST.SAMENVOEGEN(\"BOARDNAME \",B2,\" \",I2,\" \",C2,\" \",E2,\" \",ALS(D2=0,\"\",ALS(D2<0.01,TEKST(D2,\"0.#%\"),TEKST(D2,\"##%\")))),\">=\",\"\"),\"; \",\" \"),\"  \",\" \")"]),
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
