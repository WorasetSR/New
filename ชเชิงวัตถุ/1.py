class Customer :
    name = ''
    surname = ''
    age = 0
    def addUser(self):
        print('Adding user',self.name, self.surname, self.age)

customer1 = Customer()
customer1.name = 'poom'
customer1.surname = 'john'
customer1.age = 20
customer1.addUser()

customer2 = Customer()
customer2.name = 'joey'
customer2.surname = 'jim'
customer2.age = 21
customer2.addUser()

customer3 = Customer()
customer3.name = 'joey'
customer3.surname = 'jim'
customer3.age = 21
customer3.addUser()

customer4 = Customer()
customer4.name = 'joey'
customer4.surname = 'jim'
customer4.age = 21
customer4.addUser()


