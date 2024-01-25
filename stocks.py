#CS175L
#Lynda Levy
#stocks
commRateBuy = float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))
commRateSell = float(input("Enter commision rate percentage (ex 0.03) on stock sale: "))
numBuy = int(input("Enter number of shares being purchased: "))
numSell = int(input("Enter number of shares sold: "))
pricePerShareBuy = float(input("Enter purchase price per share: "))
pricePerShareSell = float(input("Enter sell price per share: "))

amountPaidForStock = float(numBuy * pricePerShareBuy)
purchaseCommission = float(commRateBuy * amountPaidForStock)
totalPaid = float(amountPaidForStock + purchaseCommission)
stockSoldFor = float(numBuy * pricePerShareSell)
sellingCommission = float(commRateSell * stockSoldFor)
totalReceived = float(stockSoldFor - sellingCommission)
profitOrLoss = float(totalReceived - totalPaid)

print(" ")
print("Amount paid for the stock: $" + '{:,.2f}'.format(amountPaidForStock))
print("Commission paied on the purchase: $" + '{:,.2f}'.format(purchaseCommission))
print("Amount the stock sold for: $" + '{:,.2f}'.format(stockSoldFor))
print("Commission paid on the sale: $" + '{:,.2f}'.format(sellingCommission))
print("Profit (or loss if negative): $" + '{:,.2f}'.format(profitOrLoss))
