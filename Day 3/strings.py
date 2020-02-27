sentence = "I love this UBS Python Class!"

#sentence2 = sentence.replace(" ", "_")
#print (sentence2)
print (sentence.replace(" ", "_"))

splitSentence = sentence.split()
print (splitSentence[1:])

firstSpace = sentence.find(" ")
print(sentence[firstSpace:])


print (sentence.find("U"))
