def enterData():
    pop = float(input("Enter population"))
    inf = float(input("Enter Initially Infected"))
    contact = float(input("Enter contact rate"))
    rec = float(input("Enter recovery period"))
    return pop, inf, contact, rec

def sim(pop, inf, contact, rec):
    # Calc rec rate
    
    cr = contact
    r = 1/rec
    
    # initialize SIR
    s_val = pop - inf
    i_val = inf
    r_val = 0
    day = 0
    
    print (f"Day {day} : {s_val, i_val, r_val}")
    day += 1
    
    while i_val >= 0.5:
        # calculate s for day
        s_next = s_val - cr * i_val * s_val
        # calculate i for day
        i_next = i_val + cr * i_val * s_val - r * i_val
        # calculate r for day
        r_next = r_val + r * i_val
        # print the day
        print (f"Day {day} : {s_val, i_val, r_val}")
        s_val = s_next
        i_val = i_next
        r_val = r_next
        day += 1
        
        
    
def main():
    pop, inf, contact, rec = enterData()
    sim(pop, inf, contact, rec)

    


main()

        
    