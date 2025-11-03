
def is_valid_ipv4(ipv4):
    l_ipv4 = ipv4.split(".")
    if len(l_ipv4) != 4:
        return False
    
    for i in l_ipv4:
        if not i.isdigit():
            return False
        if int(i)  < 0 or int(i) > 255:
            return False
        if leading_zeros(i) == True:
            return False
    
    return True
    



def leading_zeros(n):
    if len(n) > len(str(int(n))):
        return True
    return False


print(is_valid_ipv4("255.01.50.111"))
print(is_valid_ipv4("192168145213"))
print(is_valid_ipv4("192.168.1.1"))
print(is_valid_ipv4("256.101.50.115"))


