import json
import os

products_list = []
with open('/home/roman/dev/git_projects/graduate_work_tms/shop/parsing/parse_products/products_data_new.json', 'r') as f:
    products_list = json.load(f)

data = []
for tmp_dict in products_list:
    path = 'products/management/commands/images_main'
    name = tmp_dict['main_image_path'].split("\\")[-1]

    full_path = os.path.join(path, name)
    tmp_dict['main_image_path'] = full_path
    data.append(tmp_dict)


with open('/home/roman/dev/git_projects/graduate_work_tms/shop/parsing/parse_products/products_data_final.json', 'w') as f:
    json.dump(data, f, indent=4)