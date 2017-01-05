
def output_customer_payment_errors():
    """Get customer info for comparison of what was paid, what is owed, what 
    overpaid
    """
    customer_file = open("customer-orders.txt")
    for each_line in customer_file:
        each_line = each_line.rstrip()
        customer_info = each_line.split('|')

        customer_number = customer_info[0]
        customer_name = customer_info[1]
        customer_melons_num = float(customer_info[2])
        customer_paid = float(customer_info[3])
        #print customer_melons_num
        #print customer_paid
        if customer_paid != customer_melons_num:
            print "{} paid ${}, expected ${}".format(
            customer_name, customer_paid, customer_melons_num)
    customer_file.close()
output_customer_payment_errors()

#
#melon_cost = 1.00

#customer1_name = "Joe"
#customer1_melons = 5
#customer1_paid = 5.00

#customer2_name = "Frank"
#customer2_melons = 6
#customer2_paid = 6.00

#customer3_name = "Sally"
#customer3_melons = 3
#customer3_paid = 3.00

#customer4_name = "Sean"
#customer4_melons = 9
#customer4_paid = 9.50

#customer5_name = "David"
#customer5_melons = 4
#customer5_paid = 4.00

#customer6_name = "Ashley"
#customer6_melons = 3
#customer6_paid = 2.00

