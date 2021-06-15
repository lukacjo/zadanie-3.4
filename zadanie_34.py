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