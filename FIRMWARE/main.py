import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

from kmk.extensions.rotary_encoder import RotaryEncoder

from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

from kmk.extensions.rgb import RGB, AnimationModes

keyboard = KMKKeyboard()

macros = Macros()
layers = Layers()
keyboard.modules = [layers, macros]

keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP04, board.GP00, board.GP01)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder = RotaryEncoder(
    pin_a=board.GP10,
    pin_b=board.GP9,
)

encoder.map = [
    ((KC.VOLU,), (KC.VOLD,)), # volume up on clockwise, volume down on counter-clockwise
]

keyboard.extensions.append(encoder)

rgb = RGB(
    pixel_pin=board.GP3,
    num_pixels=16,  
    animation_mode=AnimationModes.BREATHING,
    val_default=128,  # brightness
    hue_default=213, # purple
    sat_default=255, 
    animation_speed=1,
)

keyboard.extensions.append(rgb)

oled = SSD1306(
    i2c=board.I2C(),
    device_address=0x3C,  #0x3d?
    rotation=90, #vertical
)

class VolumeDisplay(Display):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.volume = 50 
    
    def update(self):
        self.display.fill(0)
        
        bar_height = int((self.volume / 100) * 100)
        bar_x = 2
        bar_y = 14
        bar_width = 8
        
        self.display.rect(bar_x, bar_y, bar_width, 100, 1)
        self.display.fill_rect(bar_x + 1, bar_y + 100 - bar_height, bar_width - 2, bar_height, 1)
        
        self.display.text("VOL", 14, 0, 1)
        self.display.text("KD", 14, 114, 1)
        self.display.show()

display = VolumeDisplay(
    display=oled,
    entries=[], 
    width=32,
    height=128,
)

keyboard.extensions.append(display)

SCRN_MACRO = KC.MACRO(
    KC.LGUI(KC.SPACE),  # command + space
    200, 
    "scrn",  # already a macro from raycast
    50, 
    KC.ENTER, 
)

HIANIME_MACRO = KC.MACRO(
    KC.LGUI(KC.SPACE),  
    200, 
    "chrome new tab", #raycast
    200,  
    KC.ENTER,  
    300, 
    "hianime.to",  #idk what else lol
    100,  
    KC.ENTER, 
)

keyboard.keymap = [
    [
        KC.MPRV,       KC.MPLY,    KC.MNXT,         # media back, pause, skip
        SCRN_MACRO,    KC.LCTL(KC.C), KC.LCTL(KC.V), # scrn macro, copy, paste
        KC.RGB_TOG,    HIANIME_MACRO, KC.MUTE,       # rgb toggle (built in), hianime macro, mute
    ]
]

if __name__ == '__main__':
    keyboard.go()