def make_sandwich(*args):
    '''Makes a sandwich, the ingredients are "*args"'''
    print("\nWe'll start with the bread!")
    for ingredient in args:
        print(f"Adding {ingredient} to your sandwich.")

make_sandwich('cheese')
make_sandwich('chicken', 'tomato', 'carrots')
make_sandwich('airplane', 'steak', 'charcoal', 'banana', 'bee', 'pool')