from tkinter import *

def ok():
    currency=entry.get()
    ans=variable.get()
    res=OPTIONS.get(ans,None)
    result=float(res)*float(currency)
    txt.delete("1.0",END)
    txt.insert("1.0",f"{currency} IND rupess is equal to {result} {ans}")

OPTIONS={ "Argentine Peso" :	1.115338,
        "Australian Dollar" :	0.017966,
        "Bahraini Dinar" :	0.005109,
        "Botswana Pula" :	0.149039,
        "Brazilian Real"  :	0.068308,
        "British Pound" :	0.010200,
        "Bruneian Dollar" :0.018113,
        "Bulgarian Lev" :	0.021856,
        "Canadian Dollar" :	0.017286,
        "Chilean Peso"	 : 9.984351,
        "Chinese Yuan Renminbi" :	0.088853,
        "Colombian Peso" :	46.472740,
        "Croatian Kuna"	: 0.084281,
        "Czech Koruna":	0.294208,
        "Danish Krone" :	0.083171,
        "Emirati Dirham":0.049903,
        "Euro":	0.011175,
        "Hong Kong Dollar":	0.105329,
        "Hungarian Forint":	3.954032,
        "Icelandic Krona" :1.728425,
        "Indonesian Rupiah"	:191.655288,
        "Iranian Rial"	: 568.665341,
        "Israeli Shekel":0.044178,
        "Japanese Yen" :	1.41372,
        "Kazakhstani Tenge" :5.696617,
        "Kuwaiti Dinar"	:0.004145,
        "Libyan Dinar"	:0.018288,
        "Malaysian Ringgit" :	0.054995,
        "Mauritian Rupee" :	0.537754,
        "Mexican Peso" :	0.271623,
        "Nepalese Rupee" :	1.607500,
        "New Zealand Dollar" :	0.019132,
        "Norwegian Krone" :	0.118981,
        "Omani Rial" :	0.005225,
        "Pakistani Rupee":	2.173161,
        "Philippine Peso":	0.653161,
        "Polish Zloty" :	0.049474,
        "Qatari Riyal" :	0.049461,
        "Romanian New Leu" :	0.054403,
        "Russian Ruble":	0.993034,
        "Saudi Arabian Riyal":	0.050956,
        "Singapore Dollar":0.018113,
        "South African Rand":	0.204165,
        "South Korean Won":	14.810964,
        "Sri Lankan Rupee":	2.529038,
        "Swedish Krona" :	0.114455,
        "Swiss Franc" :	0.012034,
        "Taiwan New Dollar":	0.382560,
        "Thai Baht":	0.407954,
        "Trinidadian Dollar":	0.092336,
        "Turkish Lira":	0.107358,
        "US Dollar":	0.013588,
        "Venezuelan Bolivar":0.135713}

convertor=Tk()
convertor.title("currency convertor")
convertor.geometry('300x400+50+50')
label=Label(convertor,text="Currency Convertor",font="lucida 20 bold",fg="red")
label.grid(row=1,column=3,padx=10,pady=10)

txt=Text(convertor,font="lucida 15 bold",width=20,height=6)
txt.grid(row=3,column=3)

lb=Label(convertor,text="currency",font="lucida 15 bold",fg="green")
lb.place(x=30,y=200)

entry=Entry(convertor,font="lucida 10 italic")
entry.place(x=140,y=210)
variable=StringVar()
variable.set(None)

choice=Label(convertor,text="Country",font="lucida 15 bold",fg="brown")
choice.place(x=30,y=240)
option=OptionMenu(convertor,variable,*OPTIONS)
option.place(x=160,y=240)

butoon=Button(convertor,text="convertor",command=ok)
butoon.place(x=100,y=290)




convertor.mainloop()