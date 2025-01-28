from flet import *

class TextFieldCustom(TextField):
    def __init__(self,label,hint_text,password=False, can_reveal_password=True,width=300,height=70, padding=Padding(8,10,8,20)):
        super().__init__(label=label,hint_text=hint_text,filled=True,dense=False,border=InputBorder.UNDERLINE,password=password,can_reveal_password=can_reveal_password,width=width,height=height,content_padding=padding,fill_color='#00000000')
        


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
        