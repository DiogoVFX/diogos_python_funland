# A Script that will randomly select a number of dishes for you to cook saving the need of choosing yourself.

# Imports
import random

print("Hi and welcome to the random dish selector.\nPlease choose the number of each dish you want.")
pasta =   int(input("Pasta:"))
rice =    int(input("Rice:"))
potato =  int(input("Potato:"))
takeout = int(input('"Take Out":'))
misc =    int(input("Misc:"))

dish_numbers = {"Pasta":pasta, "Rice":rice, "Potato":potato, "Takeout":takeout, "Misc":misc}

pasta_dict =   {"Lamb Linguine":20, "Spiced Pork Ragu":20, "Veggie Ragu Pasta Bake":45, "Cajun Chorizo Chicken Thigh Tomato Pasta":25, "Bacon Linguine Amatriciana":45,
                "Spicy Pork and Spinach Ragu":20, "Speedy Creamy Chorizo Sweetcorn Pasta":20, "Pork and Oregano Sausage Linguine":30, "Rigatoni Caprese":30, 
                "Serrano Ham and Butternut Linguine":35, "Creamy Caramelised Onion Linguine":20, "Creamy Green Veg and Pesto Pasta":20, "Penne Ragu Alforno":45,
                "Beef Ragu":20, "Creamy Chorizo Sweetcorn Rigatoni":20, "Ratatouille Pasta Bake":40, "Porky Pappardelle":20, "Bacon Rigatoni":35, "Cauliflower Mac and Blue Cheese": 35,
                "Bacon Penne all'Arrabbiata":30, "Sausage Meatball Spaghetti":35}

rice_dict =    {"Indonesian Style Coconut Chicken Curry":30, "Teriyaki Sesame Chicken":20, "Aromatic Beef Pilaf":20, "Thai Style Pork Rice Bowl": 35,
                "Chicken Spinach Curry":20, "Coronation Chicken Curry":25, "Miso Honeyed Smoked Tofu":25, "Teriyaki Beef Mince":35, "Chicken Fried Rice": 20,
                "Chiken and Mushroom Rogan Josh":30, "Sweet and Sour Style Chicken":25, "Caramelised Onion Sausages with Baked Rice":35, "Coconut Caribbean Style Kidney Bean Stew":35,
                "Beef Rogan Josh Style Curry":30, "Soy Baked Chicken Thighs":20}

potato_dict =  {"Thyme Roast Chicken":40, "BBQ Sausage Skewers":45, "Mexican Style Beef Loaded Wedges With Guac":40, "Mexican Style Beef Loaded Wedges":45,
                "Halloumi and Red Onion Skewers":40, "Caramelised Onion Sausage Traybake":45, "Chicken Enchiladas and Wedges":45, "Roasted Chicken and Chilly Chive Sauce":20,
                "Cheese and Caramelised Onion Chicken":40, "Honey Mustard Sausages with Mash":35, "Pan Fried Hake":40, "Cheesy Crusty Sea Bass":40, "Chipotle Spiced Chicken":45}

takeout_dict = {"Chicken Tika Pizza":35, "BBQ Sausage Cheeseburger":30, "Herby Burgers":40, "BBQ Glazed Sausages":35, "Beef Burger with Truffel Wedges":40, 
                "Smoked Sausage in Buns":30, "Double Cheese Bsked BBQ Burgers":40, "Chipotle Pork Tacos":30, "Cheesy Chipotle Bean Quesadillas":20, "Fried Bean and Mushroom Tacos":20,
                "Korean Style Beef Tacos":20}

misc_dict =    {"Sticky Bulgogi Pork Noodles":20, "Hoisin Prawn Noodle Stir-Fry":20,"Peri Peri Pork Black Bean Stew":20, "Curried Paneer Dal Pie":45, "Lebanese Style Lab and Bulgar":35,
                "Chermoula Chicken":20, "Spicy Cajun Prawn Risotto":40, "Bacon Butternut Squash Risotto":40, "Super Cheesy Oven-Baked Tomato Risotto":45, 
                "Oven-Baked Bacon and Mushroom Risotto":45, "Prawn and Tomato Risotto":35}

dishes_chosen = []

for dish_type in dish_numbers:
    for dish in range(0,dish_numbers[dish_type]):
        if dish_type == "Pasta":
            dishes_chosen.append(list(pasta_dict.items())[random.randint(0,len(pasta_dict)-1)])
        elif dish_type == "Rice":
            dishes_chosen.append(list(rice_dict.items())[random.randint(0,len(rice_dict)-1)])
        elif dish_type == "Potato":
            dishes_chosen.append(list(potato_dict.items())[random.randint(0,len(potato_dict)-1)])
        elif dish_type == "Takeout":
            dishes_chosen.append(list(takeout_dict.items())[random.randint(0,len(takeout_dict)-1)])
        elif dish_type == "Misc":
            dishes_chosen.append(list(misc_dict.items())[random.randint(0,len(misc_dict)-1)])

print('#########')
for i in dishes_chosen:
    print('\n'+i[0]+':',str(i[1])+'mins')