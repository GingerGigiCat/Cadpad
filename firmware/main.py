import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D26, board.D27, board.D28, board.D29, board.D6]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# keycodes https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# macros https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.Macro(Press(KC.LSHIFT), Tap(KC.S), Release(KC.LSHIFT)),  # new sketch
     KC.N, # normal to sketch plane
     KC.Macro(Press(KC.LSHIFT), Tap(KC.E), Release(KC.LSHIFT)), # extrude
     KC.SPACE, # deselect all
     KC.Macro(Press(KC.LSHIFT), Tap(KC.E), Release(KC.LSHIFT)), ] # fillet
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
