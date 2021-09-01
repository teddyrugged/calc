#calculator converting currency

D = float(input("please enter amount in ngn:" ))
E = int(input("please enter 1 for usd, 2 for cad ,3 for gbp: " ))
F = 0
G = "currency"
if E == 1:
    F = (D/500)
    G = "USD"
elif E == 2:
    F = (D/350)
    G = "CAD"
elif E == 3:
    F = (D/700)
    G = "GBD"
else:
    F = ""
    G= "the number is not applicable"
    
print(G,F)


