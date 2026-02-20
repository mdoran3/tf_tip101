def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"
    
print(classify_age(18))
print(classify_age(17))
print(classify_age(50))