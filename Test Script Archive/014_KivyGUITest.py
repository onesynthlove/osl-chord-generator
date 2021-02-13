from kivy.app import App
from kivy.uix.button import Button


class FirstKivy(App):
    def build(self):
         return Button(text="Welcome to LikeGeeks!")

FirstKivy().run()

#fuck kivy moving to pyside2 and QT:
    
