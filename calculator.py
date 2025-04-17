def f_calculator(f_num, s_num, cal):
    if cal == '+':
        return f_num + s_num
    elif cal == '-':
        return f_num - s_num
    elif cal == '*':
        return f_num * s_num
    elif cal == '/':
        if s_num == 0:
            print("오류: 0으로 나눌 수 없습니다.")
            return None
        return f_num / s_num
    else:
        print("오류: 유효하지 않은 연산자입니다.")
        return None
 
is_running = True
while is_running:
    first_number = int(input("Choose a number:"))
    second_number = int(input("Choose another one:"))
    operation_char = input("Choose an operation:\n Options are:+, -, * or /. \n Writer 'exit' to finish.\n")
    if operation_char == 'exit':
        is_running = False
        print("프로그램을 종료합니다.")
    else:
        print(f"{first_number} {operation_char} {second_number} =", f_calculator(first_number,second_number,operation_char))
 