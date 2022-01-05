from tkinter import *
from functools import partial
from click import click

root = Tk()

root.title('Calculator')

root.minsize(385, 368)
root.maxsize(385, 368)

frm = Frame(root, bg='#FF9999')

field = Entry(frm, width=40, borderwidth=10, relief=RIDGE)
field.grid(column=0, row=0, columnspan=4, pady=20, padx=30)

errm = StringVar()
errl = Label(frm, textvariable=errm, bg='#FF9999')
errl.grid(column=0, row=1, columnspan=4)

frm.errm = errm

column_row_pattern = {
  "column": [None, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1],
  "row": [None, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4],
  "symbols_cr": {
      "column": [0, 1, 2, 3],
      "row": [5, 5, 5, 5]
  }
}

for i in range(1, 10):
  button = Button(frm, text=str(i), pady=15, padx=40, bg='blue', command=partial(click, str(i), field))
  button.grid(column=column_row_pattern['column'][i], row=column_row_pattern['row'][i])

button0 = Button(frm, text='0', pady=15, padx=40, bg='blue', command=partial(click, '0', field))
button0.grid(column=1, row=4)

symbols = {
    "plus": '+',
    "negative": '-',
    "multiply": 'x',
    "division": '÷'
}

for i in range(len(symbols)):
    button = Button(frm, text=list(symbols.items())[i][1], pady=15, padx=40, bg='red', command=partial(click, list(symbols.items())[i][1], field))
    button.grid(column=column_row_pattern['symbols_cr']['column'][i], row=column_row_pattern['symbols_cr']['row'][i])

clear_button = Button(frm, text='Del', pady=15, padx=34, bg='green', command=partial(click, 'Del', field))
ac_button = Button(frm, text='AC', pady=15, padx=36, bg='green', command=partial(click, 'AC', field))
equal_button = Button(frm, text='=', pady=15, padx=184, bg='yellow', command=partial(click, '=', field))

clear_button.grid(column=2, row=4)
ac_button.grid(column=3, row=4)
equal_button.grid(column=0, row=6, columnspan=4)

frm.pack(fill=BOTH, expand=1)

frm.update()
root.update()
print(root.winfo_height())
print(root.winfo_width())


root.mainloop()