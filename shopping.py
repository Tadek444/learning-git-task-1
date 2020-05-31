print ("Lista zakupów")
shopping_dict = {
    'piekarnia' : ['chleb', 'pączek', 'bułki']
}
for sklep, product in shopping_dict.items():  
    print (f'Idę do {sklep}, kupuję tu nastepujące rzeczy:{product}')  