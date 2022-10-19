i=0
soma=0
con=0
qtd=0
for i in range(10):
    n=int(input("Digite o numero"))
    if n%2==0:
        par=n
        soma=soma+par
    if n<10:
        qtd+=1
print("A soma dos numeros pares é de:",soma)
print("A quantidade de numeros menores que 10 é de:",qtd)