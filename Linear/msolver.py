from matre import matre

def linhash(number):
    npat = ['u0', 'u1', 'u2', 'u3', 'u4', 'u5', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'r0', 'r1', 'r2', 'l0', 'l1', 'l2']
    digits = []
    if (number == 0):
        digits.append(0)
        number -= 1
    while(number >= 0):
        digits.append(number%18)
        if (number == 0):
            number -= 1
        else:
            number = number - (number%18)
            number = int(number/18)-1            
    
    digits.reverse()
    for a in range(len(digits)):
        digits[a] = npat[digits[a]]
    return digits
    

    
def patter(cmd, matre):
    if (cmd[0] == 'u'):
        matre.colshift('u', int(cmd[1]))
    elif (cmd[0] == 'd'):
        matre.colshift('d', int(cmd[1]))
    elif (cmd[0] == 'l'):
        matre.rowshift('l', int(cmd[1]))        
    elif (cmd[0] == 'r'):
        matre.rowshift('r', int(cmd[1]))
    else:
        print("Error: " + str(cmd))

def matresolver(ma):
    #Somewhere either here or in the linhash function serious optomization is possible by discarding moves that undo their previous one
    #It's also perhaps possible to regain one step of speed by having a loop here that for every matrix created to then subject it to all the moves except the opposite of the most recent one
    #It only helps speed it up by about one step though
    
    #Make a hybrid system where it goes 4 steps deep for each using the memory intensive method, then leapfrogs 5 moves ahead.
    count = 0
    tempmatre = ma.mcopy()
    itercount = 1
    while (True):
        commands = linhash(count)
        if (len(commands) > itercount):
            itercount = len(commands)
            print(itercount)
        for a in commands:
            patter(a, tempmatre)
        solved = tempmatre.checksolve()
        if (solved):
            tempmatre.printmatre()
            return (tempmatre.returnsteps())
        count += 1
        tempmatre = ma.mcopy()
            
    
    
    
def main():
    #create a matrix object of the matrix puzzle in question 
    smatre = matre([[9,5, 2], [6, 8, 4], [1, 3, 1], [2,7,6], [5,7,3], [4, 9, 8]])
    #print to check
    print(smatre.returnmatre())
    #Collect the result
    solution = matresolver(smatre)
    print(solution[1])
    print(solution[0])

if __name__ == '__main__':
    main()