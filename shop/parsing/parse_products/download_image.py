import json
import time
import requests


products_data = []
with open('E:\\R\python_projects\\parsing_21_vek\\parse_products\\products_data.json','r') as f:
    products_data = json.load(f)

data = []
for tmp_dict in products_data:
    name = tmp_dict['main_image_href'].split('/')[-1]
    # print(name)
    
    url = tmp_dict['main_image_href']
    response = requests.get(url)


    with open(f"E:\\R\\python_projects\\parsing_21_vek\\parse_products\\images\\{name}", "wb") as f:
        f.write(response.content)
    
    
    tmp_dict['main_image_path'] = f"E:\\R\\python_projects\\parsing_21_vek\\parse_products\\images\\{name}"
    data.append(tmp_dict)
    
    time.sleep(2)


with open("E:\\R\python_projects\\parsing_21_vek\\parse_products\\products_data_new.json", "w") as outfile:
    json.dump(data, outfile, indent=4)