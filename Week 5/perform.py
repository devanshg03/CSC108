def repeat_string(x):
    x += x
    
def repeat_list(x):
    x.extend(x)
    
position = ["first", "second", "third", "fourth"]
double_position = position
repeat_list(double_position)

count = "123456789"
double_count = count
repeat_string(double_count)

print(position)
print(double_position)
print(count)
print(double_count)