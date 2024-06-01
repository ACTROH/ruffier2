from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, error_field_empty, error_age, error_pulse, txt_sits
from ruffier import test
from helper import check_int
from seconds import Seconds
 
name = ''
age = 0
P1 = 0
P2 = 0
P3 = 0
 
class ResultScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.lbl1 = Label(text='ok')
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(self.lbl1)
        self.add_widget(outer)
        self.on_enter = self.before
    def before(self):
        global name, P1, P2, P3
        print(name)
        self.lbl1.text = name + '\n' + test(P1, P2, P3, age)
       
 
class PulseCheck2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.error_lbl = Label(text='', color='red', size_hint=(0.8, None), height='30sp', pos_hint={'center_x': 0.5})
        self.timer_lbl = Seconds(60, size_hint=(0.8, None), height='30sp', pos_hint={'center_x': 0.5})
        self.timer_lbl.bind(done = self.timer_finish)
        instr = Label(text=txt_test3)
        lbl1 = Label(text="Результат:", halign='right')
        self.P2 = TextInput(multiline=False)
        lbl2 = Label(text='Результат після відпочинку:', halign='right')
        self.P3 = TextInput(text='', multiline=False)
        self.btn = Button(text='Завершити', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.P2)
        line2.add_widget(lbl2)
        line2.add_widget(self.P3)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(self.error_lbl)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        try:
            if not self.P2.text or not self.P3.text:
                raise Exception(error_field_empty)
            global P2, P3
            P2 = check_int(self.P2.text)
            P3 = check_int(self.P3.text)
            if P2 <= 0 or P3 <= 0:
                raise Exception(error_pulse)
            self.manager.current = 'ResultScreen'
        except Exception as error:
            self.error_lbl.text = str(error)
    def timer_finish(self, *args):
        self.next_screen = True
        self.P1.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продовжити'

class MakeFitness(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        instr = Label(text = txt_test2)
        self.next_screen = False
        self.timer_lbl = Seconds(45, size_hint=(0.8, None), height='30sp', pos_hint={'center_x': 0.5})
        self.timer_lbl.bind(done = self.timer_finish)
        self.btn = Button(text='Почати', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation = 'vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.timer_lbl)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        self.manager.current = 'PulseCheck2'
    def timer_finish(self, *args):
        self.next_screen = True
        self.P1.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продовжити'
 
class PulseCheck1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.next_screen = False
        self.error_lbl = Label(text='', color='red', size_hint=(0.8, None), height='30sp', pos_hint={'center_x': 0.5})
        self.timer_lbl = Seconds(15, size_hint=(0.8, None), height='30sp', pos_hint={'center_x': 0.5})
        self.timer_lbl.bind(done = self.timer_finish)
        instr = Label(text = txt_test1)
        lbl1 = Label(text = "Введіть результат:", halign='right')
        self.P1 = TextInput(multiline=False)
        self.P1.set_disabled(True)
        self.btn = Button(text='Почати', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        line1 = BoxLayout(orientation='vertical', size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.P1)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(self.error_lbl)
        outer.add_widget(self.timer_lbl)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(self.btn)
        self.add_widget(outer)
 
    def timer_finish(self, *args):
        self.next_screen = True
        self.P1.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продовжити'
       
    def next(self):
        try:
            if not self.next_screen:
                self.btn.set_disabled(True)
                self.timer_lbl.start()
                return
            global P1
            if not self.P1.text:
                raise Exception(error_field_empty)
            P1 = check_int(self.P1.text)
            if P1 <= 0:
                raise Exception(error_pulse)
            self.manager.current = 'MakeFitness'
        except Exception as error:
            self.error_lbl.text = str(error)
 
class UserInfoScreen(Screen):
    def __init__(self, **kw):
      super().__init__(**kw)
      self.error_lbl = Label(text='', color='red', size_hint=(0.8, None), height='30sp', pos_hint={'center_x': 0.5})
      instr = Label(text=txt_instruction)
      lbl1 = Label(text="Введіть ім'я:", halign='right')
      self.in_name = TextInput(multiline=False)
      lbl2 = Label(text='Введіть вік:', halign='right')
      self.in_age = TextInput(text='', multiline=False)
      self.btn = Button(text='Почати', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
      self.btn.on_press = self.next
      line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
      line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
      line1.add_widget(lbl1)
      line1.add_widget(self.in_name)
      line2.add_widget(lbl2)
      line2.add_widget(self.in_age)
      outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
      outer.add_widget(self.error_lbl)
      outer.add_widget(instr)
      outer.add_widget(line1)
      outer.add_widget(line2)
      outer.add_widget(self.btn)
      self.add_widget(outer)
    def next(self):
        try:
            global name, age
            if not self.in_name.text or not self.in_age.text:
                raise Exception(error_field_empty)
            name = self.in_name.text
            age = check_int(self.in_age.text)
            if age < 7:
                raise Exception(error_age)
            self.manager.current = 'PulseCheck1'
        except Exception as error:
            self.error_lbl.text = str(error)
 
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(UserInfoScreen(name='UserInfoScreen'))
        sm.add_widget(PulseCheck1(name='PulseCheck1'))
        sm.add_widget(MakeFitness(name='MakeFitness'))
        sm.add_widget(PulseCheck2(name='PulseCheck2'))
        sm.add_widget(ResultScreen(name='ResultScreen'))
        return sm
app = MyApp()
app.run()