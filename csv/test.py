import csv
def read():
    with open('employee_birthday.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
def write():
    import csv
    # ส่วนการเปิดไฟล์ CSV ที่ชื่อ employee_file.txt
    with open('employee_file.csv', mode='w') as employee_file:
        # ส่วนการกำหนดการเขียนไฟล์
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # ส่วนการเพิ่มข้อมูล
        employee_writer.writerow(['John Smith', 'Accounting', 'November','woww','riku'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
write()