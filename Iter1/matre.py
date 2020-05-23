#This file stores the matrix (matre) object
class matre(object):
    def __init__(self, array):
        self.tmatr = array[:]
        #steps keeps track of all the changes or steps taken so far in solving
        self.steps = []
    def mcopy(self):
        #simple copy returner
        newmat = matre(self.tmatr[:])
        return newmat
    def colshift(self, dire, col):
        #dire stands for direction and should be a character, col is an int from 0-2
        if (dire == "u"):
            #redirect to sub method
            self.shiftup(col)
            #add a step
            self.steps.append('u'+str(col))
        elif (dire == "d"):
            #redirect to sub method
            self.shiftdown(col)
            #add a step
            self.steps.append('d'+str(col))
    def rowshift(self, dire, row):
        if (dire == "r"):
            self.rowright(row)
            self.steps.append('r'+str(row))
        elif (dire == "l"):
            self.rowleft(row)
            self.steps.append('l'+str(row))
    
    def checksolve(self):
    #This function needs the most revision
        #Checks to see if the solve conditions are met
        #First I check for no duplicates
        for a in range(3):
            for b in range(3):
                if ((a != 2) or (b != 2)):
                    if (self.tmatr[a][b] == self.tmatr[a+3][b]):
                        return False
            #column check
        for a in self.tmatr:
            if sum(a) != 15:
                return False
            #row check
        for a in range(3):
            ltot = 0
            rtot = 0
            for b in range(3):
                ltot += self.tmatr[b][a]
                rtot += self.tmatr[b+3][a]
            if ((ltot != 15) or (rtot != 15)):
                return False
            #diagonal down
        ltot = 0
        rtot = 0    
        for a in range(3):
            ltot += self.tmatre[a][a]
            rtot += self.tmatre[a+3][a]
        if ((ltot != 15) or (rtot != 15)):
            return False
            #Diagonal up
        ltot = 0
        rtot = 0    
        for a in range(3):
            for b in reversed(range(3)):
                ltot += self.tmatre[a][b]
                rtot += self.tmatre[a+3][b]
        if ((ltot != 15) or (rtot != 15)):
            return False 
        return True
        #Helper methods
    def returnsteps(self):
        return (self.steps)        
    def returnmatre(self):
        return (self.tmatr)        
    def shiftup(self, col):
        #Given a column, it will bring all of its numbers up a slot
        keep = (self.tmatr[col])[:]
        self.tmatr[col][0] = keep[1]
        self.tmatr[col][1] = keep[2]
        self.tmatr[col][2] = keep[0]  
    def shiftdown(self, col):
        #Given a column, it will bring all of its numbers down a slot
        keep = (self.tmatr[col])[:]
        self.tmatr[col][0] = keep[2]
        self.tmatr[col][1] = keep[0]
        self.tmatr[col][2] = keep[1] 
    def rowright(self, row):
        #Given a row it will bring all of its numbers to the right
        keep = self.tmatr[5][row]
        for a in reversed(range(5)):
            self.tmatr[a+1][row] = self.tmatr[a][row]
        self.tmatr[0][row] = keep
    def rowleft(self, row):
        #Given a row it will bring all of its numbers to the left
        keep = int(self.tmatr[0][row])
        for a in range(5):
            self.tmatr[a][row] = self.tmatr[a+1][row]            
        self.tmatr[5][row] = keep
    def printmatre(self):
        for a in range(3):
            line = ""
            for col in self.tmatr:
                line += str(col[a])
            print(line)