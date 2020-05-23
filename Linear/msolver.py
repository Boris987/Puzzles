from matre import matre


    
def patter(locode, matre):
    copcode = locode[:]
    while len(copcode) != 0:
        cmd = copcode[0:2]
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
        copcode = copcode[2:]
def matresolver(ma):
    #This is the main function of the solver
    #npat stores all the possible moves
    npat = ['u0', 'u1', 'u2', 'u3', 'u4', 'u5', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'r0', 'r1', 'r2', 'l0', 'l1', 'l2']
    gen = [[], []]
    gen[0] = npat[:]
    for a in gen[0]:
        #The matrix is copied and every possible movement is done to it. All the matrices are stored in the second list of gen
        temmatre = ma.mcopy()
        patter(a, temmatre)
        gen[1].append(temmatre)
    for a in gen[1]:
        #In the off chance a solution is found immediately this loop checks for it
        if a.checksolve():
            return [a.returnsteps(), a.returnmatre()]
    itercount = 0
    while (True):
        newmatres = []
        for mat in gen[1]:
            for step in gen[0]:
                tempmat = mat.mcopy()
                patter(step, tempmat)
                if tempmat.checksolve():
                    return [tempmat.returnsteps(), tempmat.returnmatre()]
                newmatres.append(tempmat)
        gen[1] = newmatres
        itercount += 1
        print(itercount)
def main():
    #create a matrix object of the 
    smatre = matre([[9,5, 2], [6, 8, 4], [1, 3, 1], [2,7,6], [5,7,3], [4, 9, 8]])
    #print to check
    print(smatre.returnmatre())
    #Collect the result
    solution = matresolver(smatre)
    print(solution[1])
    print(solution[0])

if __name__ == '__main__':
    main()