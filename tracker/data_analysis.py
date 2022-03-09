def checkingData(symbol, actual_price, price_yesterday):
    if float(actual_price) > (price_yesterday):
        email_message = f"{symbol} cost more than yesterday by {round(actual_price-price_yesterday, 3)}$"
    if float(actual_price) < (price_yesterday):
        email_message = f"{symbol} cost less than yesterday by {round(price_yesterday-actual_price, 3)}$"
    return email_message