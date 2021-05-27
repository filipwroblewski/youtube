def quarter_of(month):
    quarter = 0
    if month in [1,2,3]:
        quarter = 1
        print(f'month: {month} --> quarter: {quarter}')
    elif month in [4,5,6]:
        quarter = 2
        print(f'month: {month} --> quarter: {quarter}')
    elif month in [7,8,9]:
        quarter = 3
        print(f'month: {month} --> quarter: {quarter}')
    elif month in [10,11,12]:
        quarter = 4
        print(f'month: {month} --> quarter: {quarter}')
    print(quarter)
    return quarter

quarter_of(3)	# 1
quarter_of(8)	# 3
quarter_of(11)  # 4