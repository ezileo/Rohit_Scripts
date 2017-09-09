streetno={
    "1":"Sachin Tendulkar",
    "2":"Sehawag",
    "3":"Dravid",
    "4":"Dhoni",
    "5":"Kohli"
}

key = input("Enter name or number (i/p):")
result = streetno.get(key)
print(result)