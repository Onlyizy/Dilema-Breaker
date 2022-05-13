def Description()-> str:
    VERSION= 1.0
    print ("VERSION {0}".format(VERSION))
    print("Dilema Breaker is a quick python script I wrote one day at work\nunsure about whether to buy a snack being broke but also starving")
    return None
def Decisionmaking()-> str:
    Description()
    decision=input("please enter a short description of your decision in this format: GOING TO THE GYM\n")
    pros=0
    cons=0
    pro=input("please enter a benefit of {}\nIf there are no benefits just hit enter!\n".format(decision))
    #Maybe assign weight later
    #The reason for hesitating about weights is because I want the script to remain as simple as possible
    #weight can be added by changing the PROS data sructure into a dictionnary and using the pros as key and the weight as value
    #maybe an example later
    while pro != "":
        pros+= 1
        pro=input("please enter another advantage of {}:\n".format(decision))
    con=input("please enter a drawback of {}\nIf there are no drawbacks just hit enter!\n".format(decision))    
    while con != "":
        cons+= 1
        con=input("please enter another drawback of {}:\n".format(decision))
    keyword=decision.split()[0].lower()
    if keyword[-1]=="g" and keyword[-2]=="n" and keyword[-3]=="i":
        keyword=keyword.replace("ing","")
        decision=decision.replace(decision.split()[0],keyword) 
    if cons<pros:
        print("You should definitely {0}!!".format(decision))
    elif cons>pros:
        print("You should not {0}!!".format(decision))
    else: 
        print("Unfortunately this script cannot help you I am currently working on an improved version!!\n Stay tuned on my GitHub and thank for the support!")
    print("THANK YOU FOR TRUSTING MY DECISION SCRIPT!!!")
Decisionmaking()
