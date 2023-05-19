import json
import os

images_list = []
with open('/home/roman/dev/git_projects/graduate_work_tms/shop/parsing/parse_products_image/products_image_data_new.json', 'r') as f:
    images_list = json.load(f)

data = []
for tmp_dict in images_list:
    path = 'products/management/commands/product_images'
    name = tmp_dict['image_path'].split("\\")[-1]

    full_path = os.path.join(path, name)
    tmp_dict['image_path'] = full_path
    data.append(tmp_dict)


with open('/home/roman/dev/git_projects/graduate_work_tms/shop/parsing/parse_products_image/images_data_final.json', 'w') as f:
    json.dump(data, f, indent=4)