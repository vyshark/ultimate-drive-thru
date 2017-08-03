burger= ["Mcaloo", "Mcchicken"]                             #burgers
burgerext= ["cheese", "lettuce", "ketchup"]                  #burger extras
drinks= ["Coke", "pepsi", "chocolate milkshake", "strawberry milkshake"]           #drinks
suborder,od={},{}
tempso=[]


def makeorder(order):
    a = ""
    qty, flag, subtotal = 0, 0, 0
    for i,ord in enumerate(reversed(order)):                                #reverse travverse the string
        if ord.isnumeric():
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
                            if k==" NA ":
                                print("You did'nt specify your order correctly!\nYOU SAID :", ' '.join(order) , "\nSkipping this Part of the order.")
                                continue
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


        if ord.lower() in  burger or ord.lower() in  drinks:            #if word is a burger or drink
            if (ord.lower() in drinks) and (bool(tempso) or bool(od) or bool(suborder)):
                print("cant have those extras with/without ", ord.lower(), "\nDefaulting to normal", ord.lower())
                tempso.clear()
                od.clear()
                suborder.clear()
            if bool(od):
                for k,v in od.items():
                    print(v, ord.lower(), k)
                    subtotal=subtotal+int(v)
                od.clear()
            item = ord.lower()
            flag=1
