import requests
from tqdm import tqdm

codes_filename = "codes.txt"
url = "http://techwoody-001-site1.gtempurl.com/api/Product/AddProduct"

with open(codes_filename, "r") as f:
    all_codes = f.readlines()
    print(all_codes)
    for code in tqdm(all_codes):
        product_type = code[1]
        if product_type == "M":
            new_product = {
                "description": "",
                "productCode": str(code.split("\n")[0]),
                "image": "",
                "smallPrice": 300,
                "mediumPrice": 350,
                "largePrice": 400,
                "type": "Multi",
            }
            x = requests.post(url, json=new_product)
        elif product_type == "S":
            new_product = {
                "description": "",
                "productCode": str(code.split("\n")[0]),
                "image": "",
                "smallPrice": 250,
                "mediumPrice": 275,
                "largePrice": 300,
                "type": "Single",
            }
            x = requests.post(url, json=new_product)
