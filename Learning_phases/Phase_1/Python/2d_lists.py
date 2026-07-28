# a list made up of lists

fruit = ["apples","orange","banana","coconant"]
veges = ["carrots","potatoes","celery"]
meats = ["chicken","fish","turkey"]

groceries = [["apples","orange","banana","coconant"],
             ["carrots","potatoes","celery"],
             ["chicken","fish","turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end= " ")
    print()
