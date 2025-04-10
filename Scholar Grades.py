def scholarGrades(fname, fields):
    grades = []; data = ''
    item = 'name'; m = ''
    
    for x in range(len(fields) + 1):
        stdata = input(f'What is your {item}: ')
        grades.append(stdata)
        
        if x >= 1: data += f'{item} mark is ---- {stdata}\n'
        item = fields[-(len(fields)-x)]; m = 'mark'
        
    avg = sum([int(n) for n in grades[1:]]) / len(fields)
    
    with open(f'{fname}.txt', 'w') as file:
         file.write(f'''Hello {grades[0]}\n{data}\n Your average grade is : {avg}''')
    
    print(f'Your average grade is : {avg}')
    
    
filename = input("What is your file name: ")
courses = ['CS', 'Algorithms', 'Analysis', 'Logic']
scholarGrades(filename, courses) 
                    
         
    