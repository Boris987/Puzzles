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
    