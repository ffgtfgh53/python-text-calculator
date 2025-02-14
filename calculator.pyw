import re
import math
import ttkbootstrap as ttk

#window
window = ttk.Window(title = "Text Calculator",
                    themename = "flatly",
                    size=[500,700])
window.iconbitmap("c:/Users/Jovie/OneDrive/Desktop/Python Code/images/calc.ico")
window.grid_columnconfigure(0,weight=1)
window.grid_rowconfigure(0,weight=2)
window.grid_rowconfigure(1,weight=5)

#text var
entrytext = ttk.StringVar(value = "1+1")
resulttext = ttk.StringVar()
errortext = ttk.StringVar()

#topframe
topframe = ttk.LabelFrame(master = window, padding = 10,text="Kakalulatorrr")
topframe.grid(column=0,row=0,)

#bottomframe
bottomframe = ttk.Frame(window,padding = 5)
bottomframe.grid(column=0,row=1,sticky="nsew")
bottomframe.columnconfigure(0,weight=1,pad=5)
bottomframe.columnconfigure(1,weight=1,pad=5)
bottomframe.columnconfigure(2,weight=1,pad=5)
bottomframe.columnconfigure(3,weight=1,pad=5)
bottomframe.columnconfigure(4,weight=1,pad=5)
bottomframe.rowconfigure(0,weight=1,pad=5,minsize=88)
bottomframe.rowconfigure(1,weight=1,pad=5,minsize=88)
bottomframe.rowconfigure(2,weight=1,pad=5,minsize=88)
bottomframe.rowconfigure(3,weight=1,pad=5,minsize=88)
bottomframe.rowconfigure(4,weight=1,pad=5,minsize=88)

#equation_label
out_label = ttk.Label(master = topframe,textvariable=resulttext,font='Helvetica 8',justify="left")
out_label.pack(pady=10,expand=True)

#entry
entry = ttk.Entry(master = topframe, textvariable=entrytext,justify = "center",width=450)
entry.pack(expand = True)

#error_label
error_label = ttk.Label(topframe,textvariable=errortext,justify="left",style="danger")
error_label.pack(expand=True)

def calculate():
    errortext.set("")
    to_calc = entrytext.get()
    number_search = re.search(r"\d", to_calc)
    if number_search == None:
        errortext.set("where are the numbers bro???")
        return
    formatted = formatinput(to_calc)
    P_resolved = calcP(formatted)
    if errortext.get() != "":
        resulttext.set("")
        return
    try:
        result = str(f"{float(pEDMAS(P_resolved)):g}")
    except:
        errortext.set("unknown error occured")
        return
    print(result)
    if errortext.get() == "":
        resulttext.set(to_calc+"=")
        entrytext.set(result)
    else:
        resulttext.set("")


#calculate button
calc_button = ttk.Button(master = topframe,width=400,command=calculate,padding=10,text="Calculate")
calc_button.pack(pady=10)



#button func
#sin buttonfunc
def sinbuttonfunc():
    entrytext.set(entrytext.get()+"sin(")
#cos buttonfunc
def cosbuttonfunc():
    entrytext.set(entrytext.get()+"cos(")
#tan buttonfunc
def tanbuttonfunc():
    entrytext.set(entrytext.get()+"tan(")
#log buttonfunc
def logbuttonfunc():
    entrytext.set(entrytext.get()+"log(")
#sqrt buttonfunc
def sqrtbuttonfunc():
    entrytext.set(entrytext.get()+"sqrt(")
#one buttonfunc
def onebuttonfunc():
    entrytext.set(entrytext.get()+"1")
#two buttonfunc
def twobuttonfunc():
    entrytext.set(entrytext.get()+"2")
#three buttonfunc
def threebuttonfunc():
    entrytext.set(entrytext.get()+"3")
#four buttonfunc
def fourbuttonfunc():
    entrytext.set(entrytext.get()+"4")
#five buttonfunc
def fivebuttonfunc():
    entrytext.set(entrytext.get()+"5")
#six buttonfunc
def sixbuttonfunc():
    entrytext.set(entrytext.get()+"6")
#seven buttonfunc
def sevenbuttonfunc():
    entrytext.set(entrytext.get()+"7")
#eight buttonfunc
def eightbuttonfunc():
    entrytext.set(entrytext.get()+"8")
#nine buttonfunc
def ninebuttonfunc():
    entrytext.set(entrytext.get()+"9")
#zero buttonfunc
def zerobuttonfunc():
    entrytext.set(entrytext.get()+"0")
#dot buttonfunc
def dotbuttonfunc():
    entrytext.set(entrytext.get()+".")
#obracket buttonfunc
def obracketbuttonfunc():
    entrytext.set(entrytext.get()+"(")
#cbracket buttonfunc
def cbracketbuttonfunc():
    entrytext.set(entrytext.get()+")")
#exponent buttonfunc
def exponentbuttonfunc():
    entrytext.set(entrytext.get()+"^")
#plus buttonfunc
def plusbuttonfunc():
    entrytext.set(entrytext.get()+"+")
#minus buttonfunc
def minusbuttonfunc():
    entrytext.set(entrytext.get()+"-")
#times buttonfunc
def timesbuttonfunc():
    entrytext.set(entrytext.get()+"*")
#divide buttonfunc
def dividebuttonfunc():
    entrytext.set(entrytext.get()+"/")
#delbuttonfunc
def delbuttonfunc():
    entryinput = entrytext.get()
    entryoutput = re.sub(r"([a-zA-Z]+|[^a-zA-Z])$","",entryinput)
    entrytext.set(entryoutput)

#button
#row0
sinbutton = ttk.Button(bottomframe,text = "sin",cursor="hand2",command=sinbuttonfunc,style="info")
sinbutton.grid(row = 0,column= 0,sticky="nsew",padx=5,pady=5)
cosbutton = ttk.Button(bottomframe,text = "cos",cursor="hand2",command=cosbuttonfunc,style="info")
cosbutton.grid(row = 0,column= 1,sticky="nsew",padx=5,pady=5)
tanbutton = ttk.Button(bottomframe,text = "tan",cursor="hand2",command=tanbuttonfunc,style="info")
tanbutton.grid(row = 0,column= 2,sticky="nsew",padx=5,pady=5)
logbutton = ttk.Button(bottomframe,text = "log",cursor="hand2",command=logbuttonfunc,style="info")
logbutton.grid(row = 0,column= 3,sticky="nsew",padx=5,pady=5)
sqrtbutton = ttk.Button(bottomframe,text = "sqrt",cursor="hand2",command=sqrtbuttonfunc,style="info")
sqrtbutton.grid(row = 0,column= 4,sticky="nsew",padx=5,pady=5)
#row1
onebutton = ttk.Button(bottomframe,text = "1",cursor="hand2",command=onebuttonfunc,style="info")
onebutton.grid(row = 1,column= 0,sticky="nsew",padx=5,pady=5)
twobutton = ttk.Button(bottomframe,text = "2",cursor="hand2",command=twobuttonfunc,style="info")
twobutton.grid(row = 1,column= 1,sticky="nsew",padx=5,pady=5)
threebutton = ttk.Button(bottomframe,text = "3",cursor="hand2",command=threebuttonfunc,style="info")
threebutton.grid(row = 1,column= 2,sticky="nsew",padx=5,pady=5)
plusbutton = ttk.Button(bottomframe,text = "+",cursor="hand2",command=plusbuttonfunc,style="info")
plusbutton.grid(row = 1,column= 3,sticky="nsew",padx=5,pady=5)
minusbutton = ttk.Button(bottomframe,text = "-",cursor="hand2",command=minusbuttonfunc,style="info")
minusbutton.grid(row = 1,column= 4,sticky="nsew",padx=5,pady=5)
#row2
fourbutton = ttk.Button(bottomframe,text = "4",cursor="hand2",command=fourbuttonfunc,style="info")
fourbutton.grid(row = 2,column= 0,sticky="nsew",padx=5,pady=5)
fivebutton = ttk.Button(bottomframe,text = "5",cursor="hand2",command=fivebuttonfunc,style="info")
fivebutton.grid(row = 2,column= 1,sticky="nsew",padx=5,pady=5)
sixbutton = ttk.Button(bottomframe,text = "6",cursor="hand2",command=sixbuttonfunc,style="info")
sixbutton.grid(row = 2,column= 2,sticky="nsew",padx=5,pady=5)
timesbutton = ttk.Button(bottomframe,text = "*",cursor="hand2",command=timesbuttonfunc,style="info")
timesbutton.grid(row = 2,column= 3,sticky="nsew",padx=5,pady=5)
dividebutton = ttk.Button(bottomframe,text = "/",cursor="hand2",command=dividebuttonfunc,style="info")
dividebutton.grid(row = 2,column= 4,sticky="nsew",padx=5,pady=5)

#row3
sevenbutton = ttk.Button(bottomframe,text = "7",cursor="hand2",command=sevenbuttonfunc,style="info")
sevenbutton.grid(row = 3,column= 0,sticky="nsew",padx=5,pady=5)
eightbutton = ttk.Button(bottomframe,text = "8",cursor="hand2",command=eightbuttonfunc,style="info")
eightbutton.grid(row = 3,column= 1,sticky="nsew",padx=5,pady=5)
ninebutton = ttk.Button(bottomframe,text = "9",cursor="hand2",command=ninebuttonfunc,style="info")
ninebutton.grid(row = 3,column= 2,sticky="nsew",padx=5,pady=5)
exponentbutton = ttk.Button(bottomframe,text = "^",cursor="hand2",command=exponentbuttonfunc,style="info")
exponentbutton.grid(row = 3,column= 3,sticky="nsew",padx=5,pady=5)
delbutton = ttk.Button(bottomframe,text = "⌫",cursor="hand2",command=delbuttonfunc,style="info")
delbutton.grid(row = 3,column= 4,sticky="nsew",padx=5,pady=5)
#row4
dotbutton = ttk.Button(bottomframe,text = ".",cursor="hand2",command=dotbuttonfunc,style="info")
dotbutton.grid(row = 4,column= 0,sticky="nsew",padx=5,pady=5)
zerobutton = ttk.Button(bottomframe,text = "0",cursor="hand2",command=zerobuttonfunc,style="info")
zerobutton.grid(row = 4,column= 1,sticky="nsew",padx=5,pady=5)
obracketbutton = ttk.Button(bottomframe,text = "(",cursor="hand2",command=obracketbuttonfunc,style="info")
obracketbutton.grid(row = 4,column= 2,sticky="nsew",padx=5,pady=5)
cbracketbutton = ttk.Button(bottomframe,text = ")",cursor="hand2",command=cbracketbuttonfunc,style="info")
cbracketbutton.grid(row = 4,column= 3,sticky="nsew",padx=5,pady=5)
calbutton = ttk.Button(bottomframe,text = "=",cursor="hand2",command=calculate,style="info")
calbutton.grid(row = 4,column= 4,sticky="nsew",padx=5,pady=5)




#cleaning and formatting input
def formatinput(entry):
    cleaned_space = re.sub(r"\s","",entry)
    formatx = re.sub(r"x","*",cleaned_space)
    formatslash = re.sub(r"\\","/",formatx)
    format_eplus = re.sub(r"(\d+|\d+\.\d+)+e\+\d+",lambda entry:str(f"{float(entry.group(0)):f}"),formatslash)
    # 0()()tan() -> 0*()*()*tan()
    disambiguatex = re.sub(r"((?<=\)|\d)(?=\(|[sctl]))","*",format_eplus)
    return disambiguatex

#stage Pedmas
def calcP(parenthesistring):
    result = parenthesistring
    while re.search(r"(\(|\))",result) != None:
        result2 = re.sub(r"\([^\(]+?\)",pEDMAS,result,1)
        #check for parenthesis error
        if result2 == result:
            errortext.set("parenthesis error, check again")
            print("parenthesis error, check again")
            break
        else:
            result = result2
    print(result)
    return result

#stage pEdmas
def calcE(Eentry):
    no1, no2 = re.findall(r"[0-9\.]+",Eentry.group(0))
    try:
        print("bananas")
        return f'{float(no1)**float(no2):f}'
    except:
        errortext.set("result too large")
        print("yeahhh")
        return "0"

#stage pedmas (ooops which stage is sin cos tan log sqrt )
def calctext(textentry):
    text = re.search(r"[a-zA-Z]+",textentry.group(0)).group(0)
    number = float(re.search(r"[0-9\.]+",textentry.group(0)).group(0))
    try:
        function = getattr(math, text)
        return(str(f"{function(number):f}"))
    except:
        errortext.set("unidentified function \""+text+"\"")
        print("unidentified function \""+text+"\"")
    
#stage peDMas
def calcDM(DMentry):
    no1, no2 = re.findall(r"[0-9\.\-]+",DMentry.group(0))
    if re.search("\*",DMentry.group(0)) == None:
        return str(float(no1)/float(no2))
    else:
        return str(float(no1)*float(no2))
    
#stage pedmAS
def calcAS(ASentry):
    no1, no2 = re.findall(r"[0-9\.]+",ASentry.group(0))
    if re.search("\+",ASentry.group(0)) == None:
        return str(float(no1)-float(no2))
    else:
        return str(float(no1)+float(no2))

#stage pEDMAS (wow so smart)
def pEDMAS(entry):
    try:
        calctedP = entry.group(0) #for when called by Pedmas()
    except:
        calctedP = str(entry)
    calctedP = re.sub(r"(\(|\))","",calctedP) #when called by Pedmas() still contains parenthesis

    while re.search("\^",calctedP) != None:
        calctedE = re.sub(r"[0-9\.]+\^[0-9\.]+",calcE,calctedP,1)
        #makes sure procedes left to right one at a time
        #wont skip cases like 5^5^5^5 -> 25^25
        if calctedE == calctedP:
            errortext.set("exponent error, wrong plaement of ^")
            print("exponent error, wrong plaement of ^")
            break #checks for wrong placement of ^ like 3^*5 or ^3
        calctedP = calctedE
    calctedE = calctedP #if no exponent to make sure calctedE has value
    print(calctedE)
    calctedT = re.sub(r"([a-zA-Z]{2,5})([0-9\.]+)",calctext,calctedE)
    search_text = re.search(r"[a-zA-Z]+", calctedT)
    if search_text != None:
        errortext.set("unidentified function \""+search_text.group(0)+"\"")
        print("unidentified function \""+search_text.group(0)+"\"")
    #impossibe to skip over text
    print(calctedT)

    while re.search(r"(\*|\/)",calctedT) != None:
        calctedDM = re.sub(r"[0-9\.]+(\*|\/)[0-9\-][0-9\.]*",calcDM,calctedT,1)
        if calctedDM == calctedT:
            errortext.set("multiply/divide error, wrong placement of * or /")
            print("multiply/divide error, wrong placement of * or /")
            calctedDM = 0
            break
        calctedT = calctedDM
    calctedDM = calctedT
    print(calctedDM)
    calctedDM = re.sub(r"\+\-","-",calctedDM)
    calctedDM = re.sub(r"\-\-","+",calctedDM) #resolves cases of +- formed from negative numbers
    while re.search(r"(?<=\d)(\+|\-)",calctedDM) != None:
        calctedAS = re.sub(r"[0-9\.]+(\+|\-)[0-9\.]+",calcAS,calctedDM,1)
        if calctedAS == calctedDM:
            errortext.set("add/subtract error, wrong placement of + or -")
            print("add/subtract error, wrong placement of + or -")
            calctedAS = 0
            break
        calctedDM = calctedAS
    calctedAS = calctedDM
    return calctedAS




window.mainloop()