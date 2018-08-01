from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
# from kivy.clock import Clock
# from functools import partial


class ChooseRoleScreen(Screen):
    """
    Screen to select which role the user wants.
    """

    dropdown_button = ObjectProperty(None)
    go_button = ObjectProperty(None)
    champ_list = ObjectProperty(None)


    def __init__(self, **kwargs):
        super(ChooseRoleScreen, self).__init__(**kwargs)
        self.create_dropdown()
        self.is_champ_selection_shown = False


    def enable_go_button(self, *args):
        self.go_button.disabled = False


    def create_dropdown(self):
        """
        Create a dropdown box.
        """
        self.dropdown = DropDown()
        roles = ["Top", "Jungle", "Middle", "ADC", "Support"]

        for role in roles:
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.
            btn = Button(text=role, size_hint_y=None, height=44)

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

            self.dropdown.add_widget(btn)

        # Display the button's text as the selected text
        self.dropdown.bind(on_select=lambda instance, x:
                           setattr(self.dropdown_button, 'text', x))
        # Enable the go button
        self.dropdown.bind(on_select=self.enable_go_button)


    def go_button_logic(self):
        """
        Pass the selected role to the next screen.
        """

        # Set the ScreenManager role_selected to the role selected
        self.parent.role_selected = self.dropdown_button.text
        self.is_champ_selection_shown = True

        popup_button = Button(text="Role Selected: {}".format(self.parent.role_selected),
                              size_hint=(0.5, 0.5))
        popup = Popup(title="Role Selected", content=popup_button, size_hint=(0.8, 0.8))
        popup_button.bind(on_press=popup.dismiss)
        popup.open()

        print(self.is_champ_selection_shown)


class RunesBuildsScreen(Screen):
    """
    TODO: Documentation & Logic
    """
    pass


class MainScreenManager(ScreenManager):
    role_selected = None


class TopFiveLeagueApp(App):
    """
    Main class that will run our GUI
    """
    def get_screen_manager(self):
        msm = MainScreenManager()
        return msm


    def build(self):
        self.sm = self.get_screen_manager()
        return self.sm


if __name__ == "__main__":
    TopFiveLeagueApp().run()
