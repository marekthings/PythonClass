books = int(input("Books "))
doc = int(input("Documentaries "))

booksList = ["Novice", "Avid Reader", "Literary", "Bibliophile"]
docList = ["Novice", "Avid Watcher", "Connoisseur", "Docuphile"]

timespent = (books*9)+(doc*2)

print ("Time spent learning:", timespent, "Hours")

if books < 5:
    bValue = 0
elif books <10:
    bValue = 1
elif books <15:
    bValue = 2
else:
    bValue = 3

if doc < 5:
    dValue = 0
elif doc <10:
    dValue = 1
elif doc <15:
    dValue = 2
else:
    dValue = 3

print (booksList[bValue], docList[dValue])
