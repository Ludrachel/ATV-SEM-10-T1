cont_par = 0
cont_impar = 0
for n in range(1, 101):
    num = int(input())
    if num % 2 == 0:
       cont_par += 1
    else:
       cont_impar += 1
print(cont_par)
print(cont_impar)
