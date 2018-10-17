# file_reader_with_plan_for.py
try:
    with open('plan.txt', 'r') as file:
        for line in file:
            print(line)
            print(len(line.strip()))
except Exception as e:
    print(e)
    

