#all the possible base conversions to base
values = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#converts a decimal number to  whatever  base is passed in
def encode(dec, base):
    baseVer = ""    #empty string to hold converted number
    #divide the number by the base number until its 0
    while dec!=0:
        #the remainder of each division becomes part of the converted number
        temp = dec%base
        #finds the corresponding base number for the remainder
        for a in range(36):
            if temp == a:
                baseVer+=values[a]
                break
        dec = int(dec/base) 
    return baseVer

#converts a number from a base to decimal
def decode(baseNum, base):
    #gets the length of conversion string and the length of the number to decode
    valueLen = len(values)
    baseLen = len(baseNum)
    #reverses the number to decode
    temp = baseNum[::-1]
    #our decoded number
    dec = 0
    #loop through out all the numbers in the number to decode
    for num in range(baseLen):
        temp = base**num
        #loop through  the conversion string
        for item in range(valueLen):
            #check if the base number matches the conversion number
            if temp[num] == values[item]:
                dec+= item*temp
    return dec

def baseChange(baseNum, firstBase, secondBase):
    dec = decode(baseNum, firstBase)
    return encode(dec, secondBase)