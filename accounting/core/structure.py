# This class provides accounts's structure
import pandas as pd

class Account_Structure:
        
    _LEVELS = pd.DataFrame(
        data={'level':[0,1,2,3,4,5],
              'parent':[None,0,1,2,3,4], 
              'len':[1,2,4,6,8,10]},
    ).set_index('level', drop=False)

    _ACCOUNT_NATURE = {
        '1':'Debit',
        '2':'Credit',
        '3':'Credit',
        '4':'Debit',
        '5':'Credit',
        '6':'Debit',
        '7':'Credit',
        '8':'Debit',
        '9':'Credit'
    }
        
    @classmethod
    def levels_full(cls, code):
        return cls._LEVELS['len'].apply(lambda l:str(code)[:l] if l<=len(str(code)) else code)
        
    @classmethod
    def levels_nan(cls, code):
        return cls._LEVELS['len'].apply(lambda l:str(code)[:l] if l<=len(str(code)) else None)

    @classmethod
    def nature(cls, code):
        return cls._ACCOUNT_NATURE[str(code)[0]]
