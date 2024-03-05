def enterData():
    pop = float(input("Enter population"))
    inf = float(input("Enter Initially Infected"))
    contact = float(input("Enter contact rate"))
    rec = float(input("Enter recovery period"))
    return pop, inf, contact, rec

def analysis(S_List, I_List, R_List):
#    maxInf = I_List.find(max(I_List))
    maxDay = I_List.index(max(I_List))
    maxInf = I_List[maxDay]
    outbreakLength = len(S_List)
    print("Highest infected count = ", '{0:.2f}'.format(maxInf))
    print("Day of highest infected count = ", maxDay)
    print("Length of outbreak: ", outbreakLength, "Days")

def sim(pop, inf, contact, rec, S_List, I_List, R_List):
    # Calc rec rate
    
    cr = contact
    r = 1/rec
    
    # initialize SIR
    s_val = pop - inf
    i_val = inf
    r_val = 0
    day = 0

    S_List = []
    I_List = []
    R_List = []
    
    
    print (f"Day {day} : {s_val, i_val, r_val}")
    S_List.append(s_val)
    I_List.append(i_val)
    R_List.append(r_val)
    
    day += 1
    
    while i_val >= 0.5:
        # calculate s for day
        s_next = s_val - cr * i_val * s_val
        S_List.append(s_next)
        # calculate i for day
        i_next = i_val + cr * i_val * s_val - r * i_val
        I_List.append(i_next)
        # calculate r for day
        r_next = r_val + r * i_val
        R_List.append(r_next)
        # print the day
        print (f"Day {day} : {s_val, i_val, r_val}")
        s_val = s_next
        i_val = i_next
        r_val = r_next
        day += 1
        
    return S_List, I_List, R_List

        
def main():
    pop, inf, contact, rec = enterData()
    S_List = []
    I_List = []
    R_List = []
    
    S_List, I_List, R_List = sim(pop, inf, contact, rec, S_List, I_List, R_List)
    
    analysis(S_List, I_List, R_List)
    

main()

        
    