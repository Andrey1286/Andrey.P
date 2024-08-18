def get_matrix(n, m, value): # n -строки, m - столбцы, value - значения
    matrix = []
    for i in range(n):
        string = []
        for j in range(m):
            string.append(value)
        matrix.append(string)
    return(matrix)

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)