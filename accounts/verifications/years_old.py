from datetime import date 


def verify_years_old(date_born):

    if date_born:
        year_atual = date.today().year
        date_born_year = int(date_born.split('-' if '-' in date_born else '/')[0])
        years_old = year_atual - date_born_year

        if years_old >= 13:
            return 'valid'
        else:
            return 'invalid'  
    else:
        return 'invalid'

