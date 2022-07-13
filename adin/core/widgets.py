import datetime

from django.forms import SelectDateWidget

class SelectDateSpanishWidget(SelectDateWidget):

    def __init__(self,attrs=None, years=None, months=None, empty_label=None):
        years = range(1970, datetime.date.today().year + 10)
        months = {
            1: 'Enero',
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Septiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12: 'Diciembre'
        }
        super().__init__(attrs, years, months, empty_label)