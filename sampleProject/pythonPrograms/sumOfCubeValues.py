def get_cube_value(x):
    return (x**3)
def get_sum_cube_value(list_a):
    sqrd_sum=0
    for i in list_a:
        sqrd_sum+=get_cube_value(i)
    return sqrd_sum
list_a=list(map(int,input().split()))
result=get_sum_cube_value(list_a)
print(result)