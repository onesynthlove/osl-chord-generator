# import sys
# import os.path
# from music21 import *
# from os import path
# from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtCore import QFile
# # from ui_mainwindow import Ui_MainWindow
# from PySide6.QtUiTools import QUiLoader
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "./qt-ui-files/osl-chord-generator-main.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec_())

# from pathlib import Path

# baseNoteLength = "quarter"
# baseMidiDirectory = "/Users/duke/Downloads/OSL_BeatPatterns/"


#OK Here's the Key Map for FLStudio 20 FPC

# Lite Crash    G4
# Tambourine    F#4
# Ride Bell     F4
# Lite Ride     D#4
# Crash         C#4
# Hi Tom        C4
# Mid Tom       B3
# Open HiHat    A#3
# Lo Tom        A3
# Pedal Hi Hat  G#3
# Floor Tom     G3
# Closed Hat    F#3
# Snare 1       E3
# Snare 2       D3
# SideStick     C#3
# Kick Drum     C3

# #test a 4 on the floor beat
# kickDrum = note.Note("C2", type=baseNoteLength)
# snareDrum = note.Note("E2", type=baseNoteLength)
# print("putting kickDrum in sequence")

# exportStream = stream.Stream()
# exportStream.repeatAppend(kickDrum, 32)
# exportStream.repeatAppend(snareDrum, 32)
#
#
# filePath = baseMidiDirectory + "4onthefloortest" + ".mid"
# if path.exists(filePath) != True:
#     print("writing stream for progression " + filePath )
#     exportStream.write("midi", filePath)
# else:
#     print(filePath + " already exists. Skipping write operation.")
