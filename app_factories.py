import tkinter as tk
from typing import List


def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Assistente de Prova Lógica')
    root.config(padx=10,pady=10,background='#fff')
    root.resizable(False,False)
    return root


def make_label(root)-> tk.Label:
    label = tk.Label(
        root,text='Vamos lá',anchor='e',justify='right',background='#fff'
    )
    label.grid(row=0,column=0,columnspan=5,sticky='news')
    return label


def make_display(root)->tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(
        font=('Helvetica', 30, 'bold'), justify='center', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    display.bind('<Control-a>', display_control_a)
    '''displayesquerda = tk.Entry(root)
    displayesquerda.grid(row=1, column=0, columnspan=2, sticky='news', pady=(0, 10))
    displayesquerda.config(
        font=('Helvetica',30,'bold'),justify='center',bd=1,relief='flat',
        highlightthickness=1,highlightcolor='#ccc'
    )
    displayesquerda.bind('<Control-a>', display_control_a)
    displaymeio = tk.Entry(root)
    displaymeio.grid(row=1, column=2, sticky='news', pady=(0, 10))
    displaymeio.config(
        font=('Helvetica', 30, 'bold'), justify='center', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    displaymeio.bind('<Control-a>', display_control_a)
    displaydireita = tk.Entry(root)
    displaydireita.grid(row=1, column=3, columnspan=5, sticky='news', pady=(0, 10))
    displaydireita.config(
        font=('Helvetica', 30, 'bold'), justify='center', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    displaydireita.bind('<Control-a>', display_control_a)
    return displayesquerda, displaymeio, displaydireita'''
    return display

def display_control_a(event):
    event.widget.select_range(0,'end')
    event.widget.icursos('end')
    return 'break'


def make_button(root, text, **grid_options) -> tk.Button:
    btn = tk.Button(root, text=text)
    btn.grid(**grid_options)
    btn.config(
        font=('Helvetica', 15, 'normal'),
        pady=10, width=1, background='#f1f2f3', bd=0,
        cursor='hand2', highlightthickness=0,
        highlightcolor='#ccc', activebackground='#ccc',
        highlightbackground='#ccc'
    )
    return btn


def make_buttons(root, starting_row) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['~', '^', 'v', '->', '<->'],
        ['Apagar','Avançar']

    ]

    buttons: List[List[tk.Button]] = []

    for row, row_value in enumerate(button_texts, start=starting_row):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = make_button(
                root, text=col_value,
                row=row, column=col_index, sticky='news', padx=5, pady=5
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons
