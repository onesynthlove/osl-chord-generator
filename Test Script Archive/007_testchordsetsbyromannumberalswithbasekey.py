from music21 import *


h1 = roman.RomanNumeral("iii")
h2 = roman.RomanNumeral("VI")
h3 = roman.RomanNumeral("ii")
h4 = roman.RomanNumeral("V")
h1.durationType = "whole"
h1.key = "C"
h2.durationType = "whole"
h2.key = "C"
h3.durationType = "whole"
h3.key = "C"
h4.durationType = "whole"
h4.key = "C"

h1.quarterLength = 4
h2.quarterLength = 4
h3.quarterLength = 4
h4.quarterLength = 4


h1.writeAsChord = True
h2.writeAsChord = True
h3.writeAsChord = True
h4.writeAsChord = True


print("built the harmony objects")

exportStream = stream.Stream()


print("creating new stream")


exportStream.append(h1)
exportStream.append(h2)
exportStream.append(h3)
exportStream.append(h4)


print("writing stream")
exportStream.write("midi", "/mnt/c/Users/duke/Downloads/test007.mid")
        

