person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

result = 'результат операции: 42'
result_from_text = result.split()
num = result_from_text[-1]
index_for_num = result_from_text.index(num)
print(int(result_from_text[index_for_num])+10)

result = 'результат операции: 514'
result_from_text = result.split()
num = result_from_text[-1]
index_for_num = result_from_text.index(num)
print(int(result_from_text[index_for_num])+10)

result = 'результат работы программы: 9'
result_from_text = result.split()
num = result_from_text[-1]
index_for_num = result_from_text.index(num)
print(int(result_from_text[index_for_num])+10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects)) 
