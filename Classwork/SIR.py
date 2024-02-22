def enterData():
    pop = input("Enter population")
    inf = input("Enter Initially Infected")
    contact = input("Enter contact rate")
    rec = input("Enter recovery period")
    return pop, inf, contact, rec

def sim(pop, inf, contact, rec):
    # Calc rec rate
    
    cr = 1/contact
    r = rec
    
    # initialize SIR
    s_val = pop - 1
    i_val = inf
    r_val = 0
    day = 0
    
    while i_val > 0.5 :
        # calculate s for day
        s_val = s_val - (cr*i_val*s_val)
        # calculate i for day
        i_val = i_val + (cr*i_val*s_val) - r*i_val
        # calculate r for day
        r_val = r_val + (r*i_val)
        # print the day
        print ("Day", day ":" format(s_val, .2), format(i_val, .2), format(i_val, .2))
        day += 1
        
        
    
def main():
    
    sim()

main()

        
    