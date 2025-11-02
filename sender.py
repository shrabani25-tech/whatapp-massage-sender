import pywhatkit
import datetime

# Student attendance data (roll: [name, parent_number, absent_days])
students = {
    1: ["Rahul", "+918927448962", 5],
    2: ["Priya", "+918927448862", 2],
    3: ["Amit", "+915451254512", 1],
}

# Absent limit
ABSENT_LIMIT = 3

# Loop through students
for roll, data in students.items():
    name, parent_number, absent_days = data
    
    if absent_days > ABSENT_LIMIT:
        # Message for parents
        message = f"Dear Parent, your child {name} has been absent for {absent_days} days. Please ensure regular attendance."
        
        # Current time + 1 min (WhatsApp requires future time)
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1
        if minute>=60:
            minute=minute%60
            hour=(hour+1)%24
        
        print(f"Sending WhatsApp message to {name}'s parents...")
        
        # Send message
        pywhatkit.sendwhatmsg_instantly(parent_number, message,wait_time=20,tab_close=True)