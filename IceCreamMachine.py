class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
    def scoops(self):
    	combination = []
    	for ingredient in self.ingredients:
    		for topping in self.toppings:
    			combination.append([ingredient,topping])
    	return combination

machine = IceCreamMachine(["vanilla","chocolate"], ["chocolate sauce"])
print(machine.scoops())
machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce","orange"])
print(machine.scoops())
# this should print
#[['vanilla', 'chocolate sauce'], ['chocolate','chocolate sauce'], ['vanilla','orange'], ['chocolate','orange']]
machine = IceCreamMachine([],[])
print(machine.scoops())
