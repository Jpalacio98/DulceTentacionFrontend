from flet import *


class IconButtonAction(FloatingActionButton):
    def __init__(self,tooltip,iconImage,iconSize=30,on_click=None):
        super().__init__(tooltip=tooltip,content=Image(src=iconImage,width=iconSize,height=iconSize),on_click=on_click)
        
