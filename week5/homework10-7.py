#Kaiden Zhou
#5.1
width=25
height=100
area=width*height

print("The width is " + str(width) + ", and the height is " + str(height) +".\n") 

perimeter=width*2+height*2
print("The area is " + str(area) + ", the perimeter is " + str(perimeter) + ".\n")
#5.2
programmingLanguage1stPlace,programmingLanguage2ndPlace= "C","Python"
message="The most popular programming language is C, and the second most popular programming language is Python.\n"
print(message)         

programmingLanguage1stPlace,programmingLanguage2ndPlace=programmingLanguage2ndPlace, programmingLanguage1stPlace

message2="After the exchange the most popular programming language is " + programmingLanguage1stPlace + " ,the second most popular programming language is " + programmingLanguage2ndPlace +"."
print(message2)
