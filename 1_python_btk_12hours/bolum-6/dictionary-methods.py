yemekTarifi = {
    "yemekAdi": "Musakka",
    "yemekTarifi": "tarif açıklaması",
    "resim": "1.jpg"
}

# access items
sonuc = yemekTarifi["yemekAdi"]
sonuc = yemekTarifi.get("yemekAdi")   
sonuc = yemekTarifi.keys()    #dict_keys(['yemekAdi', 'yemekTarifi', 'resim']) 

sonuc = yemekTarifi.values()  #dict_values(['Musakka', 'tarif a��klamas�', '1.jpg'])

sonuc = yemekTarifi.items()  #dict_items([('yemekAdi', 'Musakka'), ('yemekTarifi', 'tarif a��klamas�'), ('resim', '1.jpg')])
print(sonuc)

# update items
# yemekTarifi["yemekAdi"] = "Mantı"  
# yemekTarifi.update({"yemekAdi":"Mantı"}) 
# yemekTarifi.update({"yemekAdi2":"Mantı"})

# delete items
# yemekTarifi.pop("yemekAdi")    
# yemekTarifi.popitem()   #son eklenen elemanı siler
yemekTarifi.clear()   #listeyi boşaltır


# copy => referans

sonuc = yemekTarifi

print(sonuc)