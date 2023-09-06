import csv

class Item:
    all =[]
    transport=0.04  #of total profit
    def __init__(self,name,buying_price,selling_price,quantity):
        # validation
        assert buying_price or selling_price >=0 ,f"price should be greater or equal to zero"
        assert quantity >=0 ,f"quantity should be greater or equal to zero"
        # Attributes
        self.__name=name
        self.buying_price=buying_price
        self.selling_price=selling_price
        self.quantity=quantity
        Item.all.append(self)
    #methods 
    def calculate_total_price(self):
        return self.selling_price * self.quantity


    def calculate_lose_profit(self):
        if self.selling_price>self.buying_price:
            self.buying_price=self.selling_price-self.buying_price
            return f"Profit for {self.__name}s is {self.buying_price}"
        elif self.buying_price > self.selling_price:
            self.buying_price=self.buying_price-self.selling_price
            return f"Total lose for {self.__name}s is {self.buying_price}"
        else:
            return f"{self.__name}s has neither made a profit nor a lose"

    def profitAfter_transport(self):
        profit=(self.selling_price - self.buying_price) * self.quantity
        profit -= profit * self.transport
        return profit


    # instantiating from a file
    @classmethod  #has relationship with the class(used to instantiate) but nothing to with instances
    def instantiate_from_csv(cls):
        with open('items.csv', "r") as f:
            reader=csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                buying_price=float(item.get('buying_price')),
                selling_price=float(item.get('selling_price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod #has a relationship with the class but nothing to do with instances
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
        
    #used to represend data in format you would like
    def __repr__(self):
        return f"Item('{self.__name}',{self.buying_price},{self.selling_price},{self.quantity})"



# inheritance
class Eraser(Item):
    transport=0.06
    def __init__(self,name,buying_price,selling_price,quantity,expired_erasers):
        #super function used to inherit all atributes and methods
        super().__init__(
            name,
            buying_price,
            selling_price,
            quantity
        )
        assert expired_erasers >=0 ,f"expired_erasers should be greater or equal to zero"
        self.expired_erasers=expired_erasers 

# Encapsulation
    @property #only read but cannot get changed
    def name(self):
        return self.__name
# encapsulation prevents direct access of the attributes
    @name.setter
    def name(self,value):
        if len(value)<5:
            raise Exception("length should be greater than five")
        else:
            self.__name=value

    
    def profitAfter_transport(self):
        profit=(self.selling_price - self.buying_price) * self.quantity
        profit -= profit * self.transport
        return profit

    

    def remaing_erasers(self):
        return self.quantity - self.expired_erasers

#abstraction
#sending emails for products
#use of double underscore is used to make the methods private hence abstracting data to users
def __mail_connector(self):
    pass


def __mail_subject(self):
    pass

def __mail_body(self):
    f"""
    This are the products which are expired erasers= {self.expired_erasers} 
    we will be glad if the expired products will get replaced
    Thank you!
    """

def send_mail(self):
    mail_connector()
    mail_subject()
    mail_body()


#The only method which can be accessed by any user is send_mail()
#For mail_connector(),mail_subject(),mail_body() cannot be accessed since have been abstracted
#You can abstract a method by making it private
#You can make it private by using double underscore as shown above



# instances for Item class
item2=Item("pen",15,20,12)
item3=Item("hardcover",270,270,30)
item4=Item("A5",40,45,3)

# calling calculate_total_price
print(item4.calculate_total_price())
print(item4.calculate_lose_profit())



# instances for Eraser class
eraser1=Eraser("new",20,23,20,4)
eraser1.remaing_erasers()
print(eraser1.remaing_erasers())




#polymorphism
#use of an identity in different objects can be characterized as polymorphism

#good example is len()  function in python

name="Layton"
my_list=['yellow','orange']

print(len(name)) #returns 6
print(len(my_list)) #returns 2


#polymorphism in action in my project
#regardless of sellingprice,buyingprice and quantity being same item1 returns 14.4 and araser2 returns 14.1 but all are using same function to calculate profit after transport
# this is achieved because transport cost is different for the two classes but are using same method
print("********")

item1=Item("A4",70,75,3)
eraser2=Eraser("A4",70,75,3,2)

print(item1.profitAfter_transport())  # returns 14.4
print(eraser2.profitAfter_transport()) # returns 14.1

print("********")


# summary of what i learned

""" 
@classmethods
@staticmethods
Inheritance
Encapsulation
Abstraction
Polymorphism
"""




