
n = int(input("Vvedit cile chislo "))
summa = 0
print("Chisla vid  1 do", n,)
for i in range(1, n + 1):
    print(i, end=' ') 
    summa += i
print("Summa chisel vid 1 do ", n, "=", summa)