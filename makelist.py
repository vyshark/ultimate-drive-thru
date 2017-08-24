import pymysql
burger= []                  #burgers
burgerext= []                #burger extras
sandwiches=[]               #sandwiches
fries=[]                     #fries
drinks= []                   #drinks
spacethings=[]
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

if(not notfound):

    try:
        con = pymysql.connect(host=creds[1], user=creds[0], passwd=creds[2], db='ultimate_drive_thru')
        cur=con.cursor()

        burgerqu="SELECT item FROM Menu WHERE typeid=1"
        swqu="SELECT item FROM Menu WHERE typeid=2"
        friesqu="SELECT item FROM Menu WHERE typeid=3"
        drinksqu="SELECT item FROM Menu WHERE typeid=4"
        extqu="SELECT item FROM Menu WHERE typeid=5"
        allitems={extqu:burgerext,burgerqu:burger,friesqu:fries,drinksqu:drinks,swqu:sandwiches}
        for k,v in allitems.items():
            cur.execute(k)
            res=cur.fetchall()
            for row in res:
                v.append(str(row[0]).replace(" ","_"))
                v.append(str(row[0]+'s').replace(" ", "_"))
                v.append(str(row[0] + 'es').replace(" ", "_"))
    except:
       print ("Error: unable to fetch data")


    for i in (burger+drinks+burgerext+sandwiches+fries):
        if "_" in i:
            i=str(i).replace("_"," ")
            spacethings.append(str(i))

suborder,od={},{}
tempso=[]
finalod=[]

def makeorder(order):
    finalod.clear()
    '''print(burger)
    print(drinks)
    print(fries)
    print(burgerext)
    print(sandwiches)
    print(spacethings)'''
    a = ""
    qty, flag, subtotal = 0, 0, 0
    for i,ord in enumerate(reversed(order)):                                #reverse travverse the string
        if ord.isnumeric():
            if flag==1:
                qty = ord
                if subtotal!=0:
                    if int(qty)-subtotal!=0:
                        finalod.append((str(int(qty)-subtotal)) + " " + item + " " + "normal")
                        subtotal=0
                    elif bool(suborder):
                        for k,v in suborder.items():
                            finalod.append(qty+" "+ item+" "+ v+" "+ k)
                else:
                    if bool(suborder):
                        for k, v in suborder.items():
                            if k==" NA ":
                                print("You did'nt specify your order correctly!\nYOU SAID :", ' '.join(order) , "\nSkipping this Part of the order.")
                                continue
                            a = a + " " + v + " " + k
                            finalod.append(qty +" "+ item +" "+ a)
                        suborder.clear()
                        a = ""
                    else:
                        finalod.append(qty + " " + item +" "+ "normal")
            elif flag==0:
                subqty = ord
                for k,v in suborder.items():
                    a= a+ " "+ v +" "+ k
                    w=k
                suborder.clear()
                od[a]=subqty
                a=""


        if ord.lower() in burgerext:                    #if word is an extra
            tempso.append(ord)
            if bool(od):
                for k,v  in od.items():
                    del od[k]
                    x=str(k).replace(" NA ", ord.lower())
                    od[x]=v



        if ord.lower()=="with":                         #if word is with
            if bool(tempso):
                for i in tempso:
                    suborder[i]="with"
                tempso.clear()
            elif bool(od):
                suborder[k]="with"
            else:
                suborder[" NA "]="without"
            flag = 0



        if ord.lower() == "without" or ord.lower() == "no":             #if word is without
            if bool(tempso):
                for i in tempso:
                    suborder[i] = "without"
                tempso.clear()
            elif bool(od):
                suborder[k]="with"
            else:
                suborder[" NA "]="without"
            flag=0


        if ord.lower() in  (burger+ drinks+sandwiches+fries):            #if word is a burger or drink
            if (ord.lower() in drinks+fries) and (bool(tempso) or bool(od) or bool(suborder)):
                print("cant have those extras with/without ", ord.lower(), "\nDefaulting to normal", ord.lower())
                tempso.clear()
                od.clear()
                suborder.clear()
            if bool(od):
                for k,v in od.items():
                    finalod.append(v+ " " + ord.lower() + " " + k)
                    subtotal=subtotal+int(v)
                od.clear()
            item = ord.lower()
            flag=1
    print(finalod)
    return finalod
