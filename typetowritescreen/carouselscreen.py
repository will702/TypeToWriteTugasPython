from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition

from kivy.uix.carousel import Carousel


class CarouselScreen(MDScreen):
    def go_back(self):
        self.parent.parent.sound_slide.play()
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = self.parent.current = "screen1"
        self.parent.transition = SlideTransition(direction="left")





class MyCarousel(Carousel):


    def on_index(self, *args):

        try:
            # YOUR CODE GOES HEREs
            try:
                #print(self.parent.parent.parent.parent.parent.parent)
                pass
            except:
                pass
            self.parent.parent.parent.parent.change_carousel_label(self.current_slide.source)



            Carousel.on_index(self, *args)
        except:
            pass


