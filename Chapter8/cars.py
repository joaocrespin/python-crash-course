def build_veichle(manufacturer, model, **kwargs):    
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car = build_veichle('subaru', 'outback', color='blue', tow_package=True)
print(car)