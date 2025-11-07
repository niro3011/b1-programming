#This Program is for calculating the revenue, costs and profit margin
print("Business Calculator")
revenue = float(input("please put in your revenue:"))
cost = float(input("please input your costs:"))
profit = revenue - cost
profitmargin = (profit / revenue)*100

print("Your profit is: ",profit,"$")
print("your profitmargin is: ",profitmargin,"%")
