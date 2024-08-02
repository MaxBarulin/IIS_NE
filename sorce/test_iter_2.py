import math
from prettytable import PrettyTable as PT

from example_calculator.table import create_tables_turning_other

x = create_tables_turning_other()
y = list(x[0]["k1"].keys())

list_1 = []
for i in range(len(y)):
    s = x[0]["k1"][y[i]]
    list_1.append(s)

table_1 = PT()
table_1.field_names = ['D', 't', 'L', 10, 20, 50, 100, 200, 300, 400, 500, 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, 8000, "S", "N", "V"]


n_list = [1000, 630, 500, 400, 315, 250, 200, 160, 200, 160, 125, 100, 160, 125, 100, 80, 125, 100, 80, 63, 100, 80, 63, 50, 76 ,63, 50, 38, 63, 38, 32, 27, 38, 32, 27, 24, 32, 24, 19, 16, 24, 19, 16, 13, 19, 16, 13, 10, 16, 13, 10, 8]
d_list = [20, 50, 100, 150, 200, 250, 300, 400, 500, 750, 1000, 1250, 1500, 2000]
v_list = [63, 99, 79, 63, 99, 79, 63, 50, 94, 75, 59, 47, 101, 79, 63, 50, 98, 79, 63, 49, 94, 75, 59, 47, 96, 79, 63, 48, 99, 60, 50, 42, 90, 75, 64, 57, 101, 75, 60, 50, 94, 75, 63, 51, 90, 75, 61, 47, 101, 82, 63, 50]
s_list = [0.26, 0.28, 0.26, 0.23, 0.30, 0.28, 0.26, 0.23, 0.33, 0.30, 0.28, 0.26, 0.36, 0.33, 0.30, 0.28, 0.38, 0.36, 0.33, 0.30, 0.40, 0.38, 0.36, 0.33, 0.46, 0.40, 0.38, 0.36, 0.51, 0.46, 0.40, 0.38, 0.61, 0.51, 0.46, 0.40, 0.66, 0.51, 0.46, 0.40, 0.71, 0.51, 0.46, 0.40, 0.71, 0.51, 0.46, 0.40, 0.71, 0.51, 0.46, 0.40]
or_list = [10, 13, 18, 23]
t_list = [3, 5, 10, 15]
l_list = [10, 20, 50, 100, 200, 300, 400, 500, 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000]
stst = []
ta = []
sub = []



def c_r(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, n, feed_rate_per_revolution, overrun, rapid_traverse_rate):

    total_depth = (initial_diameter - final_diameter) / 2
    number_of_passes = math.ceil(total_depth / depth_of_cut)

    # Общее время обработки
    total_time = 0

    for i in range(number_of_passes):
        current_diameter = initial_diameter - 2 * depth_of_cut * (i + 1)
        # print(current_diameter)

        # Проверка, чтобы диаметр не стал меньше конечного
        if current_diameter < final_diameter:
            current_diameter = final_diameter

        spindle_speed = n

        feed_per_minute = feed_rate_per_revolution * spindle_speed

        total_length = length_of_workpiece + overrun

        pass_time = total_length / feed_per_minute
        total_time += pass_time

        return_time = (length_of_workpiece + overrun) / rapid_traverse_rate
        total_time += return_time
    return total_time


# initial_diameter = 103.0  # начальный диаметр в мм
# final_diameter = 100.0  # конечный диаметр в мм
# depth_of_cut = 1.5  # глубина резания в мм (на сторону)
# length_of_workpiece = 500.0  # длина вала в мм
# #cutting_speed = 101  # скорость резания в м/мин
# feed_rate_per_revolution = 0.30  # подача на один оборот в мм/об
# overrun = 10.0  # перебег резца в мм
# rapid_traverse_rate = 2000.0  # скорость возврата на ускоренной подаче в мм/мин
# n = 315

cont = 0
cont2 = 0
for i in range(len(d_list)):
    cont += 1
    for j in range(len(t_list)):

        stst.clear()
        if d_list[cont-1] == 20 and t_list[j] != 3:
            continue
        elif d_list[cont-1] == 50 and t_list[j] == 15:
            continue
        else:
            # print(d_list[cont-1], end=" ")
            # print(t_list[j], end=" ")
            # print(or_list[j], end=" ")
            # print(v_list[j], end=" ")
            # print(s_list[j], "\n")
            initial_diameter = d_list[cont-1] + t_list[j]  # начальный диаметр в мм
            final_diameter = d_list[cont-1]  # конечный диаметр в мм
            depth_of_cut = t_list[j] / 2  # глубина резания в мм (на сторону)
            n = n_list[cont2]  # скорость резания в м/мин
            feed_rate_per_revolution = s_list[cont2]  # подача на один оборот в мм/об
            overrun = or_list[j]  # перебег резца в мм
            rapid_traverse_rate = 2000.0  # скорость возврата на ускоренной подаче в мм/мин
            #cutting_speed = math.pi * current_diameter * n_list[j]
            #stst.append(d_list[cont-1])
            #stst.append(t_list[j])
            #stst.append(or_list[j])
            for k in range(len(l_list)):
                #print(l_list[k], end="")
                length_of_workpiece = l_list[k]  # длина вала в мм
                time_required = c_r(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, n, feed_rate_per_revolution, overrun, rapid_traverse_rate)# * 1.12
                #print(f"Во:{time_required:.2f}м", end=" ")
                # stst.append(d_list[cont-1])
                # stst.append(t_list[j])
                # stst.append(or_list[j])

                #print(round(time_required, 2))



                stst.append(float(f"{round(time_required, 2)}"))

            sub.append(list(stst))



            #stst.append(feed_rate_per_revolution)
            #stst.append(n_list[cont2])
            #stst.append(v_list[cont2])
            cont2 += 1
            #sub.append(lists_table)
            #table_1.add_row(stst)
            #print(stst)
            #print(stst)
            #print(stst)
            #print(stst)
#print(list_1)
#print(sub)
suu = []
for i in range(len(list_1)):
    #print(list_1[i], len(list_1[i]))
    #print(sub[i], len(sub[i]))
    su = []
    for j in range(len(list_1[i])):
        #print(list_1[i][j])
        #print(sub[i][j])
        x = list_1[i][j] - sub[i][j]
        x2 = round(x, 2)
        su.append(x2)

    suu.append(su)
    # #     print(list_1[i], sub[i])

#print(list_1)
#print(sub)
#print(suu)
for i in range(len(list_1)):
    print(list_1[i])
    print(sub[i])
    print(suu[i])
    print("")









            #print("\n")
#print(sub)
# Пример использования функции
#time_required = calculate_turning_time(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, n, feed_rate_per_revolution, overrun, rapid_traverse_rate) * 1.1
#print(f"Время обработки: {time_required:.2f} минут")
