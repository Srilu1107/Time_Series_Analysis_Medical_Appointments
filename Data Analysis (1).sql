
# Task 1: How many values are there in the given dataset
select count(*)
from patients

# Task 2: Count the number of appointments for each day in the given dataset
select AppointmentDay, count(*) as total_number_of_appointments
from patients
group by AppointmentDay

# Task 3: Calculate the average number of appointments(Set to nearest whole number) per day in the given dataset
with cte as(select appointmentDay, count(*) as c
from patients
group by AppointmentDay)

select round(avg(c), 0)
from cte

# Task 4: Find the day with the highest number of appointments in the given dataset
select AppointmentDay, count(*) as Appointments_count
from patients
group by AppointmentDay
order by Appointments_count desc
limit 1

# Task 5: Calculate the monthly average number of appointments in the given dataset
with cte as(select *, date_format(AppointmentDay, '%Y-%m') as month
from patients)

select month, count(*) as c
from cte
group by month

# Task 6: Find the month with the highest number of appointments in the given dataset
with cte as(select *, date_format(AppointmentDay, '%Y-%m') as month
from patients)

select month, count(*) as c
from cte
group by month
order by c desc
limit 1

# Task 7: Calculate the weekly average number of appointments in the given dataset
with cte as(select *, Date_format(AppointmentDay, '%Y') as year, Date_format(AppointmentDay, '%v') as week
from patients)

select year, week, count(*) as Appointments_count
from cte
group by year, week

# Task 8: Find the week with the highest number of appointments in the given dataset
with cte as(select *, date_format(AppointmentDay, '%Y') as year, date_format(AppointmentDay, '%v') as week
from patients)

select year, week, count(*) as c 
from cte 
group by year, week
order by c desc
limit 1

# Task 9: What is the distribution of appointments based on gender in the dataset
select Gender, count(*) as Gender_counts
from patients
group by Gender

with cte as(select *, dayname(AppointmentDay) as day 
from patients)

# Task 10: Calculate the number of appointments per weekday in the given dataset. Order the appointment counts in descending
select day, count(*) as c 
from cte 
where day not in ('Sunday')
group by day 

# Task 11: Calculate the average time between scheduling and the appointment day in the given dataset. Set to nearest whole number
with cte as(select *, datediff(AppointmentDay, ScheduledDay) as d 
from patients)

select round(avg(d), 0) as Avg_Days_Between_Appointments
from cte
