'''## Working on list and tuples
movie=['Banana','Mango','Apple']
print(f"Movie Names are {movie}")
print (f"Last Movie name is {movie[2]}")
movie.append('Orrange')
print(f"Movie names after adding new fruit are {movie}")
movie.remove('Banana')
print(f"Movie names after removing Banana are {movie}")
## Finding min, max, ave age in the family

#Create a list with ages in the family
age=[37,35,10,2,60]
print(f" List of the ages in the family is {age}")
print(f"Maximum age in the family is {max(age)}")
print(f"Manimum age in the family is {min(age)}")
print(f"Average age in the family is {sum(age)/len(age):.2f}")

##Tuple practicing
colors=('Blue','White','Gray')
print(f"Printing colors {colors}")
print()
print(f"Printing first color {colors[0]}")
print(f"Printing last color {colors[2]}")
print()
colors.append('Red')
def get_arrays():
    subjects=("Math", "Science", "English")
    math_scores = [89, 78, 77]
    science_scores = [80, 70, 70]
    english_scores = [70, 80, 80]
    telugu_scores = [70, 50, 90]
    subjects_list=list(subjects)
    subjects_list.append('Telugu')
    subjects=tuple(subjects_list)
    for i in subjects:
        if i =='Math':
            print(f"Printing {i} marks {math_scores} , Average marks of {i} is {sum(math_scores)/len(math_scores):.2f}")
        if i =='Science':
            print(f"Printing {i} marks {science_scores} , Average marks of {i} is {sum(science_scores)/len(science_scores):.2f}")
        if i =='English':
            print(f"Printing {i} marks {english_scores} , Average marks of {i} is {sum(english_scores)/len(english_scores):.2f}")
        if i =='Telugu':
            print(f"Printing {i} marks {telugu_scores} , Average marks of {i} is {sum(telugu_scores)/len(telugu_scores):.2f}")
get_arrays()'''
def get_lists():
    while True:
        s_names=['Mohan','Raju','Bhupal','Krish','Cherri']
        s_marks=[89,95,78,99,85]
        avg_marks=sum(s_marks)/len(s_marks)
        name=input("Enter the name to search the student or exit to exit from program.   ").strip().title()
        if name=='exit':
            print(f"Exiting from program...")
            break
        if name in s_names:
            i=s_names.index(name)
            sorted_marks = sorted(s_marks, reverse=True)
            rank = sorted_marks.index(s_marks[i]) + 1
            print(f"{name}'s marks: {s_marks[i]}")
            print(f"{name}'s rank: {rank}")
            print(f"Class average: {avg_marks:.2f}")

        else:
            print(f"{name} not found in the class.")
get_lists()