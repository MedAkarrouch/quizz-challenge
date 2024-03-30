import random
operators = ["+","-","*"]
max_operand = 12
min_operand = 3
total_problems = 10

def generate_problem():
  left = random.randint(min_operand, max_operand)
  right = random.randint(min_operand, max_operand)
  operator = random.choice(operators)
  exp = f"{left} {operator} {right}"
  answer = eval(exp)
  return exp,answer

print("Quiz started : ")
print("--------------------------------")
for problem in range(total_problems):
  exp,answer = generate_problem()
  while True:
    val = input(f"Problem #{problem+1} : {exp} = ")
    if(val== str(answer)):
      break
print("Quiz ended")
print("--------------------------------")