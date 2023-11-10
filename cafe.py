menu=["Americano","Cafe Latte","Hot chocolate","Chai Latte"]
stock={ "Americano": 5,
        "Cafe Latte": 10,
        "Hot chocolate": 6,
        "Chai Latte": 9,
        }
price={ "Americano": 2,
        "Cafe Latte": 2.5,
        "Hot chocolate": 2.5,
        "Chai Latte": 3}

total_stock=0
for item in menu:
    total_stock+=stock[item]*price[item]

print(total_stock) 