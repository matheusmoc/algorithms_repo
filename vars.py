var1 = 12
var2 = 30
var3 = var1 * var2
print(var3)

var3 = var3 / 2
print(var3)

var3 = var3 // 2
print(var3)


num1 = str(input("Digite um número a seguir: "))
dobro = 2*num1
print("O dobro do número digitado é:", dobro)



x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))
print(num > x*y, num <= x + y, num*y != x*y)
print(num == x, num == y, num == x + y)
print(2 == "2", False, 2.0 == 2)
print(True, False, False)
print(num == x*y, num*y == x*y, y > x + num)
print(False, True, True)



x = 10
y = 4.2
z = "42"

print(not (((x * y == z) and not (x < y)) or y % 2 == 0))

print(not (not (x < y and x * y == z)) or (x >= y or y % 2 == 0))
print(not False)
print(not ((x == y or True) and ((int(z) < x*y) and (type(y) == type(int(z))))))
print(not (((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) != type(z)))))
print((True and True) or not True)



a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a > b and a > c:
  resposta = a % 2 == 0
elif b > a and b > c:
  resposta = b % 2 == 0
else:
  resposta = c % 2 == 0

  
print(f"O maior número entre os três números informados é par?{resposta}")