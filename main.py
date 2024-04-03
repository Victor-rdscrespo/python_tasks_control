def add_task(schedule, task, day):
    if day in schedule:
        schedule[day].append(task)
    else:
        schedule[day] = [task]

def show_schedule(schedule):
    for key, value in schedule.items():
        #print(f'{key.capitalize()}: ' ', '.join(value))
        print(f'{key.capitalize()}: {", ".join(value)}')

schedule = {}

while True:


    print("1. Adicionar tarefa: ")
    print("2. Exibir tarefa")

    choice = input("Escolha uma opção: ")

    if choice == '1':
        day = input("Digite o dia da semana: ")
        task = input("Digite a tarefa deste dia ")
        add_task(schedule, task, day)
    elif choice == '2':
        show_schedule(schedule)
        break        
    
