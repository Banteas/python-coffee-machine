# Python Coffee Machine ☕  

A beginner-friendly Python program that simulates a coffee vending machine. Users can choose drinks, insert coins, get change, and view a report of resources. The program handles insufficient resources, invalid inputs, and tracks the machine’s money.  

## Features
- Choose a drink: espresso, latte, cappuccino  
- Print a report of current resources (water, milk, coffee, money)  
- Check if resources are sufficient for the selected drink  
- Process coins: quarters, dimes, nickels, pennies  
- Handle insufficient money and give change  
- Deduct ingredients from resources after a successful purchase  
- Turn off the machine with `"off"`  
- Handle invalid inputs gracefully  

## How to Run
1. Clone the repository or download the files.  
2. Run the script with Python 3:
   ```bash
   python main.py
   ```
3. Follow the on-screen prompts to order drinks, insert coins, and check the machine status.

**Learning Goals**

- Working with nested dictionaries for menu items and ingredients
- Using functions to structure the program
- Handling user input errors with try/except
- Practicing loops, conditionals, and basic arithmetic
- Updating and tracking program state with dictionaries

**Example Usage**
```
What would you like? (espresso/latte/cappuccino): latte
Your latte costs $2.5
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change
Here is your latte ☕ Enjoy!
```