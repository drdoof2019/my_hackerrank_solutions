def timeConversion(s):
    # Write your code here
    # print("s", s)
    t_zone = s[-2:]
    s = s[:-2]
    hour, minute, second = s.split(":")
    # print(type(hour))
    if t_zone == "PM":
        if int(hour) < 12:
            hour = str(int(hour) + 12)
        result = hour + ":" + minute + ":" + second
        #print(result)
        return result
        
    else: # AM
        if hour == "12":
            hour = "00"
        result = hour + ":" + minute + ":" + second
        #print(result)
        return result
