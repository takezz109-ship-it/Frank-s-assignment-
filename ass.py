sandwich_oders = ['tuna', 'chicken', 'veggie', 'beef']
finished_sandwiches = []
while sandwich_oders:
    sandwich = sandwich_oders.pop() 
    print(f"i made your {sandwich} sandwich.")
finished_sandwiches.append(sandwich)     
print(f"\n {finished_sandwiches}")
for sandwich in finished_sandwiches:
    print(sandwich)



sandwich_oders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []
print("sorry the deli has run out of pastrami sandwich.") 

while 'pastrami' in sandwich_oders:
    sandwich_oders.remove('pastrami')
while sandwich_oders:
    sandwich =  sandwich_oders.pop()
    finished_sandwiches.append(sandwich) 

for sandwich in finished_sandwiches:
    print(sandwich)
                          