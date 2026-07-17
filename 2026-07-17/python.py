# pehle hum 
# input lenge  usme varibales bnakr unmain food unki prices add kreinge 
# sab to pehle apa laina wa budget k apna kina wa taake aapa apne expenses track down kar sakiye
# dosra apa apne expenses daine a jere regularly hunde a k kis kis cheez ch

# arithmetic function creation
#     isme aisa hoga k  wo sb values ko add karega aur total calculate karega 
#     phir wo TOTAL ko print karega aur agar wo budget se zyada ho gaya to wo warning dega k apka budget exceed ho gaya hai

#     total expenses ko calculate krka total bugget ma sa minus krka then estimate kran ga ka kitna khrcha hova ha

def calculate_total_expenses(food_expense,transport_expense):
    total_expense = food_expense+transport_expense
    return total_expense

def get_input_give_output():
    # this part takes input.
    budget = float(input("Apna budget daalein: "))
    food_expense = float(input("Food ka kharcha daalein: "))
    transport_expense = float(input("Transport ka kharcha daalein: "))

    # this part calculates the total expenses.

    total_expense = calculate_total_expenses(food_expense,transport_expense)

    # this part gives the output.
    print(f'Your total expense is this:{total_expense}')

get_input_give_output()