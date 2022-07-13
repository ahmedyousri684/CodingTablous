import os
FILE_PATH = 'Final-Collections'

collections = os.listdir(FILE_PATH)
for collection in collections:
    split_collection = collection.split("-")
    if split_collection[0] == 'C':
        first_char = "T"
    if int(split_collection[1]) < 10:
        collection_digit = "0"+ split_collection[1]
    else:
        collection_digit = split_collection[1]   
    print(collection_digit)
    for image in os.listdir(os.path.join(FILE_PATH, collection)):
        split_image = image.split(".")
        if split_image[0] == "M":
            second_char = "M"
            if int(split_image[1]) < 10:
                image_digit = "0" + split_image[1]
            else:
                image_digit = split_image[1]
        else:
            second_char = "S"
            if int(split_image[0]) < 10:
                image_digit = "0" + split_image[0]
            else:
                image_digit = split_image[0] 
        print(split_image)
        #Rename image based on the new code
        image_code = first_char+second_char+"-"+collection_digit+image_digit+".jpg"
        os.rename(os.path.join(FILE_PATH,collection,image),os.path.join(FILE_PATH,collection,image_code))
        
    