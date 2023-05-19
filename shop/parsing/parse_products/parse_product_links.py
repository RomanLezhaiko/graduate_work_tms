import time
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://21vek.by/")
time.sleep(5)


button_cookies = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/button[2]')
button_cookies.click()
time.sleep(2)

categories_list = []
with open('E:\\R\python_projects\\parsing_21_vek\\parse_products\\category.json','r') as f:
    categories_list = json.load(f)


products_by_category = []
i = 0
for tmp_dict in categories_list:
    if 'link' in tmp_dict.keys():
        try:
            driver.get(tmp_dict['link'])
            time.sleep(3)
            
            products_result = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div[1]/div[6]/ul')
            soup = BeautifulSoup(products_result.get_attribute('innerHTML'), "html.parser")
            lis = soup.findAll('li')
            
            links = []
            for li in lis:
                links.append(li.find('a'))
            
            hrefs_dict = {}
            counter = 1
            # links_href = []
            for link in links:
                if counter == 11:
                    break
                
                hrefs_dict[counter] = link['href']
                # links_href.append(link['href'])
                # print(link['href'])
                counter += 1
            
            tmp_dict['products'] = hrefs_dict
            products_by_category.append(tmp_dict)   
            
            with open("E:\\R\python_projects\\parsing_21_vek\\parse_products\\products_by_category.json", "w") as outfile:
                json.dump(products_by_category, outfile, indent=4)
           
        except Exception:
            continue

        i += 1
        if i == 100:
            break


driver.close()