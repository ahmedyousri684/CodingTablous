from tqdm import tqdm

product_codes_filename = "codes.txt"
with open(product_codes_filename, "r") as f:
    with open("require_products.txt", "w") as fW:
        all_codes = f.readlines()
        for code in tqdm(all_codes):
            split_code = code.split("\n")[0]
            if len(split_code) > 0:
                fW.write(f"require('../assets/products/{str(split_code)}.jpg'),")
                fW.write("\n")
