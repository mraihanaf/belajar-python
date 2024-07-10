# https://www.w3schools.com/python/python_operators.asp

# Arithmetic Operators
print("==Arithmetic==")
print("2 + 2 =",2+2)
print("2 - 2 =",2-2)
print("2 / 2 =",2/2)
print("2 * 2 =",2*2)
print("2 % 2 =",2%2) # modulus
print("2 ** 2 =",2**2) # kuadrat
print("2 // 2 =",2//2) # floor division atau divisi lantai :
                       #  operasi dalam Python yang memungkinkan kita membagi 
                       #  dua angka dan membulatkan nilai yang dihasilkan ke 
                       #  bilangan bulat terdekat

# Bitwise Operators 
print("==Bitwise==")
print("1 AND 2",1&2)
print("1 OR 2",1|2)
print("1 XOR 2",1^2)
print("NOT 2",~2)
print("1 << 2",1<<2) # Zero fill shift
print("1 >> 2",1>>2) # Signed right shift

# Assignment Operators
print("==Asignment==")
x = 5
print("x = 5 -->",x)
x+=5
print("x += 5 -->",x)
x-=5
print("x -= 5 -->",x)
x*=2
print("x *= 2 -->",x)
x/=2
print("x /= 2 -->",x)
x**=2
print("x **= 2 -->",x)
x//=2
print("x //= 2 -->",x)
x%=4
print("x %= 4 -->",x)
x=int(x)
x&=1
print("x &= 1 -->",x) # Bitwise AND
x|=1
print("x |= 1 -->",x) # Bitwise OR
x^=1
print("x ^= 1 -->",x) # Bitwise XOR
x>>=1 # Bitwise
print("x >>= 1 -->",x)
x<<=1 # Bitwise
print("x <<= 1 -->",x)
print("x := 'rawr' --> x adalah",x := "rawr")
print(x)

# Comparison Operators
print("==Comparison==")
print("1 sama dengan 1",1==1)
print("1 tidak sama dengan 1",1!=1)
print("1 lebih besar dari 1",1>1)
print("1 lebih besar sama dengan 1",1>=1)
print("1 lebih kecil dari 1",1<1)
print("1 lebih kecil sama dengan 1",1<=1)

# Logical Operators
print("==Logical==")
print("True dan False -->",True and False)
print("True atau False -->",True or False)
print("Tidak True -->", not True)

# Memory Identity Operators
#   adalah operator yang digunakan untuk membandingkan objek, bukan jika mereka sama. tetapi membandingkan apakah
#   objek dan memori lokasi yang sama.
print("==Identity==")
print("x ->",x:=[1,2,3],"y ->",y:=[1,2,3],"z -> x(",z:=x,")") # z refrence x
print("x is y -->", x is y)
print("x is x -->",x is x)
print("x is z -->",x is z)
print("x is not y -->",x is not y)
print("x is not x -->",x is not x)
print("x is not z -->",x is not z)