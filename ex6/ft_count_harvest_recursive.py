
def ft_count_harvest_recursive():
    number = int(input('Days until harvest: '))

    def ft_recursive(day: int):
        if day > number:
            print('Harvest time!')
            return
        print(f'Day {day}')
        ft_recursive(day + 1)
    ft_recursive(1)
