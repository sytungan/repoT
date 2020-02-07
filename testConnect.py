import tkinter as tk
import requests

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(text="Check site of")
        self.label.pack()
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.contents = tk.StringVar()
        self.entrythingy['textvariable'] = self.contents
        self.entrythingy.bind('<Key-Return>', self.check_site)

        self.hi_there = tk.Button(self)
        self.hi_there['text'] = 'Check site'
        self.hi_there['command'] = self.check_site
        self.hi_there.pack()

        self.quit = tk.Button(self, text='QUIT', command=root.destroy)
        self.quit.pack()

    def check_site(self, event=None):
        url = self.contents.get().strip()
        if not url.startswith('http'):
            url = 'http://{}'.format(url)
        
        resp = requests.get(url)
        print("{} response: {}".format(url, resp.status_code))

        var = tk.StringVar()
        if (resp.status_code==200):
            var.set("OK")
        else:
            var.set("not OK")

        self.label = tk.Label(textvariable=var)
        self.label.pack()


root = tk.Tk()
app = Application(master=root)
app.master.title('My checker app')
app.master.minsize(200, 150)
app.mainloop()