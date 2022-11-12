from CurrencyConverter import CurrencyConverter
from tkinter import *

def exchange():
    e_usd.delete(0, END)
    e_eur.delete(0, END)
    e_gbp.delete(0, END)
    e_usd.insert(0, '%.2f' % c.convert(e_rub.get(), 'RUB', 'USD'))
    e_eur.insert(0, '%.2f' % c.convert(e_rub.get(), 'RUB', 'EUR'))
    e_gbp.insert(0, '%.2f' % c.convert(e_rub.get(), 'RUB', 'GBP'))

root.Tk()
root.title('Currency Converter')
root.geometry('300x250+300+300')
root.resizable(width=False, height=False)
root[bg] = 'black'
c = CurrencyConverter()

header_frame = Frame(root)
header_frame.pack(fill=X)

header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

h_currency = Label(header_frame, text='Currency', bg='black', fg='time', font='Arial 12 bold')
h_currency.grid(row=0, column=0, sticky=EW)
h_course = Label(header_frame, text='Course', bg='black', fg='time', font='Arial 12 bold')
h_course.grid(row=0, column=1, columnspan=2, sticky=EW)

usd_currency = Label(header_frame, text='USD', font='Arial 10')
usd_currency.grid(row=1, column=0, sticky=EW)
usd_one = Label(header_frame, text='1', font='Arial 10')
usd_one.grid(row=1, column=1, sticky=EW)
usd_converted = Label(header_frame, text='%.2f' % c.convert(1, 'USD', 'RUB'), font='Arial 10')
usd_coverted.grid(row=1, column=2, sticky=EW)

eur_currency = Label(header_frame, text='EUR', font='Arial 10')
eur_currency.grid(row=2, column=0, sticky=EW)
eur_one = Label(header_frame, text='1', font='Arial 10')
eur_one.grid(row=2, column=1, sticky=EW)
eur_converted = Label(header_frame, text='%.2f' % c.convert(1, 'EUR', 'RUB'), font='Arial 10')
eur_coverted.grid(row=2, column=2, sticky=EW)

gbp_currency = Label(header_frame, text='POU', font='Arial 10')
gbp_currency.grid(row=3, column=0, sticky=EW)
gbp_one = Label(header_frame, text='1', font='Arial 10')
gbp_one.grid(row=3, column=1, sticky=EW)
gbp_converted = Label(header_frame, text='%.2f' % c.convert(1, 'POU', 'RUB'), font='Arial 10')
gbp_coverted.grid(row=3, column=2, sticky=EW)

calc_frame = Frame(root, bg='black')
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

l.rub = Label(calc_frame, text='RUB: ', bg='black', fg='lime', font='Arial 12 bold')
l.rub.grid(row=0, column=0, padx=10)
e_rub = Entry(calc_frame, justify=CENTER, font='Arial 10')
e_rub.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)

btn_calc = Button(calc_frame, text='Convert', command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)

l_usd = Label(res_frame, text='USD', font='Arial 10')
l_usd.grid(row=2, column=0)
e_usd = Entry(res_frame, justify=CENTER, font='Arial 10')
e_usd.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)

l_eur = Label(res_frame, text='EUR', font='Arial 10')
l_eur.grid(row=3, column=0)
e_eur = Entry(res_frame, justify=CENTER, font='Arial 10')
e_eur.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)

l_gpb = Label(res_frame, text='GBP', font='Arial 10')
l_gpb.grid(row=4, column=0)
e_gpb = Entry(res_frame, justify=CENTER, font='Arial 10')
e_gpb.grid(row=4, column=1, columnspan=2, padx=10, sticky=EW)

root.mainloop()

