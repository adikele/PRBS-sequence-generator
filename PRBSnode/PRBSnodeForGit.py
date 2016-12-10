#pseudo random bit sequence  GENERATOR:

def prbsGetter(flagInt):
    global globalRegValues  #PLACE2
    if (flagInt == 0):
        globalRegValues = 0x000f  #seed

    output = globalRegValues & 0x0001
    globalRegValues = ((((( globalRegValues & 0x0002) >> 1) ^ (globalRegValues & 0x0001)) << 4) | (globalRegValues & 0x000f)) >> 1
    return output 
        
#global globalRegValues  PLACE1

for i in range (0,15):    
    print (prbsGetter(i))
    #print ("\n")
    


'''
NOTE;
If I have globalRegValues definition in PLACE1, instead of PLACE2, code doesn't work.
Error: UnboundLocalError: local variable 'globalRegValues' referenced before assignment

prints:
1
1
1
1
0
0
0
1
0
0
1
1
0
1
0

'''
