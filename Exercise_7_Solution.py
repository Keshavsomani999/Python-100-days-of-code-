import os

files = os.listdir("cluster")
i =1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"cluster/{file}",f"cluster/{i}.png")
        i=i+1

