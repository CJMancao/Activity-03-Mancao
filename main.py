import evComp as EV
import statComp as ST
import math

def tryAgain():
    select = int(input("\nDo you want to try again? \n[1] Yes  [2] No \nOption: "))
    if select == 1: main()
    elif select == 2: exit()
    else: 
        print("Invalid...")
        tryAgain()
        

def main():

    print("Pokemon STAT & EV Calculator\n\n")
    while True:
        base = int ( input ("Base HP: "))
        level = int ( input ("Level: "))
        ev = int ( input ("EV must be [0 - 255] \nEV: "))
        iv = int ( input ("IV must be [0 - 31] \nIV: "))
            
        if iv > 31:
            print("IV exceeds\n")  
            main() 

        if ev > 255:
            print("EV exceeds\n") 
            main()

        else:    
            print("Proceeding...")
            break

    while True:
        print(" \n[1] EV Calculator \n[2] Stat Calculator ")
        choice = int(input("\nInput your choice: "))
    
        if choice == 1:
            stats = int(input("Stats: "))
            ch= int(input("[1] Beneficial [2] Hindering \nModidier: "))
            if ch== 1:
                mod = 1.1

            elif ch== 2:
                mod = 0.9

            else:
                print("Invalid Input!")
            
            totalEV = EV.computeEv.computeEV(base, iv, ev, level, mod, stats)
            if totalEV <=500:
                print("Total EV:", totalEV)
            
            else:
                print("Pokemon's Total EV Exceeds!")
            tryAgain()
        

        elif choice == 2:
            choose = int(input("\nCompute other stats? [1] Yes [2] No \nSelect: "))
            if choose == 1: 
                chComp= str(input("\n[att] [def] [spatt] [spdef] [spd]\nWhat Stat would you like to compute?: "))    
                if chComp== 'att': 
                    chStats= 'Attack'   
                    sel= int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if sel== 1:
                        nat = 1.1

                    elif sel== 2:
                        nat = 0.9
                
                if chComp== 'def':
                    chStats= 'Defense'    
                    sel= int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if sel== 1:
                        nat = 1.1

                    elif sel== 2:
                        nat = 0.9
                
                if chComp== 'spatt':  
                    chStats= 'Special Attack'  
                    sel= int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if sel== 1:
                        nat = 1.1

                    elif sel== 2:
                        nat = 0.9

                if chComp== 'spdef':  
                    chStats= 'Special Defense'  
                    sel= int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if sel== 1:
                        nat = 1.1

                    elif sel== 2:
                        nat = 0.9

                if chComp== 'spd':    
                    chStats= 'Speed'
                    sel= int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if sel== 1:
                        nat = 1.1

                    elif sel== 2:
                        nat = 0.9
                
                other = ST.computeStats.otherStat(base, ev, level, iv, nat)
                if other <= 510:
                    print("\nComputing...\n", chStats,"Value =", other)
                
                else:
                    print("Pokemon's Total EV Exceeds!")
                tryAgain()

        elif chComp== 2:
            chp = ST.computeStats.health(base, ev, level, iv)
            if chp <= 510:
                print ("HP Value:", chp)
            else:
                print("Pokemon's Total EV Exceeds!")
            tryAgain()

        else:
            print("Invalid Input!")
                    

main()