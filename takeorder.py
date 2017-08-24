import speech_recognition as sr
import pyttsx3
import makelist
import text2num
import pymysql
import inflect
import os

inf = inflect.engine()
engine = pyttsx3.init()
engine.setProperty("voice", "american")
engine.setProperty("rate", "140")
recog = sr.Recognizer()

notfound = False
creds = []
creds.insert(2, "")
try:
    config = open('.dbconfig', 'r').read()
    for i in config.splitlines():
        creds.insert(0, i)
    if creds[2] != "":
        creds[2], creds[0] = creds[0], creds[2]
        creds[1], creds[0] = creds[0], creds[1]
except FileNotFoundError:
    notfound = True
except IndexError:
    notfound=True

if (not notfound):
    try:
        con = pymysql.connect(host=creds[1], user=creds[0], passwd=creds[2], db='ultimate_drive_thru')
        cur = con.cursor()
    except Exception as e:
        os.rename("./.dbconfig","./.dbconfig.bak")
        open("./.dbconfig","w").close()

def takeorderfunction():


    finalod =[]
    print("INSTRUCTIONS: \n 1) Be clear \n 2) Mention Quantity, even for suborders \n 3) Avoid Repeating name for suborder")




    engine.say("hi. whats your name?")
    engine.runAndWait()
    while True:
        with sr.Microphone() as source:                             # use the default microphone as the audio source
           name = recog.listen(source)                            #recognise name
        try:
            name = str(recog.recognize_google(name))
            break
        except sr.UnknownValueError:
           engine.say("Oops! Didn't catch that")
           engine.runAndWait()
           continue
        except sr.RequestError as e:
            mess="Sorry Service is Unavailible at the moment"
            return mess




    engine.say("what would you like to eat?")
    engine.runAndWait()
    while True:
        with sr.Microphone() as source:                             # use the default microphone as the audio source
           order = recog.listen(source)                            # recognise order
        try:
            order=recog.recognize_google(order)
            print("You said " + order)      # recognize speech using Google Speech Recognition'''
            #order=input()                  #remove after testing
            break
        except sr.UnknownValueError:
            engine.say("Oops! Didn't catch that")
            engine.runAndWait()
            continue
        except sr.RequestError as e:
            mess = "Sorry Service is Unavailible at the moment"
            return mess




    order=order.lower()
    for word in makelist.spacethings:
        order=order.replace(word, word.replace(" ","_"))
    order = order.replace(" a ", " 1 ").replace(" a ", " 1 ")
    order = order.split()
    for k,v in enumerate(order):
        order[k]=str(text2num.text2num(str(v).lower()))
    #print(order)          #remove after testing
    mess="You said "+ " ".join(order)
    #print(finalod)
    finalod.extend(makelist.makeorder(order))
    print("before anyhting more", finalod)

    while True:
        engine.say("Anything more?")
        engine.runAndWait()

        while True:
            with sr.Microphone() as source:         # use the default microphone as the audio source
                add = recog.listen(source)      # recognise confirmtion
            try:
                add = str(recog.recognize_google(add))
                if add == "yes" or add == "no":
                    break
                else:
                    engine.say("please answer with yes or no. Anything more?")
                    engine.runAndWait()
                    continue
            except sr.UnknownValueError:
                engine.say("Oops! Didn't catch that")
                engine.runAndWait()
                continue
            except sr.RequestError as e:
                mess = "Sorry Service is Unavailable at the moment"
                return mess

        if add=="yes":
            engine.say("what would you like to add to your order")
            engine.runAndWait()
            while True:
                with sr.Microphone() as source:  # use the default microphone as the audio source
                    aorder = recog.listen(source)  # recognise order
                try:
                    aorder = str(recog.recognize_google(aorder))
                    print("You said " + aorder)  # recognize speech using Google Speech Recognition'''
                    # order=input()                  #remove after testing
                    break
                except sr.UnknownValueError:
                    engine.say("Oops! Didn't catch that. Please try again.")
                    engine.runAndWait()
                    continue
                except sr.RequestError as e:
                    mess = "Sorry Service is Unavailable at the moment"
                    return mess
            aorder = aorder.lower()
            for word in makelist.spacethings:
                aorder = aorder.replace(word, word.replace(" ", "_"))
            aorder = aorder.replace(" a ", " 1 ").replace(" a ", " 1 ")
            aorder = aorder.split()
            for k, v in enumerate(aorder):
                aorder[k] = str(text2num.text2num(str(v).lower()))
            # print(order)          #remove after testing
            mess =mess+ " + " + " ".join(aorder)
            finalod.extend(makelist.makeorder(aorder))
        if add=="no":
            break

    return finalod, mess, name


def confirmorder(finalod, mess, name):
    ordqu = []
    total=0
    print("before confiming" , finalod)
    engine.say("would yu like to confirm your order?")
    engine.runAndWait()

    while True:
        with sr.Microphone() as source:  # use the default microphone as the audio source
            confirm = recog.listen(source)  # recognise confirmtion
        try:
            confirm = str(recog.recognize_google(confirm))
            if confirm=="yes" or confirm=="no":
                break
            else:
                engine.say("please answer with yes or no. would you like to confirm your order?")
                engine.runAndWait()
                continue
        except sr.UnknownValueError:
            engine.say("Oops! Didn't catch that")
            engine.runAndWait()
            continue
        except sr.RequestError as e:
            mess = "Sorry Service is Unavailable at the moment"
            return mess

    if confirm=="yes":
        print("yes")
        #insert into transaction table
        for i in finalod:
            for j in i.split():
                if str(j).isnumeric():
                    qty=int(j)
                    i=str(i).replace(j,"")
                if j in makelist.burger+makelist.drinks+makelist.sandwiches+makelist.fries:
                    #print("here")
                    z=str(j).replace("_"," ")
                    if inf.singular_noun(z)!=False:
                        z=str(inf.singular_noun(z))
                    #print("z=",z)
                    qu="select price from Menu where item=%s"
                    cur.execute(qu, (z))
                    res=cur.fetchall()
                    for k in res:
                        price=int(k[0])*qty
                        total=int(total+price)
                        #print(price)
                    i=str(i).replace(j,"").strip()
            #print("i=",i)
            ordqu.append("insert into orders values(%s,"+str(qty)+ ",'" +str(z)+"','"+ str(i)+"',"+ str(price)+ ", 0 , default)")
        #print(ordqu)
        qu = "insert into transactions values(default, '"+ str(name) +"',"+ str(total)+")"
        #print(qu)
        cur.execute(qu)
        con.commit()
        TID=int(cur.lastrowid)
        mess+="%%"+str(TID)
        for query in ordqu:
            cur.execute(query,(TID))
            con.commit()
    if confirm=="no":
        engine.say("order cancelled")
        engine.runAndWait()
        mess="order cancelled"
        return mess
    print(mess)
    return mess
