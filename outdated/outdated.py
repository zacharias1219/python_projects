months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    try:
        m,d,y = date.split("/")
        if(int(d)>0 and int(d)<32) and (int(m)>0 and int(m)<13):
            break
    except:
        try:
            pm,pd,y = date.split(" ")
            for i in range (len(months)):
                if pm == months[i]:
                    m = i+1
                    break
            if ',' in pd:
                d = pd.replace(",","")
            if(int(d)>0 and int(d)<32) and (int(m)>0 and int(m)<13):
                break
        except:
            print()
            pass
print(f"{y}-{int(m):02}-{int(d):02}")
