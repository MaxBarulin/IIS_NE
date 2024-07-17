import math

def calculate_turning_time(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, spindle_speed, feed_rate):
    """
    Рассчитывает время обработки вала.

    :param initial_diameter: начальный диаметр вала (мм)
    :param final_diameter: конечный диаметр вала (мм)
    :param depth_of_cut: глубина резания (мм)
    :param length_of_workpiece: длина вала (мм)
    :param spindle_speed: частота вращения шпинделя (об/мин)
    :param feed_rate: подача на один оборот (мм/об)
    :return: время обработки в минутах
    """
    
    # Определение количества проходов
    total_depth = (initial_diameter - final_diameter) / 2
    number_of_passes = math.ceil(total_depth / depth_of_cut)
    
    # Общее время обработки
    total_time = 0
    
    for i in range(number_of_passes):
        # Диаметр после текущего прохода
        current_diameter = initial_diameter - 2 * depth_of_cut * (i + 1)
        
        # Проверка, чтобы диаметр не стал меньше конечного
        if current_diameter < final_diameter:
            current_diameter = final_diameter
        
        # Скорость резания
        cutting_speed = math.pi * current_diameter * spindle_speed
        print(cutting_speed)
        # Подача инструмента
        feed_per_minute = feed_rate * spindle_speed
        
        # Время обработки для текущего прохода
        pass_time = length_of_workpiece / feed_per_minute
        
        total_time += pass_time
    
    return total_time

# Пример использования функции
initial_diameter = 20.0  # начальный диаметр в мм
final_diameter = 10.0  # конечный диаметр в мм
depth_of_cut = 3.0  # глубина резания в мм
length_of_workpiece = 10.0  # длина вала в мм
spindle_speed = 1000  # частота вращения шпинделя в об/мин
feed_rate = 0.26  # подача на один оборот в мм/об

time_required = calculate_turning_time(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, spindle_speed, feed_rate)
print(f"Время обработки: {time_required:.2f} минут")
