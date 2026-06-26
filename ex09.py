def primo(n):
    if n <= 1:
        return False
    else:
        divisores = 0
        for i in range(1,n+1):
            if n % i == 0:
                divisores += 1
        return divisores == 2
def primos_ate_n(numero):
    return [n for n in range(numero + 1) if primo(n)]
print(primos_ate_n(30))