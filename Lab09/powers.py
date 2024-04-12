# Author: Teddy Nueva Espana
# Date: 4/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: Program defines and uses a recursive power function

def powers(base, exponent):
    print(f"powers({base}, {exponent})")
    if exponent == 1:
        return base
    else:
        return base * powers(base, (exponent-1))
    
def main():
    base = int(input("Enter base: "))
    exp = int(input(("Enter exponent: ")))
    result = powers(base, exp)
    print(f"{base}^{exp} = {result}")
main()