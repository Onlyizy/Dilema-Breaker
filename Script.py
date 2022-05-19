def Description()-> None:
    VERSION= 2.0
    print ("VERSION {0}".format(VERSION))
    print("Dilema Breaker is a quick python script I wrote one day at work\nunsure about whether to buy a snack")
    return None

def Decisionmaking()-> None:
    Description()
    decision=input("please enter a short description of your decision in this format: GOING TO THE GYM\n")
    pro_count=0
    con_count=0
    pro=input("please enter a benefit of {}\nIf there are no benefits just hit enter!\n".format(decision)) #I can add support for the ing/preterit
    #Maybe assign weight later
    #The reason for hesitating about weights is because I want the script to remain as simple as possible
    #weight can be added by changing the PROS data sructure into a dictionnary and using the pros as key and the weight as value
    #maybe an example later
    while pro != "":
        pro_count+= 1
        pro=input("please enter another advantage of {}:\n".format(decision))
    con=input("please enter a drawback of {}\nIf there are no drawbacks just hit enter!\n".format(decision))    
    while con != "":
        con_count+= 1
        con=input("please enter another drawback of {}:\n".format(decision))
    keyword=decision.split()[0].lower()
    if keyword[-1]=="g" and keyword[-2]=="n" and keyword[-3]=="i":
        keyword=keyword.replace("ing","")
        decision=decision.replace(decision.split()[0],keyword) 
    if con_count<pro_count:
        print("You should definitely {0}!!".format(decision))
    elif con_count>pro_count:
        print("You should not {0}!!".format(decision))
    else: 
        print("Unfortunately this script cannot help you I am currently working on an improved version!!\n Stay tuned on my GitHub and thank for the support!")
    print("THANK YOU FOR TRUSTING MY DECISION SCRIPT!!!")
Decisionmaking()

def Decisionmaking2()->None:
    Description()
    decision=input("please enter a short description of your decision in this format: GOING TO THE GYM\n")
    pro_tracker={}
    con_tracker={}
    pro_count=0
    con_count=0
    pro=input("please enter a benefit of {}\nIf there are no benefits just hit enter!\n".format(decision))
    while pro!="":
        weight=int(input("please enter a weight to that parameter(1 for not so important, 5 for very important)\n")) #add support if ppl try to enter out of the range or strings
        pro_count+=1
        pro_tracker.setdefault(pro,int(weight))
        pro=input("please enter another benefit of {}\n".format(decision))
    con=input("please enter a drawback of {}\nIf there are no drawbacks just hit enter!\n".format(decision))
    while con!="":
        weight=int(input("please enter a weight to that parameter(1 for not so important, 5 for very important)\n"))
        con_count+=1
        con_tracker.setdefault(con,int(weight))
        pro=input("please enter another benefit of {}\n".format(decision))
        
