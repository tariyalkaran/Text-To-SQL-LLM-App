import sqlite3

## Connect to sqlite
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record,create table,retrieve
cursor=connection.cursor()

## Create the table
table_info="""
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT,
    Date_of_Admission DATE,
    Gender VARCHAR(25)
);


"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''INSERT INTO STUDENT VALUES
('Rohit', 'DevOps', 'B', 72, '2022-01-10', 'M'),
('Priya', 'AI ML', 'A', 90, '2022-01-11', 'F'),
('Arjun', 'Data Science', 'B', 75, '2022-01-12', 'M'),
('Anjali', 'AI ML', 'C', 68, '2022-01-13', 'F'),
('Kavita', 'Data Science', 'B', 82, '2022-01-14', 'F'),
('Ravi', 'DevOps', 'A', 88, '2022-01-15', 'M'),
('Meena', 'AI ML', 'B', 80, '2022-01-16', 'F'),
('Raj', 'Data Science', 'A', 92, '2022-01-17', 'M'),
('Sneha', 'DevOps', 'C', 65, '2022-01-18', 'F'),
('Vikram', 'Data Science', 'B', 77, '2022-01-19', 'M'),
('Neha', 'AI ML', 'A', 95, '2022-01-20', 'F'),
('Amit', 'Data Science', 'B', 78, '2022-01-21', 'M'),
('Jyoti', 'DevOps', 'C', 70, '2022-01-22', 'F'),
('Sumit', 'AI ML', 'B', 83, '2022-01-23', 'M'),
('Manoj', 'Data Science', 'C', 67, '2022-01-24', 'M'),
('Suman', 'DevOps', 'A', 89, '2022-01-25', 'F'),
('Pooja', 'AI ML', 'B', 81, '2022-01-26', 'F'),
('Nikhil', 'Data Science', 'A', 91, '2022-01-27', 'M'),
('Swati', 'DevOps', 'C', 63, '2022-01-28', 'F'),
('Akash', 'Data Science', 'B', 79, '2022-01-29', 'M'),
('Ishita', 'AI ML', 'A', 96, '2022-01-30', 'F'),
('Tarun', 'DevOps', 'C', 64, '2022-01-31', 'M'),
('Deepa', 'Data Science', 'B', 85, '2022-02-01', 'F'),
('Rahul', 'AI ML', 'B', 84, '2022-02-02', 'M'),
('Ankita', 'DevOps', 'C', 66, '2022-02-03', 'F'),
('Nitin', 'Data Science', 'A', 93, '2022-02-04', 'M'),
('Pankaj', 'AI ML', 'B', 82, '2022-02-05', 'M'),
('Mona', 'Data Science', 'B', 76, '2022-02-06', 'F'),
('Kapil', 'DevOps', 'A', 87, '2022-02-07', 'M'),
('Gaurav', 'AI ML', 'B', 79, '2022-02-08', 'M'),
('Disha', 'Data Science', 'C', 69, '2022-02-09', 'F'),
('Vinay', 'DevOps', 'B', 74, '2022-02-10', 'M'),
('Komal', 'AI ML', 'A', 92, '2022-02-11', 'F'),
('Aditya', 'Data Science', 'C', 66, '2022-02-12', 'M'),
('Rachna', 'DevOps', 'A', 85, '2022-02-13', 'F'),
('Shivani', 'AI ML', 'B', 84, '2022-02-14', 'F'),
('Rajesh', 'Data Science', 'A', 90, '2022-02-15', 'M'),
('Rakesh', 'DevOps', 'C', 62, '2022-02-16', 'M'),
('Sunita', 'AI ML', 'B', 81, '2022-02-17', 'F'),
('Arvind', 'Data Science', 'A', 94, '2022-02-18', 'M'),
('Kiran', 'DevOps', 'C', 71, '2022-02-19', 'F'),
('Asha', 'AI ML', 'A', 88, '2022-02-20', 'F'),
('Mohit', 'Data Science', 'B', 77, '2022-02-21', 'M'),
('Yash', 'DevOps', 'C', 63, '2022-02-22', 'M'),
('Sonal', 'AI ML', 'B', 82, '2022-02-23', 'F'),
('Tanvi', 'Data Science', 'A', 89, '2022-02-24', 'F'),
('Harsh', 'DevOps', 'C', 70, '2022-02-25', 'M'),
('Bhavna', 'AI ML', 'A', 96, '2022-02-26', 'F'),
('Chirag', 'Data Science', 'B', 76, '2022-02-27', 'M'),
('Ritu', 'DevOps', 'B', 73, '2022-02-28', 'F'),
('Alok', 'AI ML', 'C', 65, '2022-03-01', 'M'),
('Farhan', 'Data Science', 'A', 91, '2022-03-02', 'M'),
('Rina', 'DevOps', 'B', 80, '2022-03-03', 'F'),
('Keshav', 'AI ML', 'C', 67, '2022-03-04', 'M'),
('Saloni', 'Data Science', 'A', 93, '2022-03-05', 'F'),
('Anand', 'DevOps', 'C', 64, '2022-03-06', 'M'),
('Vimal', 'AI ML', 'B', 84, '2022-03-07', 'M'),
('Namrata', 'Data Science', 'B', 78, '2022-03-08', 'F'),
('Rajiv', 'DevOps', 'C', 66, '2022-03-09', 'M'),
('Kanika', 'AI ML', 'A', 87, '2022-03-10', 'F'),
('Kartik', 'Data Science', 'B', 79, '2022-03-11', 'M'),
('Nidhi', 'DevOps', 'C', 62, '2022-03-12', 'F'),
('Tanya', 'AI ML', 'A', 89, '2022-03-13', 'F'),
('Prateek', 'Data Science', 'C', 71, '2022-03-14', 'M'),
('Ashwin', 'DevOps', 'B', 74, '2022-03-15', 'M'),
('Kajal', 'AI ML', 'C', 65, '2022-03-16', 'F'),
('Sahil', 'Data Science', 'A', 94, '2022-03-17', 'M'),
('Kunal', 'DevOps', 'B', 83, '2022-03-18', 'M'),
('Divya', 'AI ML', 'A', 95, '2022-03-19', 'F'),
('Sandeep', 'Data Science', 'C', 68, '2022-03-20', 'M'),
('Ankur', 'DevOps', 'A', 90, '2022-03-21', 'M'),
('Harpreet', 'AI ML', 'B', 85, '2022-03-22', 'F'),
('Anushka', 'Data Science', 'B', 78, '2022-03-23', 'F'),
('Deepak', 'DevOps', 'C', 69, '2022-03-24', 'M'),
('Nilesh', 'AI ML', 'A', 92, '2022-03-25', 'M'),
('Kirti', 'Data Science', 'B', 77, '2022-03-26', 'F'),
('Yuvraj', 'DevOps', 'C', 63, '2022-03-27', 'M'),
('Tina', 'AI ML', 'B', 82, '2022-03-28', 'F'),
('Mukesh', 'Data Science', 'A', 93, '2022-03-29', 'M'),
('Niharika', 'DevOps', 'C', 71, '2022-03-30', 'F'),
('Rachit', 'Data Science', 'A', 93, '2024-08-17', 'M'),
-- Additional records to make 200 entries
('Zoya', 'AI ML', 'A', 96, '2022-03-31', 'F'),
('Kabir', 'Data Science', 'B', 85, '2022-04-01', 'M'),
('Ayesha', 'DevOps', 'B', 81, '2022-04-02', 'F'),
('Rohan', 'AI ML', 'A', 92, '2022-04-03', 'M'),
('Preeti', 'Data Science', 'C', 67, '2022-04-04', 'F'),
('Vivek', 'DevOps', 'A', 89, '2022-04-05', 'M'),
('Surbhi', 'AI ML', 'B', 84, '2022-04-06', 'F'),
('Vikrant', 'Data Science', 'B', 80, '2022-04-07', 'M'),
('Nina', 'DevOps', 'C', 64, '2022-04-08', 'F'),
('Harshit', 'AI ML', 'A', 95, '2022-04-09', 'M'),
('Kriti', 'Data Science', 'B', 82, '2022-04-10', 'F'),
('Shyam', 'DevOps', 'C', 70, '2022-04-11', 'M'),
('Pallavi', 'AI ML', 'B', 83, '2022-04-12', 'F'),
('Gagan', 'Data Science', 'A', 90, '2022-04-13', 'M'),
('Neeraj', 'DevOps', 'B', 79, '2022-04-14', 'M'),
('Mahi', 'AI ML', 'C', 68, '2022-04-15', 'F'),
('Aarav', 'Data Science', 'A', 92, '2022-04-16', 'M'),
('Shruti', 'DevOps', 'A', 88, '2022-04-17', 'F'),
('Rehan', 'AI ML', 'B', 84, '2022-04-18', 'M'),
('Tanisha', 'Data Science', 'B', 77, '2022-04-19', 'F'),
('Naveen', 'DevOps', 'C', 66, '2022-04-20', 'M'),
('Simran', 'AI ML', 'A', 96, '2022-04-21', 'F'),
('Abhishek', 'Data Science', 'B', 81, '2022-04-22', 'M'),
('Esha', 'DevOps', 'C', 65, '2022-04-23', 'F'),
('Adarsh', 'AI ML', 'A', 94, '2022-04-24', 'M'),
('Lakshmi', 'Data Science', 'B', 78, '2022-04-25', 'F'),
('Raghav', 'DevOps', 'B', 80, '2022-04-26', 'M'),
('Sia', 'AI ML', 'C', 67, '2022-04-27', 'F'),
('Arnav', 'Data Science', 'A', 89, '2022-04-28', 'M'),
('Megha', 'DevOps', 'A', 85, '2022-04-29', 'F'),
('Yashika', 'AI ML', 'B', 82, '2022-04-30', 'F'),
('Tejas', 'Data Science', 'C', 71, '2022-05-01', 'M'),
('Riddhi', 'DevOps', 'B', 79, '2022-05-02', 'F'),
('Veer', 'AI ML', 'A', 92, '2022-05-03', 'M'),
('Mahima', 'Data Science', 'C', 68, '2022-05-04', 'F'),
('Jay', 'DevOps', 'B', 74, '2022-05-05', 'M'),
('Isha', 'AI ML', 'A', 95, '2022-05-06', 'F'),
('Aman', 'Data Science', 'B', 82, '2022-05-07', 'M'),
('Sakshi', 'DevOps', 'C', 66, '2022-05-08', 'F')
''')






## Display all the records
print("The inserted records are")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## Close the connetion

connection.commit()
connection.close()