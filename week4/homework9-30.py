#kaiden zhou
print("4.1\n")

peanutCookies= 10
chocolateCookies= 15
peanutCookiePrice= 3
chocolateCookiePrice= 2



totalRevenue= peanutCookies * peanutCookiePrice + chocolateCookies * chocolateCookiePrice
print("Total revenue is " + str(totalRevenue)+"\n")


print("4.2\n")

#The chocolate price increased by 2 while peanut price increased by 1 
#thus variable + 1 or variable +2
newChocolateCookiePrice = chocolateCookiePrice + 2
newPeanutCookiePrice = peanutCookiePrice + 1

newTotalRevenue= peanutCookies * newPeanutCookiePrice + chocolateCookies * newChocolateCookiePrice
print("The new total revenue after the price increased " + str(newTotalRevenue))