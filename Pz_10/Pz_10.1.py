#В магазинах имеютс следующие товары. Магнит - молоко, соль,
#сахар печенье, сыр. Пятёрочка - мясо, молоко, сыр
#Перекрёсток - молоко, творог, сыр, сахар, печенье
#Лента - печенье, молоко, сыр, сметана
#Определить:
#1. в каких магазинах нельзя приобрести сметану
#2. какие товары из магазина Магнит отсутствуют в магазине Перекрёсток
#3. какие товары из магазина Лента отсутствуют в магазине Магнит
Magnit = {"молоко", "соль", "сахар", "печенье", "сыр"}
Pyaterochka = {"мясо", "молоко", "сыр"}
Perekrestok = {"молоко", "творог", "сыр", "сахар", "печенье"}
Lenta = {"печенье", "молоко", "сыр", "сметана"}
smetana = {"сметана"}
print("1. Сметану нельзя приобрести в магазинах:")
if smetana & Magnit != smetana:
    print("Магнит")
if smetana & Pyaterochka != smetana:
    print("Пятёрочка")
if smetana & Perekrestok != smetana:
    print("Перекрёсток")
if (smetana & Lenta) != smetana:
    print("Лента")
print("2. Какие товары из магазина Магнит отсутствуют в магазине Перекрёсток: ", Magnit - Perekrestok)
print("3. Какие товары из магазина Лента отсутствуют в магазине Магнит: ", Lenta - Magnit)


