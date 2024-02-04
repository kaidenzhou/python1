#Q7.1
dimensions=(4,5,6)
volume = dimensions[0] * dimensions[1] * dimensions[2]
print(volume)
#Q7.2
movie_ratings={"super mario bros movie":5, "detective pikachu":5, "rise of skywalker":4, "fnaf":5}
print(movie_ratings)
movie_ratings["cars 3"]=5
print(movie_ratings)
#7.3
my_colors={"blue","gold","green","red","silver"}
              
wills_colors={"blue","red","purple"}
common_colors=my_colors.intersection(wills_colors)
print(common_colors)