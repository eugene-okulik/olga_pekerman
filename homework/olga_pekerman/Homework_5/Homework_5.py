person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

result = 'результат операции: 42'
index_for_colon = result.index(':')
index_for_num = int(index_for_colon) + 2
num = result[index_for_num:]
print(int(num) + 10)

result = 'результат операции: 514'
index_for_colon = result.index(':')
index_for_num = int(index_for_colon) + 2
num = result[index_for_num:]
print(int(num) + 10)

result = 'результат работы программы: 9'
index_for_colon = result.index(':')
index_for_num = int(index_for_colon) + 2
num = result[index_for_num:]
print(int(num) + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
