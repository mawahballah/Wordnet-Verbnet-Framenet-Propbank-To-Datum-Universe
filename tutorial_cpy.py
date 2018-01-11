from cpyDatumTron import atum, datum, katum, Of, Intersect, Union 

import datetime

###############################
# Tutorial 1

# 1. setup

thing = datum.setup(atum())

# 2.1 adding data: new katums

color = thing.Get('color')
taste = thing.Get('taste')
food = thing.Get('food')
fruit = food.Get('fruit')
apple = fruit.Get('apple')
mango = fruit.Get('mango')
red = color.Get('red')
sweet = taste.Get('sweet')

# apple is red
apple._is(red)
# apple can have one color which is red
apple.set(color, red)
assert apple.Is(red)

# apple is not red anymore
apple.isnot(red)
assert not apple.Is(red)
# back to apple is red
apple.set(red)

# 3. query

red1 = color.find("red")
assert red1 == red

red2 = color.find("red")
assert red2 == red
blue = color.find("blue")
assert blue is None

assert red.Is(color)
assert red.Isa(color)

assert Of(color, apple) == red

# 4. inheritence

fujiApple = apple.Get("fujiApple")
assert Of(color, fujiApple) == red # inherited from apple

darkRed = red.Get("darkRed")
apple.set(darkRed)

assert Of(color, fujiApple) == darkRed
assert Of(color, fujiApple).Is(red)
assert Of(red, fujiApple) == darkRed

# 5. Time

pricePrePound = thing.Get("pricePrePound")
fujiApple.set(pricePrePound.Get(1.5))

fujiApple.now(pricePrePound.Get(1.3))
fujiApple.now(pricePrePound.Get(1))

assert Of(pricePrePound, fujiApple).asDouble == 1
assert Of(pricePrePound, fujiApple.at(0)).asDouble == 1.5
assert Of(pricePrePound, fujiApple.at(1)).asDouble == 1.3
assert fujiApple.countI == 2

# 6. Code

def AvgFunc(k, attr):
    return 1.0*sum([Of(attr, i).asDouble for i in k.I])/k.countI


banana = fruit.Get('banana')
weight = thing.Get('weight')

apple.set(weight.Get(1.0))
mango.set(color.Get('green'), weight.Get(0.9))
banana.set(color.Get('yellow'), weight.Get(1.1))

fruit.set(weight.Get(AvgFunc)) # <---
assert Of(weight, fruit) == 1 # average of 1, .9, 1.1 


############################
# Tutorial 2

# 7 Query

# 7.1 Setup for Northwind

katum.load('northwind.datum', atum())
northwindDB = datum.thing
assert northwindDB is not None

Table = northwindDB.find("Table")
assert Table is not None

Column = northwindDB.find("Column")
assert Column is not None

Employee = Table.find("Employee")
assert Employee is not None
Order = Table.find("Order")
assert Order is not None
Customer = Table.find("Customer")
assert Customer is not None

EmployeeCols = Column.find("Employee")
assert EmployeeCols is not None
OrderCols = Column.find("Order")
assert OrderCols is not None
CustomerCols = Column.find("Customer")
assert CustomerCols is not None
ShipperCols = Column.find("Shipper")
assert ShipperCols is not None

# 7.2 Iterate over all employees

print 'All employees'
for employee in Employee.I:
    print employee
    
# 7.3 Iterate over USA employees

USAEmployees = EmployeeCols.find("Country").find("USA") # O(1)
print 'USA employees'
for employee in USAEmployees.I:
    print employee

OrderDetailTable = Table.find("Order Detail")
OrderDetailCols = Column.find("Order Detail")

OrderDetailPriceCol = OrderDetailCols.find("UnitPrice")
OrderDetailQtyCol = OrderDetailCols.find("Quantity")
OrderDetailDiscountCol = OrderDetailCols.find("Discount")

OrderDetailTotalPrice = OrderDetailCols.Get("totalPrice")

_orderDetailPriceCol = None
_orderDetailQtyCol = None
_orderDetailDiscountCol = None

def Initialize():
    global _orderDetailPriceCol, _orderDetailQtyCol, _orderDetailDiscountCol
    Cols = katum.thing.find("Column")
    assert Cols is not None
    
    OrderDetailCols = katum.thing.find("Column").find("Order Detail")
    assert OrderDetailCols is not None

    _orderDetailPriceCol = OrderDetailCols.find("UnitPrice")
    assert _orderDetailPriceCol is not None
    _orderDetailQtyCol = OrderDetailCols.find("Quantity")
    assert _orderDetailQtyCol is not None
    _orderDetailDiscountCol = OrderDetailCols.find("Discount")
    assert _orderDetailDiscountCol is not None

def TotalPriceFunc(orderDetail, totalPrice):
    global _orderDetailPriceCol, _orderDetailQtyCol, _orderDetailDiscountCol
    if orderDetail is None or totalPrice is None:
        return None
    if _orderDetailDiscountCol is None:
        Initialize()
    if _orderDetailDiscountCol is None:
        return None
    discount = (Of(OrderDetailDiscountCol, orderDetail)).asDouble
    return (Of(_orderDetailPriceCol, orderDetail).asDouble * Of(_orderDetailQtyCol, orderDetail).asDouble) * (1-discount) 

OrderDetailTable.set(OrderDetailTotalPrice.Get(TotalPriceFunc))

for orderDetail in OrderDetailTable.I:
    price    = Of(OrderDetailPriceCol, orderDetail).asDouble
    qty      = Of(OrderDetailQtyCol, orderDetail).asDouble
    discount = Of(OrderDetailDiscountCol, orderDetail).asDouble
    totalPrice  = Of(OrderDetailTotalPrice, orderDetail)

    print "{0} ( price {1} * qty {2} ) - discount {3} \t= totalPrice {4}".format(orderDetail, price, qty, discount, totalPrice)

# 7.5 List employees older than 50 years old

EmployeeBD = EmployeeCols.find("BirthDate")
for employee in [e for e in Employee.I if Of(EmployeeBD, e) != None and datetime.datetime.strptime(str(Of(EmployeeBD, e)).split('|')[1].split(')')[0], "%m/%d/%Y %I:%M:%S %p") < datetime.datetime.today() + datetime.timedelta(days=(-60*365.25))]:
    print employee
    
# 7.6 List the order number and employee's last name ...

# List the order number and employee's last name that 
# have placed orders to be delivered in Belgium.

EmployeeLastNameCol = EmployeeCols.find("LastName")
BelgiumOrders = OrderCols.find("ShipCountry").find("Belgium") # O(1)

for order in BelgiumOrders.I:
    print order, 'by', Of(EmployeeLastNameCol, Of(Employee, order))
    
# 7.7 Give the order id, employee id ...
# Give the order id, employee id and the customer id for 
# orders that are sent by the company 'Speedy Express' to customers 
# who live in Buenos Aires.

SpeedyExpressShipper = ShipperCols.find("CompanyName").find("Speedy Express") # O(1)
BuenosAiresCustomers = CustomerCols.find("City").find("Buenos Aires") # O(1)

O1 = Order.And(SpeedyExpressShipper.I) # orders sent by Speedy Express
O2 = Order.And(BuenosAiresCustomers.I) # orders bought by Brussels customers

for order in Intersect(O1, O2):  
    print order, Of(Employee, order), Of(Customer, order)
    
# 7.8 List products that were bought or sold by people who live in London.

Category    = Table.find("Category")
Product     = Table.find("Product")
OrderDetail = Table.find("Order Detail")

customerCityLondon = Column.find("Customer").find("City").find("London")
employeeCityLondon = Column.find("Employee").find("City").find("London")

OD1 = OrderDetail.And(Order.And(Customer.And(customerCityLondon)))
OD2 = OrderDetail.And(Order.And(Employee.And(employeeCityLondon)))

for orderDetail in Union(OD1,OD2):
    print Of(Product, orderDetail)

# 8 Finding Patterns
    
print '\n--- Patterns: Any pattern in customer City and orderd product Category?\n'

minSupport = 10 # minimum 10 orders 
minConfidence = 20 # minimum 20% probability

def FreqDict(items):
    freqDict = {}
    total = 0
    for item in items:
        if item in freqDict:
            freqDict[item] += 1
        else:
            freqDict[item] = 1
        total += 1
    return freqDict, total

def VPatterns1(condition, ifPath, thenPath):
    eset = ifPath[0].And(condition)
    for i in range(1, len(ifPath)):
        eset = ifPath[i].And(eset)
    
    elist = Of(thenPath[0], eset, None, False)
    for i in range(1, len(thenPath)):
        elist = Of(thenPath[i], elist, None, False)
    
    return elist

def VPatterns(conditions, ifPath, thenPath, minSupport, minProbability):
    for condition in conditions.I0:
        patterns = VPatterns1(condition, ifPath, thenPath)
        freqDict, total = FreqDict(patterns)
        for item in freqDict.keys():
            support = freqDict[item]
            probability = (support * 100.0) / total
            
            if support >= minSupport and probability > minProbability:
                yield condition, item, support, probability
                
def PrintPattern(condition, conclustion, freqDict, total, minSupport, minConfidence):
    for item in freqDict.keys():
        support = freqDict[item]
        confidence = (support*100)/total
        
        if support >= minSupport and confidence > minConfidence:
            print condition, confidence, '%', Of(conclustion, item), '-- support =', support
            
# Customer City and Product Category 
categoryName = Column.find("Category").find("CategoryName")

for city in Column.find("Customer").find("City").I:
    categories = Of(Category, Of(Product, OrderDetail.And(Order.And(Customer.And(city))), None, False), None, False)
    
    categorie2 = VPatterns1(city, [Customer, Order, OrderDetail], [Product, Category])
    dbgCat1 = list(categories)
    dbgCat2 = list(categorie2)
    assert len(dbgCat1) == len(dbgCat2)
    
    freqDict, total = FreqDict(categories)
    PrintPattern(city, categoryName, freqDict, total, minSupport, minConfidence)
    
    dbg0 = list(Customer.And(city))
    dbg1 = list(Order.And(Customer.And(city)))
    dbg2 = list(OrderDetail.And(Order.And(Customer.And(city))))
    dbg3 = list(Of(Product, OrderDetail.And(Order.And(Customer.And(city))), None, False))
    assert len(dbg2) == len(dbg3)

    dbg4 = list(categories)
    assert len(dbg2) == len(dbg4)
    assert len(dbg2) == total

# Employee and Product Category
print "\n--- Patterns: Any patterns in Employee selling product Category?\n"

for employee in Table.find("Employee").I0:
    categories = Of(Category, Of(Product, OrderDetail.And(Order.And(employee)), None, False), None, False)
    freqDict, total = FreqDict(categories)
    
    dbg1 = list(Order.And(employee))
    dbg2 = list(OrderDetail.And(Order.And(employee)))
    dbg3 = list(Of(Product, OrderDetail.And(Order.And(employee)), None, False))
    assert len(dbg2) == len(dbg3)
    
    dbg4 = list(categories)
    assert len(dbg2) == len(dbg4)
    assert len(dbg2) == total
    
    PrintPattern(employee, categoryName, freqDict, total, minSupport, minConfidence)

# Employee and Product Category

for employee in Table.find("Employee").I0:
    categories = VPatterns1(employee, [Order, OrderDetail], [Product, Category])
    freqDict, total = FreqDict(categories)
    PrintPattern(employee, categoryName, freqDict, total, minSupport, minConfidence)

print '\nEnd Patters\n'

patterns1 = VPatterns(Column.find("Customer").find("City"), [Customer, Order, OrderDetail], [Product, Category], 10, 20)

for pattern in patterns1:
    print pattern[0], '-->', pattern[1], 'support =', pattern[2], 'probability =', pattern[3], '%'

dbgArr1 = list(VPatterns(Column.find("Customer").find("City"), [Customer, Order, OrderDetail], [Product, Category], 10, 20))
    
dbgArr2 = list(VPatterns(Table.find("Employee"), [Order, OrderDetail], [Product, Category], 10, 20))
