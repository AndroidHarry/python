from kivymd.app import MDApp
from kivy.uix.floatlayout import  FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget

'''
Tab:
            text: "CHATS"
            ScrollView:
                MDList:
                    id: list
                    TwoLineAvatarIconListItem:
                        text: 'Android Harry'
                        secondary_text: 'Just messaged you'
                        ImageLeftWidget: 
                            source: '1.jpg'
                    TwoLineAvatarIconListItem:
                        text: 'Android Harry'
                        secondary_text: 'Just messaged you'
                    TwoLineAvatarIconListItem:
                        text: 'Android Harry'
                        secondary_text: 'Just messaged you'

'''

class Tab(FloatLayout, MDTabsBase):
        '''Class implementing content for a tab.'''
        pass

class MainApp(MDApp):
    def on_start(self):
        # set colors
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = '900'

        # add messages
        self.new_message("android hh", "helli a", "1.jpg")
        self.new_message("android hh", "helli a", "1.jpg")
        self.new_message("android hh", "helli a", "1.jpg")
        self.new_message("android hh", "helli a", "1.jpg")
        self.new_message("android hh", "helli a", "1.jpg")
        self.new_message("android hh", "helli a", "1.jpg")
        self.new_message("android hh", "helli a", "1.jpg")
        self.new_message("android hh", "helli a", "1.jpg")
        
        # for i in range(20):
        #     self.root.ids.android_tabs.add_widget(Tab(text=f"Tab {i}"))

    def new_message(self, name, msg, image_name):
        new_message = TwoLineAvatarIconListItem(text=name, secondary_text=msg)
        new_message.add_widget(ImageLeftWidget(source=image_name))
        self.root.ids.list.add_widget(new_message)

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text
        ):
        # instance_tab.ids.label.text = tab_text
        pass

if __name__=='__main__':
    MainApp().run()