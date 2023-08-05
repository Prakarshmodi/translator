from tkinter import *
from tkinter import ttk
from translate import Translator 
def translate_text():
    translator = Translator(to_lang=dest_lang.get())
    translation = translator.translate(Input_text.get())
    Output_text.delete('1.0', END)
    Output_text.insert(END, translation)

root = Tk()
root.geometry('1400x320')
root.resizable(0, 0)
root['bg'] = 'grey'
root.title('Language Translator')

Label(root, text='Language Translator', font="Arial 20 bold", bg='white smoke').pack()
Label(root, text='Enter your text', font='Arial 13 bold', bg='white').place(x=30, y=90)

Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)

Label(root, text='Output', font='Arial 13 bold', bg='white').place(x=780, y=90)
Output_text = Text(root, font='Arial 10', height=0.5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=700, y=130)

dest_lang = ttk.Combobox(root, values=['english','french','spanish','german','Italian'], width=22)
dest_lang.place(x=130, y=160)
dest_lang.set('Choose language')

trans_btn = Button(root, text='Translate', font='Arial 12 bold', pady=5, command=translate_text, bg='orange', activebackground='light yellow')
trans_btn.place(x=445, y=180)

root.mainloop()
