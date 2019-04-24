from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
''' Расположение кнопок через boxlayout
class BoxApp(App):
    def build(self):
        bl = BoxLayout(orientation="vertical",padding=[0,50,100,0],spacing=100) #расположение кнопок + откступы от краев и от кнопок
        bl.add_widget(Button(text = "Кнопка 1"))
        bl.add_widget(Button(text="Кнопка 2"))
        bl.add_widget(Button(text="Кнопка 3"))
        return bl
Через BoxLayout
class BoxApp(App):
    def build(self):
        bl = GridLayout(cols=5, padding=[30],spacing=3) #указывает количество столбцов или строк(или то и то)
        for i in range(20): #генерируем 20 кнопок
            bl.add_widget(Button(text="Х"))
        return bl
'''
class BoxApp(App):
    def build(self):
        al=AnchorLayout() #размещение кнопки по центру
        bl = BoxLayout(orientation="vertical",size_hint=[.5,.5],spacing=3) #
       # bl = BoxLayout(orientation="vertical", size_hint=[None, None], size=[300,200]) #размещение с указанием размера кнопки
        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text="Кнопка")) #кнопка будет занимать 50%в ширену и в высоту
        al.add_widget(bl) #наследуем параменты AnchorLayout для BoxLayout
        return al
if __name__=="__main__":
    BoxApp().run()