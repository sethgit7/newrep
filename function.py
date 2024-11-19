def validate():
    validdigit = 10
    data = str(input('Enter you 10 digit mobile no:'))
    totallength = len(data)
    print(totallength)
    if totallength == 10:
        print('Valid length')
    elif totallength < 10:
        print('Invalid length')
        balancedigit = validdigit - totallength

        print('total missing digits', balancedigit)
        print('make sure you have 10 digit')
    else:
        print('total length exceeded')
        extra = totallength - validdigit
        print('total exceeded digit:', extra)
        print('please remove it')
validate()




