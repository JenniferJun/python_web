# 👇🏻 YOUR CODE 👇🏻:

DISCOUNT_RATE_HIGH = 0.25
DISCOUNT_RATE_LOW = 0.15
MONTH_COUNT = 12
TAX_TURNPOINT = 100_000

def get_yearly_revenue(monthly_revenue):
    return monthly_revenue*MONTH_COUNT

def get_yearly_expenses(monthly_expenses ):
    return monthly_expenses*MONTH_COUNT

def get_tax_amount(profie_amt):
    if  profie_amt > TAX_TURNPOINT:
        tax_rate = profie_amt * DISCOUNT_RATE_HIGH
    else:
        tax_rate = profie_amt * DISCOUNT_RATE_LOW
    tax_amount = profie_amt * tax_rate
    return tax_amount

def apply_tax_credits(tax_amount, tax_credits):
  return tax_amount * tax_credits

def format_currency(amount,currency_symbol):
   return f"{currency_symbol}{amount:,}"
        
# BLUEPRINT | DONT EDIT

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

profit = yearly_revenue - yearly_expenses

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print("=============================")
print("monthly revenue :",format_currency(monthly_revenue,"₩"))
print("monthly expenses :",format_currency(monthly_expenses,"₩"))
print("tax credits :", tax_credits)
print("final tax amount : ",format_currency(final_tax_amount,"₩"))