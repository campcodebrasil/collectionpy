
def number_to_money(number, simbol=False, txt_simbol='brl'):

    if txt_simbol.lower() == 'us': S = '$'
    else: S = 'R$'

    number = '{:,.2f}'.format(number).replace('.', '|').replace(',', '.').replace('|', ',')

    if simbol: number = f"{S} {number}"
    return number


def number_to_percent(number, simbol=True):
    simbol = '%' if simbol else ''
    return '{:.2f}{}'.format(number * 100, simbol)
