def menu():
    print("dungiin burtgeliin programm")
    print("-"*30)
    print(" 1. Dungiin medeelel harah")
    print(" 2. Dungiin medeelel burtgeh")
    print(" 3. Dungiin medeelel ustgah")
    print(" 4. Dungiin medeelel zasah")
    print(" 5. Programmaas garah")
    print("-"*30)
def create():
   owog,ner,dun = input("Owog, ner, dun: ").split()
   f = open("dun.txt", "a")
   f.write("\n"+ owog + " " + ner + " " + dun)
   f.close()
def remove():
    owog,ner = input("owog ner: ").split()
    f = open("dun.txt","r")
    data = f.readlines()
    f.close
    for item in data:
        line = item.split()
        if line[0] == owog and line[1] == ner:
            data.remove(item)
    txt = "".join(data)
    f = open("dun.txt","w")
    f.write(txt)
    f.close()
def show():
    f = open("dun.txt","r")
    txt = f.readlines()
    f.close()
    for item in txt:
        line = item.split()
    txt = "".join(txt)
    print("\n")
    print(txt)
def update():
    f = open("dun.txt","r")
    txt=f.read()
    f.close()
    data = txt.split("\n")
    owog, ner = input("Owog, ner: ").split()
    for item in data:
        row = item.split()
        if row[0] == owog and row[1] ==ner:
            f1 = open("dun.txt","r+")
            dun = input("Zasah dungee bichne uu: ")
            index = data.index(item)
            f1.write(item.replace(row[2], dun))
    f1.close()
def update1():
    f = open("dun.txt","r")
    txt=f.read()
    f.close()
    data = txt.split("\n")
    owog, ner = input("Owog, ner: ").split()
    for item in data:
        row = item.split()
        if row[0] == owog and row[1] ==ner:
            dun = input("Dun: ")
            row[2]=dun
            index = data.index(item)
            data[index] = " ".join(row)
    f = open("dun.txt","w")
    f.write("\n".join(data))
    f.close