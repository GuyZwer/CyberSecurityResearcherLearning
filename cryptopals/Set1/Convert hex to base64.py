##convert hex to binary
hex1 = str(raw_input("Please enter only HEX number: "))
binary = bin(int(hex1, 16))[2:]
print binary
##Binary to Base64
bin1 = str(binary)
list1 = []
def check_bin(bin1):
    bin1 = list(bin1)
    bin2=bin
    for lop in range(len(bin2)):
        if bin1[lop] == '1':
            break
        elif bin1[lop] == '0':
            bin = bin1[lop+1:len(bin2)]
    return ''.join(bin1)

for lop in range(len(bin1)):
    list1.append(int(bin1[lop])*(64**((len(bin1)-1)-lop)))
print sum(list1)
