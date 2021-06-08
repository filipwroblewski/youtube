def people_with_age_drink(age):
    drink=''
    if age < 14:
        drink = 'drink toddy'
    elif age < 18:
        drink = 'drink coke'
    elif age < 21:
        drink = 'drink beer'
    elif age >= 21:
        drink = 'drink whisky'
    return drink

# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
people_with_age_drink(13)   # 'drink toddy'
people_with_age_drink(0)    # 'drink toddy'
people_with_age_drink(17)   # 'drink coke'
people_with_age_drink(15)   # 'drink coke'
people_with_age_drink(14)   # 'drink coke'
people_with_age_drink(20)   # 'drink beer'
people_with_age_drink(18)   # 'drink beer'
people_with_age_drink(22)   # 'drink whisky'
people_with_age_drink(21)   # 'drink whisky'