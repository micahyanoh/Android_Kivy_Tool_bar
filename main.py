from kivy.core.window import Window 
from kivy.lang import Builder
from kivymd.app import  MDApp

Window.size=(350,600)

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Cyan'
        screen=Builder.load_file('main.kv')
        return screen 
    def navigation_draw(self):
        print('Navigation')
if __name__ == '__main__':
    DemoApp().run()