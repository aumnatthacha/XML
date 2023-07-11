import xml.etree.ElementTree as ET


tree = ET.parse('studentse.xml')
root = tree.getroot()


students = []

for student in root.findall('student'):
   
    id = student.find('id').text
    name = student.find('name').text
    lastname = student.find('lastname').text
    
    
    student_data = {
        'id': id,
        'name': name,
        'lastname': lastname
    }
    students.append(student_data)


for student in students:
    print('Id:', student['id'])
    print('Name:', student['name'])
    print('Lastname:', student['lastname'])
    print('---')