print ("soal:", "\n")
print ("Misalkan N(t) adalah variable acak poissison dengan parameter lambda_t>0")
print ("             P(N(t) = n) e**(-lambda_t)*(lambda_t)**N/(n!)              ")
print ("Buatlah suatu program untuk menghitung P(N(t) = n), inputkan nilai terlebih dahulu.            ","\n")
lambda_t = int (input("masukkan nilai lambda t         : "))
m        = int (input("input nilai m                   : "))
e = 2.71828
faktorial_b = 1
print ("\n")
for b in range (0,m+1):
    faktorial_b *= (b+1)
    n=(e**(-lambda_t)) * ((lambda_t)**b)/faktorial_b 
    print(f"maka nilai P(N(t) ke -{b} adalah :{n} {m} faktiorial adalah:{faktorial_b}")











    

