import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        Window.size = (300, 230)
        self.title = 'Calculadora Simple'
        self.icon = 'icon.png'
        Window.clearcolor = (0.2, 0.6, 0.8, 1)

        layout = FloatLayout()

        self.num1 = TextInput(size_hint=(None, None), size=(260, 50), pos=(20, 170), halign='right', font_size=20, input_filter='int', multiline=False)
        self.num2 = TextInput(size_hint=(None, None), size=(260, 50), pos=(20, 110), halign='right', font_size=20, input_filter='int', multiline=False)

        btn_sum = Button(text='Suma', size_hint=(None, None), size=(50, 40), pos=(20, 60), font_size=12)
        btn_res = Button(text='Resta', size_hint=(None, None), size=(50, 40), pos=(90, 60), font_size=12)
        btn_mult = Button(text='Producto', size_hint=(None, None), size=(50, 40), pos=(160, 60), font_size=11)
        btn_div = Button(text='Division', size_hint=(None, None), size=(50, 40), pos=(230, 60), font_size=11.5)

        self.label = Label(text='Esperando la entrada', size_hint=(None, None), pos=(70, 0), size=(150, 40))

        btn_sum.bind(on_press=self.on_press_button)
        btn_res.bind(on_press=self.on_press_button)
        btn_mult.bind(on_press=self.on_press_button)
        btn_div.bind(on_press=self.on_press_button)

        layout.add_widget(self.num1)
        layout.add_widget(self.num2)
        layout.add_widget(btn_sum)
        layout.add_widget(btn_res)
        layout.add_widget(btn_mult)
        layout.add_widget(btn_div)
        layout.add_widget(self.label)


        return layout
    def on_press_button(self, instance):
        try:
            valor1 = float(self.num1.text)
            valor2 = float(self.num2.text)
        except ValueError:
            print('Ingrese el valor correcto')
        if instance.text == 'Suma':
            self.label.text='el resultado de la suma es:' + str(valor1 + valor2)
        if instance.text == 'Resta':
            self.label.text='el resultado de la resta es:' + str(valor1 - valor2)
        if instance.text == 'Producto':
            self.label.text='el resultado del producto es:' + str(valor1 * valor2)
        if instance.text == 'Division':
            if valor2 == 0:
                self.label.text = 'No se puede hacer la operación'
            else:
                self.label.text='el resultado de la suma es:' + str(valor1 / valor2)

if __name__ == '__main__':
    MyApp().run()