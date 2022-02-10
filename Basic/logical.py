''' AND: both has to be true
    or :at least one has to be true'''
has_good_credit=True
has_criminal_record=False
if has_good_credit or not has_criminal_record:
    print('eligable for loan')
