peg1 = [3, 2, 1] #last index (1 for this case) is at the top
peg2 = []        #empty peg
peg3 = []        #empty peg
pegs = [peg1, peg2, peg3]
validPegs = [] 
validPegs.append(list(map(list, pegs))) #adds initial state to the list of valid pegs

def isValid(pegs):#checks if generated state is already generated
    if(pegs in validPegs):
        return False
    return True

def stateGenerator(x):
        for i in range(3):
            for j in range(3):
                if i != j:
                    if len(pegs[i]) > 0:
                        if len(pegs[j]) == 0 or pegs[i][-1] < pegs[j][-1]:
                            pegs[j].append(pegs[i].pop())
                            if isValid(pegs):
                                validPegs.append(list(map(list, pegs)))
                                stateGenerator(x-1)  
                            pegs[i].append(pegs[j].pop())
              
stateGenerator(27)
for i in validPegs:
    print(i)
result = "The number of states generated: " + str(len(validPegs))
print(result)