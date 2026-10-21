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
                              return [details[0],details[-1]]
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
            return f"{self.id},{self.product_name},{self.price},{self.quantity}\n"

class Admin:

      def add_product(self):
            id = input("Enter product id: ")
            product_name = input("Enter product name: ")
            price = input("Enter product price : ")
            quantity = int(input("Enter product quantity: "))
            product = Product(id,product_name,price,quantity)
            with open("products.txt", "r") as file:
                  lines = file.readlines()

            with open("products.txt", "w") as file:
                  is_found=False
                  for line in lines:
                        details = line.strip().split(",")
                        if(details[1]==product_name):
                              is_found=True
                              quantity=int(details[3])+(quantity)
                              file.write(f"{details[0]},{details[1]},{details[2]},{quantity}\n")
                        else:
                              file.write(line)

            if(is_found==False):
                  with open("products.txt","a") as file:
                        file.write(product.product_details())
                        print("Product Added Successfully!")

      def update_product(self):
            id = input("Enter id for the product update:")
            with open("products.txt","r") as file:
                  lines = file.readlines()

            with open("products.txt","w") as file:
                  is_found = False
                  for line in lines:
                        details =line.strip().split(",")
                        if(details[0]==id):
                              is_found = True
                              product_name = input(f"change {details[1]} to:")
                              price = input(f"change {details[2]} to:")
                              quantity =input(f"change {details[3]} to:")
                              file.write(f"{id},{product_name},{price},{quantity}\n")
                        else:
                              file.write(line)
                  if is_found==True:
                        print("Product updated successfully!")
                  else:
                        print("Product not found!")

      def delete_product(self):
            id = input("Enter id for the product delete:")
            with open("products.txt","r") as file:
                  lines = file.readlines()

            with open("products.txt","w") as file:
                  is_found = False
                  for line in lines:
                        details = line.strip().split(",")
                        if(details[0]!=id):
                              file.write(line)
                        else:
                              is_found = True
                  if(is_found==True):
                        print("Product deleted succesfully!")
                  else:
                        print("Product not found!")

      def view_product(self):
            with open("products.txt", "r") as file:
                  lines = file.readlines()
            print("----------------------------------------")
            print("|id   |name      |price     |quantity  |")
            print("----------------------------------------")
            for line in lines:
                  details = line.strip().split(",")
                  print(f"|{details[0]+" "*(5-(len(details[0])))}|{details[1]+" "*(10-len(details[1]))}|{details[2]+" "*(10-len(details[2]))}|{details[3]+" "*(10-len(details[3]))}|")
            print("----------------------------------------")

class Cart(Admin):
      def __init__(self,userid):
            self.userid=userid
      def add_product_to_the_cart(self):
            product_name = input("Enter the product name: ")
            with open("products.txt","r") as file:
                  lines = file.readlines()

            is_found = False
            new_product = []
            with open("products.txt","w") as file:
                  for line in lines:
                        details =line.strip().split(",")
                        if(details[1]==product_name and int(details[-1])>0):
                              is_found = True
                              new_product = details
                              quantity = int(details[-1])-1
                              file.write(f"{details[0]},{details[1]},{details[2]},{quantity}\n")
                        else:
                              file.write(line)
            if(is_found):
                  new_product[-1]="1"
                  new_product.insert(0,self.userid)
                  with open("cart.txt","r") as file:
                         lines = file.readlines()

                  with open("cart.txt","w") as file:
                        is_found = False
                        for line in lines:
                              details =line.strip().split(",")
                              if(details[2]==product_name and self.userid==details[0]):
                                    is_found = True
                                    quantity = int(details[-1])+1
                                    file.write(f"{details[0]},{details[1]},{details[2]},{details[3]},{quantity}\n")
                              else:
                                    file.write(line)
                        if(is_found==False):
                              file.write(",".join(new_product)+"\n")

            else:
                  print("Out of stock!")

      def decrease_quantity(self):
            product_name = input("Enter the product name: ")

            with open ("cart.txt","r") as file:
                  lines = file.readlines()

            with open ("cart.txt","w") as file:
                  is_found_= False
                  for line in lines:
                        details = line.strip().split(",")
                        if (details[2]==product_name and self.userid==details[0]):
                              is_found = True
                              quantity = int(details[-1])-1
                              if(quantity>0):
                                    file.write(f"{details[0]},{details[1]},{details[2]},{details[3]},{quantity}\n")
                        else:
                              file.write(line)
                  if(is_found==False):
                        print("Product not found in the cart!")
                  else:
                        with open("products.txt","r") as file:
                              lines =file.readlines()

                        with open("products.txt","w") as file:
                              for line in lines:
                                    details=line.strip().split(",")
                                    if(details[1]==product_name):
                                          quantity = int(details[-1])+1
                                          file.write(f"{details[0]},{details[1]},{details[2]},{quantity}\n")
                                    else:
                                          file.write(line)   

      def view_cart(self):
            with open("cart.txt","r") as file:
                  lines = file.readlines()
            
            my_cart =[]
            for line in lines:
                  details=line.strip().split(",")
                  if(self.userid==details[0]):
                        my_cart.append(details)
                        
            if(len(my_cart)==0):
                  print("Your cart is empty!")
            else:
                  print("----------------------------------")
                  print("|name      |price     |quantity  ")
                  print("----------------------------------")
                  for details in my_cart:
                        print(f"|{details[2]+(" "*(10-len(details[2])))}|{details[3]+(" "*(10-len(details[3])))}|{details[4]+(" "*(10-len(details[4])))}|")
                  print("----------------------------------")

def admin():
      while True:
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. View Product")
            print("5. Logout")
            admin = Admin()
            option = input("Choose one option: ")
            if(option=="1"):
                  admin.add_product()
            elif(option=="2"):
                  admin.update_product()
            elif(option=="3"):
                 admin.delete_product()
            elif(option=="4"):
                  admin.view_product() 
            elif(option=="5"):
                  break
            else:
                  print("Choose valid option.")

def user(user_id):
      while True:
            print("1. Add product to the cart")
            print("2. Decrease quantity")
            print("3. View cart")
            print("4. View product")
            print("5. Logout")
            cart = Cart(user_id)
            option = input("Choose one option: ")
            if(option=="1"):
                  cart.add_product_to_the_cart()
            elif(option=="2"):
                  cart.decrease_quantity()
            elif(option=="3"):
                  cart.view_cart()
            elif(option=="4"):
                  cart.view_product() 
            elif(option=="5"):
                  break
            else:
                  print("Choose valid option.")

def run():
      while True:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            option = input("Choose one option: ")
            auth = Auth()
            if(option=="1"):
                  auth.register()
            elif(option=="2"):
                  res=auth.login()
                  if(res is not None):
                        if(res[1]=="admin"):
                              admin()
                        else:
                              user(res[0])
            elif(option=="3"):
                  print("Thanks for visiting")
                  break
            else:
                  print("Choose the correct option")


      
run()
# auth = Auth()
#auth.register() 
# admin = Admin()
# admin.add_product() 
# admin.update_product()  
# admin.delete_product()
# admin.view_product()
# cart = Cart()
# cart.view_products()
# userid = auth.login()
# cart = Cart(userid)
# cart.add_product_to_the_cart()
# cart.decrease_quantity()
# cart.view_cart()




