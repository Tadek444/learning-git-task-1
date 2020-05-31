print ("Lista zakupów")
shopping_dict = {
    'piekarnia' : ['chleb', 'pączek', 'bułki'],
     'warzywniak': ['marchew', 'seler', 'rukola']
     }
for shop, products in shopping_dict.items():   	# produkty z jednego sklepu
    produkty = []				                # zerujemy listę produktów
    for p in products:				            # dla każdego elementu z listy product
        produkty.append(p.title()) 		        # dodaj produkty z pierwszą dużą literą	    
    produkty = ", ".join(produkty)		        # metoda join ciąg znaków przecinek, produkt
    print(f'Idę do {shop.title()}, kupuję tu następujące rzeczy: {produkty}')
ile = 0					                        # zerujemy pętlę for na początku
for products in shopping_dict.values():         # wyciągamy produkty z produktów słownika shopping_dict 
    ile += len(products)	                    # zliczamy ilość wystapień produktów
print(f'W sumie kupuję {ile}, produktów')       # drukujemy ilość produktów

   