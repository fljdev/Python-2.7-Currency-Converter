# -*- coding: utf-8 -*-
from Tkinter import *
import urllib2
import json

def currencyConverter(currency_from,currency_to,currency_input):
  
    yql_base_url = "https://query.yahooapis.com/v1/public/yql"
    
    yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+currency_from+currency_to+'")'
    
    yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    try:
        yql_response = urllib2.urlopen(yql_query_url)
        try:
            yql_json = json.loads(yql_response.read())
            currency_output = currency_input * float(yql_json['query']['results']['rate']['Rate'])
            return currency_output
        except (ValueError, KeyError, TypeError):
            return "JSON format error"
    
    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

#****This will be called if a non numerical value is placed in text box
def numberErrorMessageYen():
  s_label.configure(text="Number expected!!")

def numberErrorMessageSterling():
   
  s_label.configure(text="Number expected!!")
def numberErrorMessageDollar():
     s_label.configure(text="Number expected!!")

def convertSterling(Event=None):
    try:
        a = float(anEntry.get())
        currency_from="EUR"
        currency_to="GBP"
        rate=currencyConverter(currency_from,currency_to,a)
        s_label.configure(text='£%g'%rate)
    except ValueError:
        numberErrorMessageSterling()
        pass 

def convertDollar(Event=None):

  try:
    a=float(anEntry.get())


    currency_input = a
    currency_from = "EUR"
    currency_to = "USD"
    rate = currencyConverter(currency_from,currency_to,currency_input)
    s_label.configure(text='$%g'%rate)

  except ValueError:
    numberErrorMessageDollar()
    pass

    

def convertYen(Event=None):
  try:
    a = float(anEntry.get())
    currency_from="EUR"
    currency_to="JPY"
    y=unichr(165)
    rate=currencyConverter(currency_from,currency_to,a)
    s_label.configure(text=y+'%g'%rate)
  except ValueError:
    numberErrorMessageYen()
    pass
  


#*********************
#**Main GUI FRAME
#**create a new window/instance of the Tkinter class
root = Tk()
#**give the window a title
root.title("*John's Currency Exchange*")

#**Declare a Frame, call it "top" and place it in the root window
top = Frame(root)
top.pack(side='top')
#***Declare middle and bottom frame, then put them in, top means place them as high as they will go
middle=Frame(root)
middle.pack(side='top')
bottom=Frame(root)
bottom.pack(side='top')
#*********************
#***TITLE (create frame,add it to top position, (because there is nothing there yet
myFrame=Frame(top,bg="red")
myFrame.pack(side='top')
#**set font = 20, to make it a large header,set text,color etc.
font= 'times 20 bold'
myText = Label(myFrame,text='Euro Converter',font = font,fg="blue")
myText.pack(side='top',pady=5,padx=5)







#***********************
#***TO Sterling Section

aFrame = Frame(top,bg="white")
aFrame.pack(side='top',padx=10,pady=20)

#** format will look like  "label" | "entryBox" | "button" | "resultLabel"(that will be set from method)

#**Label
aLabel = Label(aFrame,text="Euro's : ")
aLabel.pack(side='left',padx=5,pady=5)

#**entryBox for input
anEntry= Entry(aFrame,width=10)
anEntry.pack(side='left')
anEntry.insert('end','1')#**place initial value inside box (optional)

#**The method that is called by one of the ways above will produce a value
#**the configure method will be used, assigning the value to the following label
s_label=Label(aFrame,width=15)
s_label.pack(side='left')



#**********************
#***TO DOLLAR SECTION
aFrame2 =Frame(top)
aFrame2.pack(side='top',padx=10,pady=20)
conversionDollar = Button(aFrame2,text="Convert -> Dollar",command=convertDollar)
conversionDollar.pack(side='left')


#**********************
#***TO yen SECTION
aFrame3 =Frame(top)
aFrame3.pack(side='top',padx=10,pady=20)
conversionYen = Button(aFrame3,text="Convert -> Yen",command=convertYen)
conversionYen.pack(side='left')


#***To Sterling
aFrame4 =Frame(top)
aFrame4.pack(side='top',padx=10,pady=20)
conversionSterling = Button(aFrame4,text="Convert -> Sterling",command=convertSterling)
conversionSterling.pack(side='left')


#**EXECUTE***********************************
root.mainloop()
