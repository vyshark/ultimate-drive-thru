import speech_recognition as sr
import pyttsx3
import makelist
import text2num
import pymysql
import inflect



def takeorderfunction():
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

    if (not notfound):
        inf = inflect.engine()
        con = pymysql.connect(host=creds[1], user=creds[0], passwd=creds[2], db='ultimate_drive_thru')
        cur = con.cursor()
    total=0
    ordqu = []
    finalod =[]
    print("INSTRUCTIONS: \n 1) Be clear \n 2) Mention Quantity, even for suborders \n 3) Avoid Repeating name for suborder")
    engine= pyttsx3.init()
    engine.setProperty("voice", "american")
    engine.setProperty("rate", "140")
    engine.say("hello, what would you like to eat?")
    engine.runAndWait()

    recog = sr.Recognizer()
    with sr.Microphone() as source:                             # use the default microphone as the audio source
       order = recog.listen(source)                            # listen for the first phrase and extract it into audio data
    try:
        order=recog.recognize_google(order)
        print("You said " + order)      # recognize speech using Google Speech Recognition'''
        #order=input()         #remove after testing
        order=order.lower()
        for word in makelist.spacethings:
            order=order.replace(word, word.replace(" ","_"))
        order = order.replace(" a ", " 1 ").replace(" a ", " 1 ")
        order = order.split()
        for k,v in enumerate(order):
            order[k]=str(text2num.text2num(str(v).lower()))
        #print(order)          #remove after testing
        mess="You said "+ " ".join(order)
        print(finalod)
        finalod=makelist.makeorder(order)
        print(finalod)
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
            ordqu.append("insert into orders values(%s,"+str(qty)+ ",'" +str(z)+"','"+ str(i)+"',"+ str(price)+ ")")
        #print(ordqu)
        name=input("whats your name?")
        qu = "insert into transactions values(default, '"+ str(name) +"',"+ str(total)+")"
        #print(qu)
        cur.execute(qu)
        con.commit()
        TID=int(cur.lastrowid)
        mess+="%%"+TID
        for query in ordqu:
            cur.execute(query,(TID))
            con.commit()

    except sr.UnknownValueError:
       print("Oops! Didn't catch that")
       mess="error"
    except sr.RequestError as e:
        print("Sorry Service is Unavailible at the moment")
    return mess