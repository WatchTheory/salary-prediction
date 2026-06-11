
/*Cleaning all special character from "Data Analyst!!!" title */

-- First, filiter all the records that have incorrect job title "Data Analyst!!!"
Select * From resume where job_title = "Data Analyst!!!";

/*Changes 'Data Analyst!!!' to 'Data Analyst' */
Update resume
Set job_title = Replace(job_title,'!!!', '') 
where job_title = 'Data Analyst!!!';

/*Check update rows*/
Select * From resume 

/*Checks before changing 'Data Analyst!!!' to 'Data Analyst*/
-- Select 
--    job_title,
--    Replace(job_title,'!!!', '') 
-- From resume
-- where job_title = 'Data Analyst!!!';