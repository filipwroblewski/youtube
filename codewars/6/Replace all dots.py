def replace_dots(str):
    return str.replace('.', '-')

replace_dots("")    # ""
replace_dots("no dots") # "no dots"
replace_dots("one.two.three")   # "one-two-three"
replace_dots("........")    # "--------"