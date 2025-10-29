U = float(input("Enter initial velocity : "))
A = float(input("Enter acceleration : "))
S = float(input("Enter distance : "))

V2 = U**2 + 2*A*S
V = V2**0.5  

print("Final velocity squared =", V2)
print("Final velocity =", V)