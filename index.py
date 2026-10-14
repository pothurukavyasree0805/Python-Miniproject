class User:
      def __init__(self,id,name,password,role):
            self.id = id
            self.name = name
            self.password = password
            self.role = role
      def user_details(self):
            return f"{self.id},{self.name},{self.password},{self.role}\n"

class Auth:
      def register(self):
            id = input("Enter userid: ")
            name = input("Enter username:")
            password = input("Enter password: ")
            role = input("Enter user role: ")
            user = User(id,name,password,role)

            with open("users.txt","r") as file:
                  lines  = file.readlines()

            is_found = False 
            for line in lines:
                  details = line.strip().split(",")
                  if(details[1]==name):
                        is_found = True

            if(is_found):
                  print("User Already Exist")
            else:
                  with open("users.txt","a") as file:
                        file.write(user.user_details())
                  print("Registration Successful!")

      def login(self):
            name = input("Enter the name: ")
            password = input("Enter the password: ")
            with open ("users.txt","r") as file:
                  lines = file.readlines()

            is_found = False
            for line in lines:
                  details = line.strip().split(",")
                  if(details[1]==name):
                        is_found = True 
                        if(details[2]==password):
                              print("Login Successful!")
                              break
                        else:
                              print("Invalid Credentials")
                              break
            if(is_found==False):
                  print("User Not Found. Please Register.")

class Product:
      def __init__(self,id,product_name,price,quantity):
            self.id = id
            self.product_name = product_name
            self.price = price
            self.quantity = quantity
      def product_details(self):
            return f"{self.id},{self.product_name},{self.price}rs,{self.quantity}\n"

class Admin:
      def add_product(self):
            id = input("Enter product id: ")
            product_name = input("Enter product name: ")
            price = input("Enter product price : ")
            quantity = input("Enter product quantity: ")
            product = Product(id,product_name,price,quantity)
            with open("products.txt", "r") as file:
                  lines = file.readlines()

            with open("products.txt", "w") as file:
                  for line in lines:
                        details = line.strip().split(",")
                        if(details[1]==product_name):
                              quantity

            with open("products.txt","a") as file:
                  file.write(product.product_details())
                  print("Product Added Successfully!")








admin = Admin()
admin.add_product())))
      
            



#auth = Auth()
#auth.register()    




