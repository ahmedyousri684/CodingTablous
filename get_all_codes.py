import os

FILE_PATH = "data"
output_file = "codes.txt"

with open(output_file, "w") as f:
    counter = 0
    for collection in os.listdir(FILE_PATH):
        for image in os.listdir(os.path.join(FILE_PATH, collection)):
            counter += 1
            f.write(image.split(".")[0])
            f.write("\n")
    f.write("\n")
    print("Number of images:" + str(counter))
