#Program to calculate gst of given product and return the final bill

food_grain=['rice','wheat','dal']
furniture=['table','sofa','chair']
electronics=['mobile','tv','tablet']
cosmetics=['cream','perfume','lotion']


class GST_calculator:
        
    def calculate_GST(self,quant,product,price):
        sell_price=0
        
        #checking  negative value for price and quantity
        if(quant>0 and price >0):
            if product.lower() in food_grain:
                sell_price=quant*price
            
            elif product.lower() in furniture:
                
                #formula=price of product * gst_percent /100
                gst_on_product=price*5/100
                sell_price=quant*(gst_on_product+price)
                
            elif product.lower() in electronics:
                gst_on_product=price*18/100
                sell_price=quant*(gst_on_product+price)
                
            elif product.lower() in cosmetics:
                gst_on_product=price*28/100
                sell_price=quant*(gst_on_product+price)
                
            else:
                print("Product not found")
                
        else:
            print("invalid quantity or price")
    
        return sell_price
        
 # taking input from user      
print("Enter product to buy")
prod=input()
print("Enter quantity of {}".format(prod))
quant=int(input())
print("Enter price of {}".format(prod))
price=float(input())

#Object created for class
gst=GST_calculator()

#Call function of class using object
final_price=gst.calculate_GST(quant,prod,price)

if final_price>0:
    print("Your bill amount is {}".format(final_price))
    
    