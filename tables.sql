CREATE TABLE CustomerInformation (
    CustomerID INT PRIMARY KEY NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL
);


select * from CustomerInformation;


create table  students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    roll_no VARCHAR(20) UNIQUE NOT NULL,
    course VARCHAR(50) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    attendance ENUM('absent', 'present') NOT NULL
);

select * from students;

	-- SQL VIEW OF STUDENT TABLE -- 
CREATE VIEW student_attendance_view AS
SELECT name, rollno, attendance
FROM students;

SELECT * FROM student_attendance_view;

-- Trigger-- 

-- CREATE TRIGGER student_insert_trigger
-- AFTER INSERT ON students
-- FOR EACH ROW
--     UPDATE students SET attendance = 'present' WHERE id = NEW.id;
--  
--  
 -- Stored Procedure
 
DELIMITER //
DROP Trigger student_insert_trigger;
CREATE PROCEDURE get_all_students()
BEGIN
    SELECT * FROM students;
END;
//

DELIMITER ;
CALL get_all_students();
