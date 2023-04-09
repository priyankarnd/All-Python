employees = ["John", "Frank", "Scott", "Mary", "Jim"]

print(employees[-2])

movies = ['Inception', 'Aladin', 'Avatar', 'Inception']

movies.sort()

movie_sort = []

for x in movies:
    y = x
    print(y)
    if y not in movie_sort:
        movie_sort.append(y)
    else:
        y = 'null'


print(movie_sort)




