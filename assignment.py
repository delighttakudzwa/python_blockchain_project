#create two variable - one with your name one with age

my_name = input ('Please enter your name: ')
#my_age = input (int('Please enter your age: '))???
my_age = input ('Please enter your age: ')

#create a function which prints your data as one string
def name_age():
    print(my_name + my_age)

name_age()

#create a function which prints ANY data (two arguments) as one string
def any_data(switch1, switch2):
    print(switch1 + ' - ' + switch2)

any_data(my_name, my_age)
#create a function which calculates and returns the number of decades you already lived (e.g 23 = 2 decades)

def cal_decades(age):
    decades_lived = age // 10
    return decades_lived

decades = cal_decades(int(my_age))
print(decades)

