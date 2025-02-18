from flet import *

class TextFieldCustom(TextField):
    def __init__(self,label,hint_text,password=False, can_reveal_password=True,width=300,height=70, padding=Padding(8,10,8,20),page=Page):
        super().__init__()
        self.page = page
        self.label = label,
        self.hint_text=hint_text
        self.filled=True
        self.dense=False
        self.border=InputBorder.UNDERLINE
        self.password=password
        self.can_reveal_password=can_reveal_password
        self.width=width
        self.height=height
        self.content_padding=padding
        self.fill_color='#00000000'
        self.focus_color="0xd91e2e",
        self.textField=TextField(
            label=self.label,
            hint_text=self.hint_text,
            filled=self.filled,
            dense=self.dense,
            border=self.border,
            password=self.password,
            can_reveal_password=self.can_reveal_password,
            width=self.width,
            height=self.height,
            content_padding=self.content_padding,
            fill_color=self.fill_color,
            focus_color=self.focus_color,
            on_focus=lambda e: self.focus(e),
        )
        
        
    def focus(self,e):
        self.textField.cursor_color="0xd91e2e"
        self.textField.hover_color="0x00ffffff"#0x7ad91e2e"
        self.textField.focused_border_color="0xd91e2e"
        self.textField.update()
        print("focus")
    def build(self):
        return self.textField


class TextFieldCustom2(TextField):
    def __init__(self,hint_text,width=300,height=50,):
        super().__init__(label="",fit_parent_size=True,hint_text=hint_text,filled=True,dense=False,border=InputBorder.UNDERLINE,width=width,height=height,text_align=TextAlign.CENTER)


class TextFieldCustom3(TextField):
    def __init__(self,hint_text,width=300,height=40,):
        super().__init__(label="",fit_parent_size=True,hint_text=hint_text,filled=True,dense=False,border=InputBorder.UNDERLINE,width=width,height=height,text_align=TextAlign.START,content_padding=padding.only(10,10,10,3),capitalization=TextCapitalization.WORDS)

class SearchTextFieldCustom(TextField):
    def __init__(self,hint_text,on_change,width=300,height=40):
        super().__init__(label="",fit_parent_size=True,hint_text=hint_text,filled=True,dense=False,border=InputBorder.UNDERLINE,width=width,height=height,text_align=TextAlign.CENTER,content_padding=padding.only(10,10,10,3),capitalization=TextCapitalization.WORDS,on_change=on_change)

class SearchTextFieldCustom2(TextField):
    def __init__(self,hint_text,on_change,width=None,height=40, expand=1):
        super().__init__(label="",fit_parent_size=True,hint_text=hint_text,filled=True,dense=False,border=InputBorder.UNDERLINE,width=width,height=height,text_align=TextAlign.CENTER,content_padding=padding.only(10,10,10,3),capitalization=TextCapitalization.WORDS,on_change=on_change,expand=expand)
        

class PlainTextField(TextField):
    def __init__(self,hint_text,width=200,height=150,):
        super().__init__(fit_parent_size=True,label="",hint_text=hint_text,filled=True,dense=False,expand=True,expand_loose=True,border=InputBorder.UNDERLINE,width=width,height=height,text_align=TextAlign.START,multiline=True,capitalization=TextCapitalization.SENTENCES)
        