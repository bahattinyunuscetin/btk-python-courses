# with open("markalar.txt","a") as file:
#     file.write("6-Bmw")

# with open("markalar.txt","r+", encoding="utf-8") as file:
#     markalar = file.read()       #başına eklemek için listeyi diziye al ve tekrar birleştir
#     markalar = "1-Toyota\n" + markalar
#     file.seek(0)
#     file.write(markalar)

with open("markalar.txt","r+",encoding="utf-8") as file:
    markalar = file.readlines()    # listeye al ve insert metoduyla ekle
    markalar.insert(2, "3-Renault\n")
    file.seek(0)
    # for marka in markalar:
    #     file.write(marka)
    file.writelines(markalar)


with open("markalar.txt", "r", encoding="utf-8") as file:
    print(file.read())