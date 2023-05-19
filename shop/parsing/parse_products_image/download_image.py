import json
import time
import requests


products_image_data = []
with open('E:\\R\python_projects\\parsing_21_vek\\parse_products_image\\products_image_data.json','r') as f:
    products_image_data = json.load(f)

i = 1
data = []
for tmp_dict in products_image_data:
    print(i)
    name = tmp_dict['image_href'].split('/')[-1]
    
    url = tmp_dict['image_href']
    response = requests.get(url)


    with open(f"E:\\R\\python_projects\\parsing_21_vek\\parse_products_image\\images\\{name}", "wb") as f:
        f.write(response.content)
    
    
    tmp_dict['image_path'] = f"E:\\R\\python_projects\\parsing_21_vek\\parse_products_image\\images\\{name}"
    data.append(tmp_dict)
    
    time.sleep(1)
    i += 1


with open("E:\\R\python_projects\\parsing_21_vek\\parse_products_image\\products_image_data_new.json", "w") as outfile:
    json.dump(data, outfile, indent=4)