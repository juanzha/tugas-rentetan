#create a function
def my_function():
    print("ngopi yukk")

nama = " juanzha nanda pratama "
umur = 18
tinggi = 17,5

#call function
my_function()
print(type(nama),"/n")
print(type(umur),"/n")
print(type(tinggi),"/n",tinggi)

#list
print(10*"=")
hewan = ["kucing","ayam","kelinci"]
print(hewan[2])
print(10*"=")

if 2 > 1:
    print("benar")
else:
    print("salah")

a = 1
b = 2
c = a + b
print(a , "+" , b,"=",c)

#tuple
makanan = ("sate","tahu tek")
print(makanan)
#set
minuman = ("air mineral","kopi")

a = 20
b = 7
print("penjumlahan : " + str(a + b))


#arkitmatika
print(a, "+", b , "=", c)
print(a, "-", b , "=", a - b)
print(a, "/", b , "=", a / b)
print(a, "%", b , "=", a % b)

nama = input("Masukan nama anda : ")
print("ternyata nama anda adalah" + nama)



print("\nPROGRAM KONVERSI TEMPERATUR\n")

#CELCIUS
celcius = float(input("Masukan suhu dalam celcius = "))
print("suhunya adalah = ",celcius,"Celcius")

reamur = (4/5) * celcius
print("suhunya adalah = ",reamur,"Reamur")

fahrenheit = ((9/5) * celcius) + 32
print("suhunya adalah = ",fahrenheit,"Fahrenheit")

kelvin = celcius + 273
print("suhunya adalah = ",kelvin,"Kelvin")

#FAHRENHEIT
print("\n")
fahrenheit = float(input("Masukan suhu dalam fahrenheit = "))
print("suhunya adalah = ",fahrenheit,"Fahrenheit")

celcius = ((5/9) * (fahrenheit -32 ))
print("suhunya adalah = ",celcius,"Celcius")

reamur = ((4/9) * (fahrenheit - 32))
print("suhunya adalah = ",reamur,"Reamur")

kelvin = ((5 / 9) * (fahrenheit - 32) + 273)
print("suhunya adalah = ",kelvin,"Kelvin")

#KELVIN
print("\n")
kelvin = float(input("Masukan suhu dalam kelvin = "))
print("suhunya adalah = ",kelvin,"Kelvin")

celcius = kelvin - 273
print("suhunya adalah = ",celcius,"Celcius")

reamur = (4/5) * (kelvin - 273)
print("suhunya adalah = ",reamur,"Reamur")

fahrenheit = 1.8 * (kelvin - 273) + 32
print("suhunya adalah = ",fahrenheit,"Fahrenheit")


#V = 1/3 x π x r^2 x t


r = int(input("masukan jari jari : "))
t = int(input("masukan tinggi : "))
v = (r*t*1/3*22/7)
print("volume adalah : ", v )
