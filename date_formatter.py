import calendar
def format_date(date_string):
    month, day, year = date_string.split()
    d = day.split(",")[0]
   
    if len(d) < 2:
        day = f"{int(d):02d}"
    else:
        day = d
    
    for ind, m in enumerate(list((calendar.month_name))):
        if m == month:
            month = f"{int(ind):02d}"
            
    
    return f"{year}-{month}-{day}"



print(format_date("December 6, 2025"))
print(format_date("January 1, 2000"))
print(format_date("November 11, 1111"))