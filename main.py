from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

turns = 0
points = 0

class Hello(FloatLayout):
    def __init__(self,**kwargs):
        super(Hello,self).__init__(**kwargs)

        self.turns_label = Label(text = "Turns = " + str(turns), size_hint=(.1, .15),pos_hint={'x':.05, 'y':.9})
        self.points_label = Label(text = "Points = " + str(points), size_hint=(.1, .15),pos_hint={'x':.9, 'y':.9})
        self.name_label = Label(text = "First Math Game", size_hint=(.1, .15),pos_hint={'x':.45, 'y':.9})
        self.main_label = Label(text = "Hello and Welcome!", size_hint=(1, .55),pos_hint={'x':0, 'y':.35})

    #Main Buttons
        self.help_button = Button(text="Help", size_hint=(.3, .1),pos_hint={'x':.65, 'y':.2})
        self.exit_button = Button(text="Exit", size_hint=(.3, .1),pos_hint={'x':.65, 'y':.1},on_press = self.update)
        self.answer_button = Button(text="Answer", size_hint=(.6, .2),pos_hint={'x':.05, 'y':.1})



        self.add_widget(self.turns_label)
        self.add_widget(self.main_label)
        self.add_widget(self.points_label)
        self.add_widget(self.exit_button)
        self.add_widget(self.help_button)
        self.add_widget(self.answer_button)
        self.add_widget(self.name_label)

    def update(self,event):
        if (event.text == "Help"):
            self.main_label.text = "Help button to change button"
        elif (event.text == "Go"):
            self.main_label.text = "Go button  to change button"
        else:
            pass
        #self.main_label.text = "Changed to change"

class app1(App):
    def build(self):
        return Hello()
if __name__=="__main__":
     app1().run()