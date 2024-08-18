import pandas as pd

import numpy as np


firstName = 'Raqs'
lastName = 'Soriano'

testfString = f'{firstName}', {lastName}

combinedName = firstName + ' ' + lastName

print(testfString) 

print(combinedName)


wbc_test = ['3500',
            '4000',
            '8000',
            '12000',
            ]

len(wbc_test)


def bloodtestanalysis(**kwargs):
    wbc_test = kwargs.get('wbc', None)

    if wbc_test >=4000 and wbc_test <12000:
        print('The blood test is within normal range')
    else:
        print('The blood test is abnormal range')

    result = {
        'wbc': wbc_test,
    }
    return result

bloodtestanalysis(wbc=4000)
bloodtestanalysis(wbc=15000)


