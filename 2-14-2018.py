"""
CSC131 - Computational Thinking
Missouri State University, Spring 2018
FP Chapter 8 - Graphical User Interfaces
File: labeldemo.py
"""
"""
from breezypythongui import EasyFrame


class LabelDemo(EasyFrame):
    Displays a greeting in a window.
    

    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text="Hello world!", row=0, column=0)


def main() -> None:
    LabelDemo().mainloop()


if __name__ == "__main__":
    main()(text = "Hello world!", row = 0, column = 0)
"""

from breezypythongui import EasyFrame


class LayoutDemo(EasyFrame):
    """Displays labels in the quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)

        # Note: default alignment is left; to change to center or grid element
        # add  sticky="NSEW"
        self.addLabel(text="(0, 0)", row=0, column=0, sticky = 'NSEW')
        self.addLabel(text="(0, 1)", row=0, column=1, sticky = 'NSEW')
        self.addLabel(text="(1, 0)", row=1, column=0, sticky = 'NSEW')
        self.addLabel(text="(1, 1)", row=1, column=1, sticky = 'NSEW')


def main():
    """Instantiate and pop up the window."""
    LayoutDemo().mainloop()


if __name__ == "__main__":
    main()