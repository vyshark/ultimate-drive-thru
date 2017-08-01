burger= ["mcaloo", "mcchicken"]                             #burgers
burgerext= ["cheese", "lettuce", "kethup"]                  #burger extras
drinks= ["Coke", "pepsi", "milkshake"]                      #drinks
drinksext= ["ice"]                                          #drinks Extras
suborder,od={},{}
tempso=[]


def makeorder(order):
    a = ""
    qty, flag, subtotal = 0, 0, 0
    for i,ord in enumerate(reversed(order)):                                #reverse travverse the string
        if ord.isnumeric():                                                 #if word is a number
            print("found number")
            if flag==1:
                qty = ord
                if subtotal!=0:
                    if int(qty)-subtotal!=0:
                        print(int(qty)-subtotal, item, "(normal)")
                        subtotal=0
                    elif bool(suborder):
                        for k,v in suborder.items():
                            print(qty, item, v, k)
                else:
                    if bool(suborder):
                        for k, v in suborder.items():
                            a = a + " " + v + " " + k
                            print(qty, item, a)
                        suborder.clear()
                        a = ""
                    else:
                        print(qty, item, "(normal)")
            elif flag==0:
                subqty = ord
                for k,v in suborder.items():
                    a= a+ " "+ v +" "+ k
                suborder.clear()
                od[a]=subqty
                a=""


        if ord.lower() in burgerext:                    #if word is an extra
            tempso.append(ord)



        if ord.lower()=="with":                         #if word is with
            for i in tempso:
                suborder[i]="with"
            tempso.clear()
            flag=0



        if ord.lower() == "without" or ord.lower() == "no":             #if word is without
            for i in tempso:
                suborder[i] = "without"
            tempso.clear()
            flag=0


        if ord.lower() in  burger:                                       #if word is a burger
            if bool(od):
                for k,v in od.items():
                    print(v, ord.lower(), k)
                    subtotal=subtotal+int(v)
                od.clear()
            item = ord.lower()
            flag=1
