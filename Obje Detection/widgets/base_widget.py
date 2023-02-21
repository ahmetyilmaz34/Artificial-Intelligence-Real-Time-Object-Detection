import pathlib
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.scrolledframe import ScrolledFrame

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "base.ui"


class BaseWidget(ttk.Panedwindow):
    def __init__(self, master=None, **kw):
        super(BaseWidget, self).__init__(master, **kw)
        self.F_Buttons = ttk.Frame(self)
        self.btn_start = tk.Button(self.F_Buttons)
        self.btn_start.configure(activebackground='#3756e1', activeforeground='#ffffff', background='#283184', cursor='hand2')
        self.btn_start.configure(font='{Microsoft YaHei} 12 {bold}', foreground='#ffffff', text='BAŞLAT')
        self.btn_start.pack(expand='true', fill='both', padx='5', pady='5', side='left')
        self.btn_start.configure(command=self.capture)
        self.btn_stop = tk.Button(self.F_Buttons)
        self.btn_stop.configure(activebackground='#e4453a', activeforeground='#ffffff', background='#c12515', cursor='hand2')
        self.btn_stop.configure(font='{Microsoft YaHei} 12 {bold}', foreground='#ffffff', text='BİTİR')
        self.btn_stop.pack(expand='true', fill='both', padx='5', pady='5', side='left')
        self.btn_stop.configure(command=self.stop)
        self.F_Buttons.configure(height='200', relief='groove', width='200')
        self.F_Buttons.pack(side='left')
        self.add(self.F_Buttons, weight='1')
        self.PW_Body = ttk.Panedwindow(self, orient='horizontal')
        self.SF_Canvas = ScrolledFrame(self.PW_Body, scrolltype='both')
        self.canvas_image = tk.Canvas(self.SF_Canvas.innerframe)
        self.canvas_image.configure(background='#2c2c2c', height='480', width='640')
        self.canvas_image.pack(expand='true', side='top')
        self.SF_Canvas.configure(usemousewheel=False)
        self.SF_Canvas.pack(expand='true', fill='both', side='top')
        self.PW_Body.add(self.SF_Canvas, weight='3')
        self.PW_Body.configure(height='200', width='200')
        self.PW_Body.pack(side='top')
        self.add(self.PW_Body, weight='16')
        self.NB_Footer = ttk.Notebook(self)
        self.txt_log = tk.Text(self.NB_Footer)
        self.txt_log.configure(background='#404040', foreground='#ffffff', height='10', width='50')
        self.txt_log.pack(side='top')
        self.NB_Footer.add(self.txt_log, text='Message Log')
        self.NB_Footer.configure(height='100', width='200')
        self.NB_Footer.pack(side='top')
        self.add(self.NB_Footer, weight='1')

    def capture(self):
        pass

    def stop(self):
        pass



