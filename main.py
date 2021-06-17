#Source Root of A root
from kivymd.app import MDApp
#Initialize Ads for Android
from kivy.core.text import LabelBase


import glob

from json import load,dump

from datetime import date
from typetowritescreen import  nulis
from kivy.uix.image import Image
from kivy.clock import Clock
from google.cloud import storage
from kivymd.theming import ThemeManager
#Kivy import
from plyer import filechooser
from kivy.clock import mainthread
from kivy.core.window import Window
from kivy.utils import platform

from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
import certifi
from kivmob import KivMob
# Hiding Debugs
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivy.animation import Animation

if platform == 'macosx':

    Window.size = (450, 750)
    #if you use macosx you will be resized like this
else:
    pass



class OneApp(MDApp):
    try:
        #Register Custom Font
        LabelBase.register(name='font1',
                           fn_regular='bahan/font1.ttf')

        #Set Up The Settings
        ads = KivMob('ca-app-pub-1818238534900904~2025018602')
        def __init__(self):
            try:
                super().__init__()

                #Declaring MDApp object
                self.theme_cls  = ThemeManager()
                self.theme_cls.primary_palette =  'Orange'

                self.theme_cls.primary_style = 'Light'
                self.title = 'Type To Write'
                self.screen = Builder.load_file('main.kv')
                #Load The Main Windows

                self.count = 1
                #Save A Count Variable


                Clock.schedule_once(self.setup)

                # Put Banner Ads
            except:
                pass



        def choose(self):
            '''
            Call plyer filechooser API to run a filechooser Activity.
            '''
            filechooser.open_file(on_selection=self.handle_selection)



        def handle_selection(self, selection):
            '''
            Callback function for handling the selection response from Activity.
            '''
            self.selection = selection[0]



            self.picture_taken('',filename=self.selection)

        def animate_card(self, widget, text_field, spinn):
            anim = Animation(pos_hint={'center_y': 0.53})
            anim1 = Animation(pos_hint={'center_x': 0.5})
            anim2 = Animation(pos_hint={'center_y': 0.65})

            anim.start(widget)

            anim1.start(text_field)

            anim2.start(spinn)

        def reset_card(self, widget, text_field, spinn):
            anim = Animation(pos_hint={'center_y': 0.0})
            anim.start(widget)
            anim1 = Animation(pos_hint={'center_x': 0})
            anim1.start(text_field)
            anim2 = Animation(pos_hint={'center_y': 1})
            anim2.start(spinn)

        def check_data_login(self):
            self.screen.ids.firebaseloginscreen.display_loading_screen()
            self.screen.ids.typetowritescreen.get_permission()

            path = self.screen.ids.typetowritescreen.ids.screen1
            path2 = self.screen.ids.typetowritescreen.ids.screen2



            try:

                prs = nulis.Fung(path.isi.text, path.spinn1.text, path.spinn.text,
                                path.username.text, path.kelas.text)

                prs.textNulis()

                path2.image1.source = prs.return_location()
                path2.ids.label.text = str(path2.image1.source)
                self.screen.ids.typetowritescreen.change_screen('screen2')
                self.hide_screen()
                self.ads.show_interstitial()
                with open('data/date.json', 'r') as f:

                    self.attempts = load(f)

                    try:
                        pass



                    except KeyError:
                        with open('data/date.json', 'w') as fpp:
                            self.attempts[str(date.today())] = 0

                            dump(self.attempts, fpp)

                with open('data/date.json', 'w') as f:

                    try:
                        self.attempts[str(date.today())] += 1

                        dump(self.attempts, f)
                    except KeyError:
                        with open('data/date.json', 'w') as fpp:
                            self.attempts[str(date.today())] = 0

                            dump(self.attempts, fpp)

                            self.attempts[str(date.today())] += 1

                            dump(self.attempts, f)


                image = Image(source=path2.image1.source, allow_stretch=True, keep_ratio=False)
                self.screen.ids.typetowritescreen.ids.carouselscreen.ids.carousel.add_widget(image)
                self.screen.ids.typetowritescreen.ids.carouselscreen.ids.label.text = path2.image1.source


                path.isi.text, path.spinn1.text,path.spinn.text,path.username.text, path.kelas.text = '', 'Paper', 'Font', '', ''

            except:
                self.dialog2 = MDDialog(title='ERROR', text='CHOOSE FONT & PAPER FIRST',
                                        size_hint=(0.7, 1),
                                        buttons=[MDFlatButton(text='CLOSE', on_release=self.close_dialog2)
                                            , MDRaisedButton(text='DEFAULT', on_release=self.default)])

                self.dialog2.open()

                self.hide_screen()

        def default(self, *args):

            self.screen.ids.typetowritescreen.ids.screen1.spinn.text = '1'  # Make Value To Default

            self.screen.ids.typetowritescreen.ids.screen1.spinn1.text = '1'  # Make Value To Default

            self.dialog2.dismiss()  # Close The Dialog
        def close_dialog2(self,*args):
            self.dialog2.dismiss()
        def picture_taken(self, obj,filename):


            try:
                print(filename,obj)
                self.screen.ids.firebaseloginscreen.display_loading_screen()



                """Uploads a file to the bucket."""
                bucket_name = 'online-server-test'
                destination_blob_name = "test-storage-blob.png"
                debug = True
                if not debug:
                    storage_client = storage.Client()
                else:
                    cred_file = 'typetowritescreen/key.json'
                    storage_client = storage.Client.from_service_account_json(cred_file)

                bucket = storage_client.bucket(bucket_name)
                blob = bucket.blob(destination_blob_name)

                blob.upload_from_filename(filename)


                self.hit_cloud_function1(destination_blob_name)




            except:
                pass


        def picture_chosen(self, obj,filename):

            try:


                self.loading_screen()

                from PIL import Image,ImageOps
                # colorImage = Image.open(filename)
                #
                # transposed = colorImage.transpose(Image.ROTATE_270)
                #
                # transposed.save(filename)

                image = Image.open(filename)

                image = image.transpose(90)

                image = ImageOps.mirror(image)

                image.save(filename)




                """Uploads a file to the bucket."""

                bucket_name = 'online-server-test'
                destination_blob_name = "test-storage-blob.png"
                debug = True
                if not debug:
                    storage_client = storage.Client()
                else:
                    cred_file = 'typetowritescreen/key.json'
                    storage_client = storage.Client.from_service_account_json(cred_file)

                bucket = storage_client.bucket(bucket_name)
                blob = bucket.blob(destination_blob_name)

                blob.upload_from_filename(filename)


                self.hit_cloud_function(destination_blob_name)





            except:
                pass

        @mainthread
        def hit_cloud_function1(self, blob_name):

            try:

                from urllib.parse import urlencode
                msg_data = urlencode({'message': blob_name})
                headers = {'Content-type': 'application/x-www-form-urlencoded',
                           'Accept': 'text/plain'}

                trigger_url = "https://us-central1-endless-theorem-297112.cloudfunctions.net/detect_handwriting"
                UrlRequest(trigger_url, req_body=msg_data, req_headers=headers, ca_file=certifi.where(),
                           on_failure=self.error1, on_error=self.error1, on_success=self.success1)
            except:
                pass
        @mainthread
        def hit_cloud_function(self, blob_name):

            try:
                from urllib.parse import urlencode
                msg_data = urlencode({'message': blob_name})
                headers = {'Content-type': 'application/x-www-form-urlencoded',
                           'Accept': 'text/plain'}

                trigger_url = "https://us-central1-endless-theorem-297112.cloudfunctions.net/detect_handwriting"
                UrlRequest(trigger_url, req_body=msg_data, req_headers=headers, ca_file=certifi.where(),
                           on_failure=self.error, on_error=self.error, on_success=self.success)
            except:
                pass

        def error(self, *args):
            try:


                self.screen.ids.typetowritescreen.change_values(args)
                self.hide_screen()

                self.screen.ids.typetowritescreen.change_screen('screen1')
            except:
                pass

        def error1(self, *args):
            try:

                self.screen.ids.typetowritescreen.change_values(args)
                self.hide_screen()
                self.screen.ids.typetowritescreen.change_screen('screen1')


            except:
                pass

        def success1(self, request, response):

            try:
                self.screen.ids.typetowritescreen.change_values(response)
                self.hide_screen()
                self.screen.ids.typetowritescreen.change_screen('screen1')


            except:
                pass
        def success(self, request, response):


            try:
                self.screen.ids.typetowritescreen.change_values(response)
                self.hide_screen()



                self.screen.ids.typetowritescreen.change_screen('screen1')
            except:
                pass

        def setup(self,*args):
            try:

                self.screen.ids.firebaseloginscreen.web_api_key = "AIzaSyBmrGpiwimYZ-HT_BSesv4gMjuPJcG3omM"
                self.screen.ids.firebaseloginscreen.debug = False
                self.screen.ids.firebaseloginscreen.remember_user = True
                self.screen.ids.firebaseloginscreen.require_email_verification = True
                self.ads.new_interstitial('ca-app-pub-1818238534900904/8138357580')
                self.ads.request_interstitial()
            except:
                pass

        def on_resume(self):
            self.ads.request_interstitial()
        def set_up(self,*args):
            try:
                if platform == 'android':




                    for i in glob.glob('/sdcard/DCIM/TypeToWrite/*.png'):
                        image = Image(source=i, allow_stretch=True, keep_ratio=False)

                        self.screen.ids.typetowritescreen.ids.carouselscreen.ids.carousel.add_widget(image)

                    if self.screen.ids.typetowritescreen.ids.carouselscreen.ids.label.text == '':
                        self.screen.ids.typetowritescreen.ids.carouselscreen.ids.label.text = \
                        glob.glob('/sdcard/DCIM/TypeToWrite/*.png')[0]


                    if self.screen.ids.typetowritescreen.ids.carouselscreen.ids.image1.source == '':
                        self.screen.ids.typetowritescreen.ids.carouselscreen.ids.image1.source = \
                            glob.glob('/sdcard/DCIM/TypeToWrite/*.png')[0]
            except:
                pass


            if platform != 'android':
                try:




                    for i in glob.glob('*.png'):
                        image = Image(source=i, allow_stretch=True, keep_ratio=False)

                        self.screen.ids.typetowritescreen.ids.carouselscreen.ids.carousel.add_widget(image)

                    if self.screen.ids.typetowritescreen.ids.carouselscreen.ids.label.text == '':
                        self.screen.ids.typetowritescreen.ids.carouselscreen.ids.label.text = \
                            glob.glob('*.png')[0]

                    if self.screen.ids.typetowritescreen.ids.carouselscreen.ids.image1.source == '':
                        self.screen.ids.typetowritescreen.ids.carouselscreen.ids.image1.source = \
                            glob.glob('*.png')[0]


                except:
                    pass


        def call(self,button):
            if button.icon == 'pencil':
                self.screen.ids.typetowritescreen.change_screen('realtimescreen')
            if button.icon == 'typewriter':

                try:


                    self.check_data_login()



                except:
                    pass

            if button.icon == 'file':
                try:
                    self.choose()
                except:
                    pass

            if button.icon == 'notebook':
                try:
                    self.screen.ids.typetowritescreen.grammar_check()
                except:
                    pass


            if button.icon == "google-photos":




                self.screen.ids.typetowritescreen.ids.screen1.go_carousel()





            if button.icon == 'camera':
                try:
                    self.screen.ids.typetowritescreen.ids.screen1.go_camera()

                except:
                    pass

            if button.icon == 'ship-wheel':
                try:
                    self.screen.ids.typetowritescreen.ids.screen1.go_addscreen()
                except:
                    pass

            if button.icon == 'content-save':
                try:
                    self.screen.ids.typetowritescreen.make_json()
                except:
                    pass

            if button.icon == 'view-list':
                try:
                    self.screen.ids.typetowritescreen.visualize_json()


                    self.screen.ids.typetowritescreen.ids.addscreen.go_friend()
                except:
                    pass

            if button.icon == 'exit-to-app':
                try:
                    self.screen.ids.typetowritescreen.ids.addscreen.go_back()
                except:
                    pass

            if button.icon == 'delete':
                try:
                    self.screen.ids.typetowritescreen.delete()
                except:
                    pass

            if button.icon == 'chart-bar':
                try:
                    self.screen.ids.typetowritescreen.ids.screen1.go_pie_chart()
                except:
                    pass
            if button.icon == 'truck-delivery':
                try:
                    self.screen.ids.typetowritescreen.ids.screen1.go_ongkir()
                except:
                    pass







        def show_dialog(self):
            try:
                #Make A PopUp Dialog to warn user
                self.dialog = MDDialog(title='LOGOUT', text='Are you sure to log out',
                                       size_hint=(0.7, 1),
                                       buttons=[MDFlatButton(text='CLOSE', on_release=self.close_dialog)
                                           , MDRaisedButton(text='SIGN-OUT', on_release=self.sign_out)])
                #Show It On The Screen
                self.dialog.open()
            except:
                pass


        def close_dialog(self,*args):
            #Closing Dialog
            try:
                self.dialog.dismiss()
            except:
                pass

        def sign_out(self, obj):
            #Make Firebase To Be Logged Out
            try:

                self.screen.ids.firebaseloginscreen.log_out()
                self.screen.current = "firebaseloginscreen"

                self.dialog.dismiss()
            except:
                pass

        def loading_screen(self,*args):
            #Show The Loading Screen
            try:
                self.screen.ids.firebaseloginscreen.display_loading_screen()
            except:
                pass

        def hide_screen(self,*args):
            #Hide The Loading Screen
            try:
                self.screen.ids.firebaseloginscreen.hide_loading_screen()

            except:
                pass





        def build(self):



            return self.screen


        def on_start(self):


            Clock.schedule_once(self.set_up)
            Clock.schedule_once(self.screen.ids.typetowritescreen.setup)

    except:
        pass




if __name__ == '__main__':
    OneApp().run()

