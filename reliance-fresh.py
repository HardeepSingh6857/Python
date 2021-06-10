def reliance_fresh():
    l = ['grapes','carrots','apples','watermelon','kiwi']
    print(f'Welcome to Reliance Fresh \nToday we have {l} available')
    uinp = input("please enter the item you want to purchase: ").lower()
    l.remove(uinp)
    print(f"{l}\nThank you for your purchase!")
    
reliance_fresh()
