def create_order(customer, *skus):
    print("The customer name is :"+customer)

    for sku in skus:
        print(sku)
customer_name = "Customer1"

create_order(customer_name, 12548, 58965, 1455, 454545)