def voltear_numero(reverso_n):
    n = reverso_n
    r = 0
    while(n > 0):
        a = n % 10 
        r = r * 10 + a
        n = n // 10
    return(r)

numero = int(input("Digite un número por favor :) : "))

if numero % 10 == 0: 
    numero = numero // 10

if numero == voltear_numero(numero) :
    print(numero,"El numero ingresado es un número palindrome")

else :
    print(numero,"EL numero ingresado no es un número palindrome")