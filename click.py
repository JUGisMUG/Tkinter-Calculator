from tkinter import END
from time import sleep

def click(x, f):
    if x == 'Del':
        if f.get() == '': 
            return err('Nothing To Delete Here!', 0.5, f)
        return f.delete(len(f.get())-1)
    elif x == 'AC':
        if f.get() == '':
            return err('Nothing To Delete Here!', 0.5, f)
        return f.delete(0, END)
    elif x == '=':
        equation = f.get()

        if equation == '':
             return err('Please Enter Something!', 0.5, f)

        if '÷' in equation:
            equation = equation.replace('÷', '/')
        if 'x' in equation:
            equation = equation.replace('x', '*')
        click('AC', f)

        try:
            f.insert(0, eval(equation))
        except:
            err('Invalid Operation!', 0.5, f)
        return

    f.insert(len(f.get()), x)


def err(msg, time, f):
    f.master.errm.set(msg)
    f.master.update()
    sleep(time)
    f.master.errm.set('')