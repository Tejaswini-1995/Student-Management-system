SELECT s1.First_Name, s1.Last_Name, s1.Mobile_Number, s1.Aadhar_Card_Number,s1.Subject, s1.StudentAdmissionDate,
s1.Fees_Paid, concat(s2.Total_Fees-s2.Fees_Paid) AS Remaining_Fees FROM student_Details AS s1 , student_Details AS s2
Where s1.Aadhar_Card_Number = s2.Aadhar_Card_Number;