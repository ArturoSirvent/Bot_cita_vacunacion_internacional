#!/usr/bin/env python
# coding: utf-8

# In[90]:


from selenium import webdriver
import os 
import numpy as np
from selenium.webdriver.common import keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


# In[86]:


#!pip install phantomjs


# In[91]:


#cargamos el driver

chrome_options = Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome("./driver/chromedriver",options=chrome_options )
#driver=webdriver.PhantomJS()


# In[92]:


#ahora vamos a cargar la pagina de interes
driver.get("https://sisaex-vac-cita.mscbs.gob.es/sanitarios/consejos/inicioAction.do")


# In[ ]:


#se rellena como texto y lso meses empiezan el 0
#el sexo es "H" o "M"
mis_datos={"dia_nacimiento": ,
          "mes_nacimiento": ,
          "anyo_nacimiento": , 
          "sexo": ,
          "dia_viaje": ,
          "mes_viaje": ,
          "anyo_viaje": ,
          "dracion": ,
          "provincia": ,
          "DNI": ,
          "nombre": 
          "apellido1": ,
          "apellido2": ,
          "telefono": ,
          "email": , 
          }


# In[93]:


#y tenemos qeu hacer una secuencia de acciones para que clique
#y rellene los formularios donde toca
driver.find_element_by_xpath('//button[@name="comenzar"]').click()


# In[94]:


#metemos las fechas y el sexo
Select(driver.find_element_by_xpath('//select[@name="dia"]')).select_by_value(mis_datos["dia_nacimiento"])
Select(driver.find_element_by_xpath('//select[@name="mes"]')).select_by_value(mis_datos["mes_nacimiento"])
Select(driver.find_element_by_xpath('//select[@name="anyo"]')).select_by_value(mis_datos["anyo_nacimiento"])
Select(driver.find_element_by_xpath('//select[@name="sexo"]')).select_by_value(mis_datos["sexo"])
driver.find_element_by_xpath('//input[@name="continuar"]').click()


# In[95]:


#metemos los paises
Select(driver.find_element_by_xpath('//select[@name="codigoPais"]')).select_by_value("PA")
driver.find_element_by_xpath('//input[@name="incluir"]').click()


# In[96]:


#siguiente pagina
driver.find_element_by_xpath('//input[@name="continuar"]').click()


# In[97]:


#tipo de viaje
Select(driver.find_element_by_xpath('//select[@name="codigoTipo"]')).select_by_value("1")
driver.find_element_by_xpath('//input[@name="incluir"]').click()


# In[98]:


#siguiente pagina

driver.find_element_by_xpath('//input[@name="continuar"]').click()


# In[99]:


#metemos las fechas y la diracion
Select(driver.find_element_by_xpath('//select[@name="dia"]')).select_by_value(mis_datos["dia_viaje"])
Select(driver.find_element_by_xpath('//select[@name="mes"]')).select_by_value(mis_datos["mes_viaje"])
Select(driver.find_element_by_xpath('//select[@name="anyo"]')).select_by_value(mis_datos["anyo_viaje"])
driver.find_element_by_xpath('//input[@name="duracion"]').clear()
driver.find_element_by_xpath('//input[@name="duracion"]').send_keys(mis_datos["duracion"])
driver.find_element_by_xpath('//input[@name="continuar"]').click()


# In[100]:


driver.find_element_by_xpath('//input[@value="Citar sin certificado digital"]').click()


# In[101]:


Select(driver.find_element_by_xpath('//select[@name="codigoProvincia"]')).select_by_value(mis_datos["provincia"])
driver.implicitly_wait(0.2)
driver.find_element_by_xpath('//input[@name="continuar"]').click()


# In[102]:


#ahora rellenamos mis datos 
driver.find_element_by_xpath('//input[@name="nif"]').send_keys(mis_datos["DNI"])
driver.find_element_by_xpath('//input[@name="nombre"]').send_keys(mis_datos["nombre"])
driver.find_element_by_xpath('//input[@name="apellido1"]').send_keys(mis_datos["apellido1"])
driver.find_element_by_xpath('//input[@name="apellido2"]').send_keys(mis_datos["apellido2"])
driver.find_element_by_xpath('//input[@name="telefono"]').send_keys(mis_datos["telefono"])
driver.find_element_by_xpath('//input[@name="email"]').send_keys(mis_datos["email"])
driver.implicitly_wait(0.2)
driver.find_element_by_xpath('//input[@name="addViajero"]').click()
driver.implicitly_wait(0.5)


# In[103]:


driver.find_element_by_xpath('//input[@name="continuar"]').click()


# In[104]:


#por último, tenemos que hacer un bucle que vaya por todas la fechas de hoy hacia adelante, 
#y pare cuando encuentre a fecha mas cercana

#fata una fecha, se ejecuta esto
for i in [5,6]:
    for j in range(1,31):

        Select(driver.find_element_by_xpath('//select[@name="dia"]')).select_by_value(str(j))
        Select(driver.find_element_by_xpath('//select[@name="mes"]')).select_by_value(str(i))
        Select(driver.find_element_by_xpath('//select[@name="anyo"]')).select_by_value("2022")
        #driver.implicitly_wait(0.1)
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="cambiarFecha"]')))
        #driver.find_element_by_xpath('//input[@name="cambiarFecha"]').click()
        #driver.implicitly_wait(0.1)
        element.click();
        #y una vez cambiada la fecha, se intenta sacar la tabla y si sale por algun lado
        #la palabra cita y tal
        try:
            aux=driver.find_elements_by_xpath('//tr//input[@name="cita"]')
        except:
            print("Nop")
            
        if aux:
            print(f"Para el día {j}, mes {i}, si hay citas.")
        else:
            pass


# In[ ]:




