from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.carousel import Carousel

class Screen1(MDScreen):
    def go_ongkir(self):
        self.parent.parent.sound_slide.play()
        self.parent.transition = SlideTransition(direction="left")

        self.parent.current = 'ongkirscreen'
        self.parent.transition = SlideTransition(direction='right')

    def go_carousel(self):
        self.parent.parent.sound_slide.play()
        self.parent.transition = SlideTransition(direction="left")

        self.parent.current = 'carouselscreen'
        self.parent.transition = SlideTransition(direction='right')
    def go_camera(self):
        self.parent.parent.sound_slide.play()
        self.parent.transition = SlideTransition(direction="left")

        self.parent.current = 'camerascreen'
        self.parent.transition = SlideTransition(direction='right')
    def go_pie_chart(self):
        self.parent.parent.sound_slide.play()
        self.parent.parent.go_piechart()
        self.parent.transition = SlideTransition(direction="left")

        self.parent.current = 'piechart'
        self.parent.transition = SlideTransition(direction='right')


    def go_addscreen(self):
        self.parent.parent.sound_slide.play()
        self.parent.transition = SlideTransition(direction="left")

        self.parent.current = 'addscreen'
        self.parent.transition = SlideTransition(direction='right')



