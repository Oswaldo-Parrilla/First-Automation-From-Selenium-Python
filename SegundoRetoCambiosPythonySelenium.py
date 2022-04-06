#Librerias
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #SE IMPLEMENTO ESTA LIBRERIA PARA EJECTURA EL WEBDRIVER DE DIFERENTE FORMA PARA LAS ULTIMAS ACTUALIZACIONES DE GOOGLE, SELENOUM Y PYTHON
from webdriver_manager.chrome import ChromeDriverManager #SE IMPLEMENTO ESTA LIBRERIA PARA EJECTURA EL WEBDRIVER DE DIFERENTE FORMA PARA LAS ULTIMAS ACTUALIZACIONES DE GOOGLE, SELENOUM Y PYTHON
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver_service = Service(executable_path="C:\Drivers\chromedriver.exe") #SE IMPLEMENTO ESTA LIBRERIA PARA EJECTURA EL WEBDRIVER DE DIFERENTE FORMA PARA LAS ULTIMAS ACTUALIZACIONES DE GOOGLE, SELENOUM Y PYTHON
driver = webdriver.Chrome(service=driver_service) #SE IMPLEMENTO ESTA LIBRERIA PARA EJECTURA EL WEBDRIVER DE DIFERENTE FORMA PARA LAS ULTIMAS ACTUALIZACIONES DE GOOGLE, SELENOUM Y PYTHON
# driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe") #FORMA ANTIGUA DE CONFIGURAR LA EJECUCION DE WEBDRIVER
driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
driver.maximize_window()
t = 1
#driver.execute_script("window.scrollTo(0,700)")

#Obteniendo los elementos
try:
    btn = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='submit']"))) #validar que existe el elemento boton.
    btn = driver.find_element(By.XPATH,"//input[@value='submit']") #Seleccionar el elemento para aplicar una accion que deseemos.
    ir = driver.execute_script("arguments[0].scrollIntoView();", btn) #Buscando el elemento haciendo scroll hasta donde este
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

#Identificando el elemento UserName
name_val = driver.find_element(By.XPATH,"//input[@name='username']")
name = name_val.text #guardara el texto de ese campo si es que contiene algun valor(texto)
# print("El valor del error es: " + name)
if(name == "Nombre de usuario incorrecto"):
    print("Falta el nombre")
elif(name == ""):
    name = driver.find_element(By.XPATH,"//input[@name='username']")
    name.send_keys("Oswaldo")
    time.sleep(t)
else:
    print("Nombre correcto")
time.sleep(t)

#Identificando el elemento password
pass_name = driver.find_element(By.XPATH,"//input[@name='password']")
passw = pass_name.text
# print("El valor del error es: " + name)
if(passw == ""):
    # print("Falta el nombre")
    pass1 = driver.find_element(By.XPATH,"//input[@name='password']")
    pass1.send_keys("Oswa1234")
    time.sleep(t)
else:
    print("Password Correcto")
time.sleep(t)

#Text Area
coment = driver.find_element(By.XPATH,"//textarea[contains(@cols,'40')]")
textArea = coment.text
# print("El valor del error es: " + name)
if(textArea == "Comments..."):
    #print("Existe el comentario")
    comentr = driver.find_element(By.XPATH,"//textarea[contains(@cols,'40')]")
    comentr.send_keys("Un saludo a todos mis contactos de LinkedIn")
    time.sleep(t)
else:
    print("Falta el Comentario")
time.sleep(t)

#Upload Image
try:
    upload = driver.find_element(By.XPATH,"//input[contains(@type,'file')]")
    upload.send_keys("C://Users//xSpectra//PycharmProjects//Curso_selenium//images//AsusGamgin.jpg")
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

#Checks Items
check = driver.find_element(By.XPATH,"//input[@value='cb1']")
check2 = driver.find_element(By.XPATH,"//input[@value='cb2']")
check.click()
time.sleep(1)
check2.click()
time.sleep(t)

#Radio Items
radioBtn = driver.find_element(By.XPATH,"//input[@value='rd2']")
radioBtn.click()
time.sleep(1)
radioBtn2 = driver.find_element(By.XPATH,"//input[@value='rd3']")
radioBtn2.click()
time.sleep(t)

#Multiple list
multi = Select(driver.find_element(By.NAME,"multipleselect[]"))
multi.select_by_index(0)
multi.select_by_index(2)
multi.select_by_index(3)
time.sleep(t)

#List
ds = Select(driver.find_element(By.XPATH,"//select[@name='dropdown']"))
ds.select_by_index(0)
time.sleep(t)

btn.click()
time.sleep(t)
driver.close()