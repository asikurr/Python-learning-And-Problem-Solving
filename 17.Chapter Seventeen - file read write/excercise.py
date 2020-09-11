# read other file coma separed value

with open('file1.txt','r') as rf: 
    with open('Salary_output.txt','a') as wf:
        for li in rf.readlines():
            name,salary = li.split(',')
            wf.write(f'hi {name}\'s your salary is {salary}')