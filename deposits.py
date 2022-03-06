def bank(a,years):
    # часть от суммы 
    quart = (a * 10)/ 100
    # проценты за каждый год  
    percents = years * quart
    sum = a + percents
    return sum
print(bank(5000,1))        
