import random as r

# START

def findMax(array):
    print('Finding max value in given(random) array')
    val = 0
    idx = 0
    temp_index = 0              #for counting index
    for i in array:
        if i > val:             #keep only greater value 
            val = i
            idx = temp_index
        temp_index += 1
    print("Index : ", idx, " and Value : ", val)
    
#Generate random value      
def rd():
    return r.randrange(0,100,1)

#END

#Main loop
while(1):
    a = [r.randint(0, 100) for _ in range(rd())]    #Create random array

    print(a)
    findMax(a)
    input()