from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from Home_screen import MyPharmacistPro
from kivy.core.window import Window


# load the logo image
logo_image = "image/logo.png"


class main(MDApp):

    def build(self):
        Window.size = (360, 640)
        Window.top = 100
        Window.left = 100
        Window.right = 100
        Window.bottom = 100


        # adding theme_color
        self.theme_cls.theme_style = "Dark"
        self.title = "My Pharmacist Pro +"

        main_box = MDBoxLayout(orientation = "vertical", size_hint = (1,1))

        #Splash Screen
        wing = Image(source= logo_image, pos = (800,800), size_hint = (1,1))

        
        animation = Animation(x=0, y=0, d=2, t='out_bounce')
        animation.start(wing)

        main_box.add_widget(wing)


        Clock.schedule_once(lambda dt: MyPharmacistPro().run(), 5) #run timer.work1 after 5 seconds

        return main_box
    

if __name__ == '__main__':
    main().run()