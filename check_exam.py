def check_exam(arr1,arr2):
# оценка 
    mark = 0

# повторяение всех индексов от 0 до последней позиции наименьшего списка 
    for i in range(min(len(arr1), len(arr2))):

# проверка елементов по индексу             
            if arr1[i] == arr2[i]:
                mark += 4
            elif arr2[i] == '':
                mark += 0
            else:
                mark += -1

# если оценка меньше 0, то mark равен 0        
    if mark < 0:
            mark = 0
    
    return mark    

