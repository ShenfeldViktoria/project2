
def f(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def d_to_b(d_number):
    b_number= bin(d_number)
    return b_number

number = int(input("Vvedit cile chislo "))

f_res = f(number)
print(f"factorial {number} = {f_res}")

b_res = d_to_b(number)
print(f"chislo {number} v dviykoviy sisteme: {b_res}")