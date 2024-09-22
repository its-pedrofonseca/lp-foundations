from enum import Enum

class Region(Enum):
    AL = 'AL'
    AM = 'AM'
    AT = 'AT'
    AZ = 'AZ'
    BE = 'BE'
    BG = 'BG'
    BY = 'BY'
    CH = 'CH'
    CY = 'CY'
    CZ = 'CZ'
    DE = 'DE'
    DE_TOT = 'DE_TOT'
    DK = 'DK'
    EA18 = 'EA18'
    EA19 = 'EA19'
    EE = 'EE'
    EEA30_2007 = 'EEA30_2007'
    EEA31 = 'EEA31'
    EFTA = 'EFTA'
    EL = 'EL'
    ES = 'ES'
    EU27_2007 = 'EU27_2007'
    EU27_2020 = 'EU27_2020'
    EU28 = 'EU28'
    FI = 'FI'
    FR = 'FR'
    FX = 'FX'
    GE = 'GE'
    HR = 'HR'
    HU = 'HU'
    IE = 'IE'
    IS = 'IS'
    IT = 'IT'
    LI = 'LI'
    LT = 'LT'
    LU = 'LU'
    LV = 'LV'
    MD = 'MD'
    ME = 'ME'
    MK = 'MK'
    MT = 'MT'
    NL = 'NL'
    NO = 'NO'
    PL = 'PL'
    PT = 'PT'
    RO = 'RO'
    RS = 'RS'
    RU = 'RU'
    SE = 'SE'
    SI = 'SI'
    SK = 'SK'
    SM = 'SM'
    TR = 'TR'
    UA = 'UA'
    UK = 'UK'
    XK = 'XK'

    @classmethod
    def countries(cls):
        """Returns a list of reions that are countries"""
        
        non_countries = {
            'DE_TOT', 
            'EA18', 
            'EA19', 
            'EEA30_2007', 
            'EEA31', 
            'EFTA',
            'EU27_2007', 
            'EU27_2020', 
            'EU28'
        }
        return [region for region in cls if region.value not in non_countries]
