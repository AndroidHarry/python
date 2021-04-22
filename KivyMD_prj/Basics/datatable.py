from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable()
        # table = MDDataTable(orientation="lr-tb",
        #             pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #             size_hint=(0.9, 0.6),
        #             column_data=[("Food", dp(30)),("Calories", dp(30))],
        #             row_data=[("Burger", "300"),("Oats", "50")])
        # table.orientation = 'lr-tb'
        # table.columm_data=[("Food", dp(30)), ("Calories", dp(30))]
        # screen.add_widget(table)
        return screen

DemoApp().run()
