def Description()-> str:
    VERSION= 1.0
    print ("VERSION {0}".format(VERSION))
    print("Decision Maker is a quick python script I wrote one day at work\nunsure about whether to buy a snack being broke but also starving")
    return None
def Decisionmaking()-> str:
    Description()
    decision=input("please enter a short description of your decision in this format: GOING TO THE GYM where you know that the statement is the obvious right decision to make: ")
    pros=0
    cons=0
    pro=input("please enter a benefit of {}\nIf there are no benefits just hit enter!".format(decision))
    #Maybe assign weight later
    #The reason for hesitating about weights is because I want the script to remain as simple as possible
    #weight can be added by changing the PROS data sructure into a dictionnary and using the pros as key and the wight as value
    #maybe an example later
    while pro != "":
        pros+= 1
        pro=input("please enter another advantage of {}: ".format(decision))
        
    con=input("please enter a drawback of {}\nIf there are no drawbacks just hit enter! ".format(decision))    
    while con != "":
        cons+= 1
        con=input("please enter another drawback of {}: ".format(decision))
    
    if cons<pros:
        print("U should definitely {0}!!".format(decision))
        
    elif cons>pros:
        print("U should not {0}!!".format(decision))
        
    else: 
        print("Bruh!! please retry and be honest or try another version of the script")
        
    print("THANK YOU FOR TRUSTING MY DECISION SCRIPT!!!")
    
Decisionmaking()
