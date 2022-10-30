"""
pip install selenium
pip install webdriver_manager.chrome
pip install packaging

"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

import pandas as pd

from scrap import scrap

def scrapingPublic():
    
    url = 'https://www.google.com/search?q=cordoba+shopping&oq=cordoba+shoop&aqs=edge.1.69i57j0i10i131i433i512j0i10i512l7.6107j0j1&sourceid=chrome&ie=UTF-8'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    data = driver.find_elements(By.CSS_SELECTOR,'div[role="radiogroup"]')

    data = driver.find_elements(By.CSS_SELECTOR,'div[data-hour]')

    i    = 0
    k    = 0
    df   = pd.DataFrame()
    df2  = pd.DataFrame()
    df3  = pd.DataFrame()

    daysWeeks = {
        'lun'    : 1,
        'mar'   : 2,
        'mié': 3,
        'jue'   : 4,
        'vie'  : 5,
        'sáb'   : 6,
        'dom'  : 7
    }

    for key, value in daysWeeks.items():
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()= '"+key+"']"))).click()
        df3 = df3.append(scrap(df, df2, data, i, k, value))
        i    = 0
        k    = 0

    return df3.to_csv('distribucion_dia_horario.csv', sep=';', index=False)