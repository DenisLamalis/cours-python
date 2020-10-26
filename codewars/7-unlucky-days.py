def unlucky_days(year):
    import calendar
    
    CALOBJ = calendar.Calendar()
    
    LUCKY = 0
    
    for month in range(1, 13):
        for day in CALOBJ.itermonthdays2(year, month):
            if day[0] == 13 and day[1] == 4:
                LUCKY = LUCKY + 1
    return LUCKY