from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition
class RealTimeScreen(Screen):
    def go_back(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = self.parent.current = "screen1"
        self.parent.transition = SlideTransition(direction="left")