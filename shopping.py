print ("Lista zakupów")
shopping_dict = {
    'piekarnia' : ['chleb', 'pączek', 'bułki'],
     'warzywniak': ['marchew', 'seler', 'rukola']
     }
for shop, products in shopping_dict.items():   	# produkty z jednego sklepu
    produkty = []				# zerujemy listę produktów
    for p in products:				# dla każdego elementu z listy product
        produkty.append(p) 		# dodaj produkty z pierwszą dużą literą	    
    produkty = ", ".join(produkty)		#metoda join ciąg znaków przecinek, produkt
    print(f'Idę do {shop}, kupuję tu następujące rzeczy: {produkty}')