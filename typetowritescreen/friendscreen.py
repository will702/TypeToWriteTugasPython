from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.boxlayout import BoxLayout
class CustomDropDown(BoxLayout):
    pass
class FriendScreen(MDScreen):
    def go_back(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = self.parent.current = "addscreen"
        self.parent.transition = SlideTransition(direction="left")
