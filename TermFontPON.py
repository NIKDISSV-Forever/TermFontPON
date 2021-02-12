from PIL import Image, ImageDraw, ImageFont
import shutil
import sys
import os


class TermFontPON:

    def __init__(self,
                 PADDING=(0, 0),
                 italic=0,
                 TERMINAL_SIZE=(30, 30),
                 bg=None,
                 fg=None,
                 TEXT=None):

        self.Image_With_Text = Image.new(mode="RGB", size=TERMINAL_SIZE)
        self.drawer = ImageDraw.Draw(self.Image_With_Text)
        self.italic = italic

        if not TEXT:
            TEXT = "Hello World!"
        self.bg = "".join(
            list(
                filter(lambda x: x, [bg])
            )
        ).center(1, " ")
        self.fg = "".join(
            list(
                filter(lambda x: x, [fg])
            )
        ).center(1, chr(8718))

        self.drawer.text(
            PADDING,
            TEXT)
        self.Result_Text = self.get_text()
        print(self.Result_Text)

    def get_text(self):

        pixes = self.Image_With_Text.load()
        IMAGE_SIZE = self.Image_With_Text.size
        Result_Text = ""
        for i in range(IMAGE_SIZE[1]):
            for j in range(IMAGE_SIZE[0]):
                S = sum(pixes[j, i])
                Ser = (255//2)*3
                if S > Ser:
                    Result_Text += self.fg
                else:
                    if self.italic and j == 0:
                        continue
                    Result_Text += self.bg
        return Result_Text


TERMINAL_SIZE = shutil.get_terminal_size()
args = sys.argv

TEXT, fg, bg = [None]*3

if "-fg" in args:
    fg = args[
        args.index("-fg")+1
    ]
    args.remove("-fg")
    args.remove(fg)
if "-bg" in args:
    bg = args[
        args.index("-bg")+1
    ]
    args.remove("-bg")
    args.remove(bg)
if "-cls" in args:
    os.system("cls" if os.name == "nt" else "clear")
    args.remove("-cls")
if "-t" in args:
    TEXT = " ".join(args[
        args.index("-t")+1:
    ])


TermFontPON(
    TERMINAL_SIZE=TERMINAL_SIZE,  # w, h
    PADDING=tuple(
        map(
            lambda x: x//4,
            TERMINAL_SIZE
        )
    ),
    TEXT=TEXT,
    fg=fg,
    bg=bg,
)
