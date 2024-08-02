from example_calculator.table import create_tables_turning_other

x = create_tables_turning_other()
y = list(x[0]["k1"].keys())

list_1 = []
for i in range(len(y)):
    s = x[0]["k1"][y[i]]
    list_1.append(s)

print(list_1)
