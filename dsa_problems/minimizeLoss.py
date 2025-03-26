
def cnt_loss(price):
    min_loss = float('inf')
    buy_year, sell_year = -1, -1
    n = len(price)
    
    for buy in range(n - 1):
        for sell in range(buy + 1, n):
            if price[sell] < price[buy]:
                loss = price[buy] - price[sell]
                if loss < min_loss:
                    min_loss = loss
                    buy_year = buy + 1
                    sell_year = sell + 1
    
    if buy_year == -1:
        print("No valid loss found")
    else:
        print(f"Buy in year {buy_year} and sell in year {sell_year} with a loss of {min_loss}")


n = int(input("Enter total number of years: "))
price = list(map(int, input("Enter prices: ").split()))
cnt_loss(price)