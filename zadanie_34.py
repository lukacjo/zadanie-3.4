#zadanie 1
slownik={
    "piekarnia": ["chleb","paczek","bulki"],
    "warzywniak": ["marchew", "seler","rukola"]
}

itemy=slownik.items()

print("Lista zakupów")

count=0

for key, value in itemy:
    print("Ide do", key.capitalize(),"kupuje tu następujące rzeczy:",value )
    count += len(value)
print("W sumie kupuję",count,"produktów.")

#zadanie 2
licz=[]
poteg=[]
i=0

while True:
    m=i*5
    licz.append(m)
    i=i+1
    j=m**3
    poteg.append(j)
    if m >=100:
        break
print("liczby podzielne przez 5:",licz)
print("potęgi ^3 liczb podzielnych przez 5:",poteg)
print("sprawdzam git push")