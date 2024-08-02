import math
from prettytable import PrettyTable as PT

table_1 = PT()
table_1.field_names = ['D', 't', 'L', 10, 20, 50, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, "S", "N", "V"]


n_list = [500, 315, 250, 250, 2200, 160, 125, 100, 125, 100, 80, 100, 80, 63, 90, 76, 63, 76, 63, 50, 63, 38, 32, 38, 32, 32, 27, 30, 24, 19, 24, 19, 16, 19, 16, 13, 15, 13, 10]
d_list = [50, 100, 150, 200, 250, 300, 400, 500, 750, 1000, 1250, 1500, 2000]
v_list = [79, 79, 63, 79, 63, 75, 59, 47, 79, 63, 50, 79, 63, 49, 85, 72, 59, 96, 79, 63, 99, 60, 50, 90, 75, 75, 64, 94, 75, 60, 94, 75, 63, 90, 75, 61, 94, 82, 63]
s_list = [0.20, 0.22, 0.18, 0.25, 0.21, 0.26, 0.22, 0.18, 0.26, 0.22, 0.18, 0.28, 0.25, 0.2, 0.28, 0.25, 0.2, 0.3, 0.28, 0.22, 0.35, 0.3, 0.25, 0.38, 0.35, 0.35, 0.3, 0.4, 0.3, 0.32, 0.43, 0.4, 0.35, 0.5, 0.43, 0.35, 0.5, 0.43, 0.35]
or_list = [10, 13, 18]
t_list = [3, 5, 10]
l_list = [10, 20, 50, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000]
stst = []
ta = []



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
        if d_list[cont-1] == 50 and t_list[j] != 3:
            continue
        elif d_list[cont-1] == 80 and t_list[j] == 10:
            continue
        elif d_list[cont - 1] == 100 and t_list[j] == 10:
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
            stst.append(d_list[cont-1])
            stst.append(t_list[j])
            stst.append(or_list[j])
            for k in range(len(l_list)):
                #print(l_list[k], end="")
                length_of_workpiece = l_list[k]  # длина вала в мм
                time_required = c_r(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, n, feed_rate_per_revolution, overrun, rapid_traverse_rate) * 1.1
                #print(f"Во:{time_required:.2f}м", end=" ")
                # stst.append(d_list[cont-1])
                # stst.append(t_list[j])
                # stst.append(or_list[j])


                stst.append(round(time_required, 2))

            stst.append(feed_rate_per_revolution)
            stst.append(n_list[cont2])
            stst.append(v_list[cont2])
            cont2 += 1
            table_1.add_row(stst)
            #print(stst)
            stst.clear()




            #print("\n")



print(table_1)
input("для завершения нажмите 'Enter' ")
# for i in range(len(d_list)):
#     for j in range(len(t_list)):
#         #print(d_list[j])
#         if d_list[i] == 20 and t_list[j] != 3:
#             continue
#         elif d_list[i] == 50 and t_list[j] == 15:
#             continue
#         else:
#             pass
            #print(j)
            #depth_of_cut = t_list[j] / 2
            #print(depth_of_cut * 2)
            #initial_diameter = d_list[j]


            #time_required = calculate_turning_time(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, cutting_speed, feed_rate_per_revolution, overrun, rapid_traverse_rate) * 1.1


# initial_diameter = 200.0  # начальный диаметр в мм
# final_diameter = 197.0  # конечный диаметр в мм
# depth_of_cut = 1.5  # глубина резания в мм (на сторону)
# length_of_workpiece = 500.0  # длина вала в мм
# cutting_speed = 101  # скорость резания в м/мин
# feed_rate_per_revolution = 0.36  # подача на один оборот в мм/об
# overrun = 10.0  # перебег резца в мм
# rapid_traverse_rate = 2000.0  # скорость возврата на ускоренной подаче в мм/мин




#time_required = calculate_turning_time(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, cutting_speed, feed_rate_per_revolution, overrun, rapid_traverse_rate) * 1.1
#print(f"Время обработки: {time_required:.2f} минут")
