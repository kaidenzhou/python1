para="In a galaxy far, far away, a young farm boy named Luke Skywalker discovers a message hidden within a droid, setting in motion a chain of events that will forever alter the course of his life. Guided by the wise and mysterious Obi-Wan Kenobi, Luke learns of his connection to the Force and the ancient battle between the Jedi and the Sith. As the dark shadow of the Galactic Empire looms large, a rebellion takes root, and unlikely heroes emerge, including the smuggler Han Solo and the fearless Princess Leia. Together, they embark on a daring quest to challenge the tyranny of Darth Vader and the Emperor, forging a saga of epic proportions filled with lightsabers, starships, and the eternal struggle between good and evil."
#10.1
print("Question 10.1")

char_count=0

for char in para:
    if char in{'.'}:
        break
    else:
        char_count+=1

print("The sentence length " + str(char_count) + " without the last period.")


#10.2
print("Question 10.2")

space_count=0
for char in para:
    if char in{' '}:
        space_count=space_count+1
print("The total occurence of ' ' is " + str(space_count) + ".")
    
#10.3
print("Question 10.3")

word_count=0
for char in para:
    if char in{' '}:
        word_count=word_count+1
#I added one more because it didn't count the last word        
word_count=word_count+1
print("The word count is " + str(word_count) + ".")

#10.4
print("Question 10.4")

e_count=0
o_count=0

for char in para:
    if char in{'e', 'E'}:
        e_count=e_count+1
    if char in{'o', 'O'}:
        o_count=o_count+1

if e_count > o_count:
    print("The character e occurs the most " + str(e_count))
elif e_count < o_count:
    print("The character o occurs the most with " +str(o_count))
elif e_count == o_count:
    print("The character e and o have the same occurence " + str(e_count) +" " + str(o_count))
else:
    print("Error happened")

#10.5
print("Question 10.5")

char_count=0
o_found=False
for char in para:
    char_count=char_count+1
    if char in{'O'}:
          o_found=True
          break
          print("The first appreance of letter O is at index " + str(char_count))
          
if o_found:
    print("O is found")
else:
    print("There is no O")
