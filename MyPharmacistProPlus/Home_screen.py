from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.camera import Camera
from kivymd.uix.dialog import MDDialog
from extract_image import extract_text_from_image
from get_info_about_ext_text_from_openai import get_info_from_openai
from create_speech import talk
from animation_for_widgets import animation
from kivy.core.window import Window
from sound_player import play_sound



# load the camera shutter sound
camera_shutter_sound = "sounds/camera_shutter.mp3"
# load the touch sound
touch_sound_mp3_file = "sounds/touch_sound.mp3"
# load the logo
logo_image = "image/logo.png"
# load the flash light image
flash_light_image = "image/flash_light.png"
# load whatsapp image
whatsapp_image = "image/whatsapp.png"
# load share image
share_image = "image/share.png"
# load the close image
close_image = "image/close.png"
# load the info about app image
info_about_app_image = "image/info.png"
# load the info about company image
company_info_image = "image/company_info.png"
# laod the camera image
camera_image = "image/camera.png"


def play_mp3_file():
        play_sound(sound_file = "computer_generated_speech.mp3")


       

def text_to_speech(dialog_name, text):
        dialog_name.dismiss()
        talk(text = text)
        successfully_changed_text_to_speech =  MDDialog(
                text = "Success! \nText to speech conversion was successful! Click on microphone to play it! Please wait!!!",
                buttons = [
                        MDIconButton(icon = "image/play.png", on_release = lambda x : play_mp3_file(), icon_size = 50.0),
                        MDIconButton(icon = "image/stop.png", on_release = lambda x : successfully_changed_text_to_speech.dismiss(), icon_size = 50.0),
                ]
        )
        successfully_changed_text_to_speech.opacity = 0.7
        successfully_changed_text_to_speech.open()





def get_info_from_open_ai(text, dialog_name):
        dialog_name.dismiss()
        info_text = get_info_from_openai(text = text)
        successfully_got_information_message_box_dialog = MDDialog(
                text = "We successfully got information from internet about the extracted text! \nPlease click on the mp3 icon to change text to speech.",
                buttons = [
                        MDIconButton(icon = "image/music.png", on_release = lambda x : text_to_speech(dialog_name=successfully_got_information_message_box_dialog, text = info_text), icon_size = 50.0)
                ]
        )

        successfully_got_information_message_box_dialog.opacity = 0.7
        successfully_got_information_message_box_dialog.open()
        



def start_text_extraction(dialog_name, image_path):
        dialog_name.dismiss()
        extracted_text = extract_text_from_image(image_path=image_path)
        extration_message_box = MDDialog(
                text = "The text was extracted successfully! \nClick on the button to find information about from internet!\nPlease be patient and wait!",
                buttons = [
                        MDIconButton(icon = "image/internet.png", on_release = lambda x : get_info_from_open_ai(text = extracted_text, dialog_name= extration_message_box), icon_size = 50.0)
                ]
        )
        extration_message_box.opacity = 0.7
        extration_message_box.open()
        



#########################
def take_photo(camera_widget):
            play_sound(sound_file = camera_shutter_sound)
            camera_widget.export_to_png(filename = "image/taken_photo.png")
            photo_taken_dialog = MDDialog(
                    size_hint = (1,1),
                    text = "Success! \nClick on heart please!",
                    buttons = [
                            MDIconButton(icon = "image/okay.png", on_release = lambda x: start_text_extraction(dialog_name=photo_taken_dialog, image_path="image/taken_photo.png"), icon_size = 50.0),
                    ]
            )
            photo_taken_dialog.opacity = 0.7
            photo_taken_dialog.open()


#########################
def close_app_function():
            play_sound(sound_file = touch_sound_mp3_file)
            MyPharmacistPro.get_running_app().stop()



def whatsapp_info_function():
            play_sound(sound_file = touch_sound_mp3_file)
            dialog = MDDialog(
            title="My Pharmacist Pro + Whatsapp",
            text = "Our Whatsapp Number: +93793269259",
            buttons=[
                MDFlatButton(
                    text="Close", on_release=lambda x: dialog.dismiss(),
                ),
            ],
        )
            dialog.open()


def information_function():
        play_sound(sound_file = touch_sound_mp3_file)
        dialog = MDDialog(
        title="My Pharmacist Pro +",
        text="My Pharmacist Pro + is a Computer vision application developed by Touchless Technologies Ltd, used to find information about drugs from their pictures. It acts like a real Pharmacist. The app was first release on Dec, 2023.",
        buttons=[
            MDFlatButton(
                text="Close", on_release=lambda x: dialog.dismiss()
            )
        ],
    )
        dialog.open()



def share_function():
        play_sound(sound_file = touch_sound_mp3_file)
        dialog = MDDialog(
        title="My Pharmacist Pro + Share",
        text = "Please kindly tell your friends about this app and encourage them to use it.",
        buttons=[
            MDFlatButton(
                text="Close", on_release=lambda x: dialog.dismiss(),
            ),
        ],
    )
        dialog.open()



def company_info_function():
        play_sound(sound_file = touch_sound_mp3_file)
        dialog = MDDialog(
        title="My Pharmacist Pro + Developer Company Info",
        text = "Our company is called Touchless Technologies Ltd. We are committed to create AI apps to facilitate life and Technology usage.",
        buttons=[
            MDFlatButton(
                text="Close", on_release=lambda x: dialog.dismiss(),
            ),
        ],
    )
        dialog.open()



def flash_light_function():
        play_sound(sound_file = touch_sound_mp3_file)
        print ("flash is open now")




def click_on_logo_function():
    play_sound(sound_file = touch_sound_mp3_file)
    dialog = MDDialog(
    title="Hi! Welcome to My Pharmacist Pro +",
    text = "I am here to work for you as a virtual Pharmacist.",
    buttons=[
        MDFlatButton(
            text="Close", on_release=lambda x: dialog.dismiss(),
        ),
    ],
)
    dialog.open()

            

class MyPharmacistPro(MDApp):
    def build(self):
        Window.size = (360, 640)
        Window.top = 100
        Window.left = 100
        Window.right = 100
        Window.bottom = 100
        self.theme_cls.theme_style = "Dark"
        self.title = "My Pharmacist Pro +"
        
            
        # create a top bar
        topbar = MDTopAppBar(size_hint = (1,1), md_bg_color = ((0.070,0.070,0.070,1)))
        
        # create a box layout inside the top bar
        box_layout_for_header = MDBoxLayout(orientation = "horizontal", size_hint = (1,1), spacing = 45)
        topbar.add_widget(box_layout_for_header)


        # create a button for my pharmacist pro +

        logo = MDIconButton(icon = logo_image, size_hint = (0.8,0), on_release = lambda x:click_on_logo_function(), icon_size = 70.0, pos_hint = {"center_y":0.9})
        flash_light = MDIconButton(icon = flash_light_image, size_hint = (0.2,0), on_release = lambda x:flash_light_function(), icon_size = 30.0)
        whatsapp = MDIconButton(icon = whatsapp_image, size_hint = (0.2,0), on_release = lambda x:whatsapp_info_function(), icon_size = 30.0)
        share = MDIconButton(icon = share_image, size_hint = (0.2,0), on_release = lambda x:share_function(), icon_size = 30.0)
        close = MDIconButton(icon = close_image, size_hint = (0.2,0), on_release = lambda x:close_app_function(), icon_size = 30.0)

        box_layout_for_header.add_widget(logo)
        box_layout_for_header.add_widget(flash_light)
        box_layout_for_header.add_widget(whatsapp)
        box_layout_for_header.add_widget(share)
        box_layout_for_header.add_widget(close)

        # we create a general box layout for all other elements
        mother_box_layout = MDBoxLayout(orientation = "vertical", size_hint = (1,1), spacing = 5, padding = 5)
        
        # we create a box layout for buttons in the bottom of the page
        bottom_buttons_box = MDBoxLayout(orientation = "horizontal", size_hint = (1,0.1), spacing = 5, padding = 5)
        info_button = MDIconButton(icon = info_about_app_image, size_hint = (0,0), on_release = lambda x: information_function(), icon_size = 30.0)
        company_info_button = MDIconButton(icon = company_info_image, size_hint = (0,0), on_release = lambda *args: company_info_function(), icon_size = 30.0)        
        camera_button = MDIconButton(icon = camera_image, size_hint = (0,0), on_release = lambda x:take_photo(camera_widget=camera_widget), icon_size = 60.0)
        
        bottom_buttons_box.add_widget(info_button)
        bottom_buttons_box.add_widget(camera_button)
        bottom_buttons_box.add_widget(company_info_button)

        #Define an animation for buttons
        animation(widget_name = info_button, size_hint=(0.2,1), duration = 2)
        animation(widget_name = company_info_button, size_hint=(0.2,1), duration = 2)
        animation(widget_name = camera_button, size_hint=(0.5,1), duration = 2)

        mother_box_layout.add_widget(topbar)

        # let's creat the camera box now
        camera_box = MDBoxLayout(orientation = "vertical", size_hint = (1,1), pos_hint = {"center_x": 0.5, "center_y": 0.5})
        camera_widget = Camera(play = True, fit_mode = "cover")
        camera_box.add_widget(camera_widget)
        mother_box_layout.add_widget(camera_box)
        mother_box_layout.add_widget(bottom_buttons_box)


        return mother_box_layout