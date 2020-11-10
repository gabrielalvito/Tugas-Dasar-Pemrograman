#MEDIA PEMBELAJARAN MATEMATIKA
def luasbujursangkar(s):
    luas= s*s
    return luas
def kelilingbujursangkar(s):
    keliling= 4*s
    return keliling
def luaspersegipanjang(p,l):
    luas= p*l
    return luas
def kelilingpersegipanjang(p,l):
    keliling= 2*(p+l)
    return keliling
def luassegitiga(a,t):
    luas= (a*t)/2
    return luas
def kelilingsegitiga(a,b,c):
    keliling= a+b+c
    return keliling
def luaslingkaran(r):
    luas= 3.14*r*r
    return luas
def kelilinglingkaran(r):
    keliling= 2*3.14*r
    return keliling
def luasjajargenjang(a,t):
    luas= a*t
    return luas
def kelilingjajargenjang(a,b):
    keliling= 2*(a+b)
    return keliling
    
#INPUT
pilihan =1
while pilihan !=0:
    print("Program Media Pembelajaran Matematika")
    print('')
    print("1. Menghitung luas bujur sangkar")
    print("2. Menghitung keliling bujur sangkar")
    print("3. Menghitung luas persegi panjang")
    print("4. Menghitung keliling persegi panjang")
    print("5. Menghitung luas segitiga")
    print("6. Menghitung keliling segitiga")
    print("7. Menghitung luas lingkaran")
    print("8. Menghitung keliling lingkaran")
    print("9. Menghitung luas jajar genjang")
    print("10.Menghitung keliling jajar genjang")
    print("11.Exit Program")
    print('')
    
    pilihan=int(input("Masukkan pilihan anda: "))
    print('')
    print('')

    if pilihan ==1:
        s=float(input("Masukkan panjang sisi: "))
        print("Luas bujur sangkar adalah: ",luasbujursangkar(s))
        print('')
    
    elif pilihan ==2:
        s=float(input("Masukkan panjang sisi: "))
        print("Keliling bujur sangkar adalah: ",kelilingbujursangkar(s))
        print('')    
    elif pilihan ==3:
        p=float(input("Masukkan panjang: "))
        l=float(input("Masukkan lebar: "))
        print("Luas persegi panjang adalah: ",luaspersegipanjang(p,l))
        print('')
    elif pilihan ==4:
        p=float(input("Masukkan panjang: "))
        l=float(input("Masukkan lebar: "))
        print("Keliling persegi panjang adalah: ",kelilingpersegipanjang(p,l))
        print('')
    elif pilihan ==5:
        a=float(input("Masukkan alas: "))
        t=float(input("Masukkan tinggi: "))
        print("Luas segitiga adalah: ",luassegitiga(a,t))
        print('')
    elif pilihan ==6:
        a=float(input("Masukkan panjang sisi a: "))
        b=float(input("Masukkan panjang sisi b: "))
        c=float(input("Masukkan panjang sisi c: "))
        print("Keliling segitiga adalah: ",kelilingsegitiga(a,b,c))
        print('')
    elif pilihan ==7:
        r=float(input("Masukkan panjang jari-jari: "))
        print("Luas lingkaran adalah: ",luaslingkaran(r))
        print('')
    elif pilihan ==8:
        r=float(input("Masukkan panjang jari-jari: "))
        print("Keliling lingkaran adalah: ",kelilinglingkaran(r))
        print('')
    elif pilihan ==9:
        a=float(input("Masukkan panjang alas: "))
        t=float(input("Masukkan panjang tinggi: "))
        print("Luas jajar genjang adalah: ",luasjajargenjang(a,t))
        print('')
    elif pilihan ==10:
        a=float(input("Masukkan panjang a: "))
        b=float(input("Masukkan panjang b: "))
        print("Keliling jajar genjang adalah: ",kelilingjajargenjang(a,b))
        print('')
    elif pilihan ==11:
        break
    else:   
        print("Masukkan salah")
    
print("Program Selesai")
  