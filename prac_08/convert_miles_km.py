"""

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class ConvertMilesToKmApp(App):
    """ ConvertMilesToKmApp is a Kivy App for converting miles to km"""

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """ handle conversion (could be button press or other call), output result to label widget """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """ handle increment, either positive or negative, by 1, output result to input widget """
        value = self.get_validated_miles()
        result = value + increment
        self.root.ids.input_number.text = str(result)
        self.handle_convert()

    def get_validated_miles(self):
        """Gets input text and converts it to float, returns 0 if error"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKmApp().run()
