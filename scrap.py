import pandas as pd
from selenium.webdriver.common.by import By


def scrap(df, df2, data, i, k, n):
    for hora in data:
        try:
            df   = df.append( pd.Series(data[i].get_attribute('data-hour'))  , ignore_index=True)
            i    = i+1
        except:
            print('Hubo un error')
    for hora in data:
        try:
            df2  = df2.append( pd.Series(data[k].find_elements(By.CSS_SELECTOR,'div')[1].get_attribute('style')) , ignore_index=True) 
            k = k + 1
        except:
            print('Hubo un error')
    df2 = (df2[0].str.split(expand=True)[1]).str.split('p', expand=True)[0].str.split(expand=True)
    df.columns=['Horas']
    df2.columns=['Cantidad']
    df3 = pd.concat([df, df2], axis=1)
    df3 = df3.assign( Dia  = n)
    return df3