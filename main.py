from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

class Hello(FloatLayout):
    def __init__(self,**kwargs):
        super(Hello,self).__init__(**kwargs)

        self.turns = 0
        self.points = 0
        questions = {'1+1=': '2', '1+2=': '3', '1+3=': '4', '1+__=2': '1'}
        self.questions1 = [{'task': '1+1=', 'result': '2'}, {'task': '1+2=', 'result': '3'},
                      {'task': '1+3=', 'result': '4'},
                      {'task': '1+__=2', 'result': '1'}]


        self.turns_label = Label(text = "Turns = " + str(self.turns), size_hint=(.1, .15),pos_hint={'x':.05, 'y':.9})
        self.points_label = Label(text = "Points = " + str(self.points), size_hint=(.1, .15),pos_hint={'x':.9, 'y':.9})
        self.name_label = Label(text = "First Math Game", size_hint=(.1, .15),pos_hint={'x':.45, 'y':.9})
        self.main_label = Label(text = self.questions1[self.turns]['task'], size_hint=(1, .35),pos_hint={'x':0, 'y':.55})
        self.text_input = TextInput(text="", size_hint=(.9, .1),pos_hint={'x':.05, 'y':.35})
    #Main Buttons
        self.help_button = Button(text="Help", size_hint=(.3, .1),pos_hint={'x':.65, 'y':.2},on_press = self.update)
        self.exit_button = Button(text="Exit", size_hint=(.3, .1),pos_hint={'x':.65, 'y':.1},on_press = self.update)
        self.answer_button = Button(text="Answer", size_hint=(.6, .2),pos_hint={'x':.05, 'y':.1},on_press = self.update)



        self.add_widget(self.turns_label)
        self.add_widget(self.main_label)
        self.add_widget(self.points_label)
        self.add_widget(self.exit_button)
        self.add_widget(self.help_button)
        self.add_widget(self.answer_button)
        self.add_widget(self.name_label)
        self.add_widget(self.text_input)

    def update(self,event):
        if (event.text == "Help"):
            self.main_label.text = "******* HELP ******* \n Help button to change button \n Help button to change button"
        elif (event.text == "Exit"):
            self.main_label.text = "Exit button  to change button"
        elif (event.text == "Answer"):
            if self.text_input.text == self.questions1[self.turns]['result']:
                self.points +=1

            self.text_input.text = ''
            self.turns += 1
            self.turns_label.text = "Turns = " + str(self.turns)
            self.points_label.text = "Points = " + str(self.points)
            self.main_label.text = self.questions1[self.turns]['task']
        else:
            pass

class app1(App):
    def build(self):
        return Hello()
if __name__=="__main__":
     app1().run()