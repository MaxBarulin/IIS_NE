import time
import requests
import threading

from prettytable import PrettyTable as PT
from requests_ntlm import HttpNtlmAuth
from bs4 import BeautifulSoup

from progress.bar import IncrementalBar as IB

def send_authenticated_request(url, username, password):
    try:
        response = requests.get(url, auth=HttpNtlmAuth(f'{username}', f'{password}'))
        # Проверка успешности запроса
        if response.status_code == 200:
            # Вернуть текст ответа
            return response.text
        else:
            return f"Ошибка запроса: {response.status_code}"
    except Exception as e:
        return f"Ошибка: {e}"

def send_request(url):
    try:
        response = requests.get(url)
        # Проверка успешности запроса
        if response.status_code == 200:
            # Вернуть текст ответа
            return response.text
        else:
            return f"Ошибка запроса: {response.status_code}"
    except Exception as e:
        return f"Ошибка: {e}"





def final(listus):
    global color
    global viwe_tt
    viwe_t = []

    num = (len(listus))
    for k in range(0, num):
        url = f'http://srv-photo.ashipyards.com/status.php?{listus[k][7]}' # Замените на нужный URL
        response_text = send_request(url)
        #print(f'{response_text}\n')
        if 'MediumSeaGreen' in response_text:
            color = '+'
            u_in.append(1)
        else:
            color = '-'
            u_out.append(1)
            first_name_out.append(list_3[k][0])
            t_2.append('-')
            t_2.append(list_3[k][0])
            t_2.append(list_3[k][7])

            #print(t_2)

        viwe_t.append(color)
        viwe_t.append(listus[k][0])
        viwe_t.append(listus[k][7])
        viwe_tt.append(viwe_t)
        #print(viwe_t)
        viwe_t = []
        bar.next()



# Пример использования функции send_authenticated_request
time_start = time.strftime('%X')
#url = ['http://portal/Pages/Phonebook.aspx?View={EFE8C997-A328-44E4-9F3E-56B969C56B02}&FilterField1=Division&FilterValue1=%D0%A6%D0%95%D0%A5%2022', 'http://portal/Pages/Phonebook.aspx?Paged=TRUE&p_Division=%d0%a6%d0%95%d0%a5%2022&p_FullName1=8_%d0%9c%d0%98%d0%a5%d0%90%d0%99%d0%9b%d0%9e%d0%92%20%d0%94%d0%9c%d0%98%d0%a2%d0%a0%d0%98%d0%99%20%d0%92%d0%90%d0%a1%d0%98%d0%9b%d0%ac%d0%95%d0%92%d0%98%d0%a7&p_ID=5016914&PageFirstRow=401&FilterField1=Division&FilterValue1=%D0%A6%D0%95%D0%A5%2022&&&View={EFE8C997-A328-44E4-9F3E-56B969C56B02}'] # Замените на нужный URL
url = ['http://portal/Pages/Phonebook.aspx?View={EFE8C997-A328-44E4-9F3E-56B969C56B02}&FilterField1=OrganizationalIDNumber&FilterValue1=992&FilterField2=ol%5FDepartment&FilterValue2=%D0%91%D1%8E%D1%80%D0%BE%20%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D1%82%D1%80%D1%83%D0%B4%D0%BE%D0%B5%D0%BC%D0%BA%D0%BE%D1%81%D1%82%D1%8C%D1%8E']
username = 'barulin.ma' # Ваш логин Windows
password = 'BarulinMax352678999' # Ваш пароль Windows

color = ''
page_num = len(url)
count = 0
all_list_name = []
all_list = []

u_in = []
u_out = []
first_name_out = []

t_2 = []

viwe_tt = []

table_1 = PT()
table_1.field_names = ['+/-', 'Фамилия', 'Таб. №']


for i in range(0, page_num):
    response_text = send_authenticated_request(url[i], username, password)
    soup_1 = BeautifulSoup(response_text, 'html.parser')
    links_1 = soup_1.find_all('a')
    #print(links_1)

    for link in links_1:
        link_text = link.get_text()
        if link_text.isupper():
            count += 1
            if count < 14:
                continue

            else:
                all_list_name.append([link.get_text()])

    count = 0

#print(len(all_list_name))

    soup_2 = BeautifulSoup(response_text, 'html.parser')
    td_tag_text = soup_2.find_all(class_='ms-vb2')

    temp_list = []
    index = 0

    for text in td_tag_text:
        temp_list.append(text.get_text())
        index += 1

        if index % 11 == 0 or index == len(td_tag_text):
            #print(temp_list)
            all_list.append(temp_list)
            temp_list = []


#print(len(all_list))
#print(len(all_list_name))
num_person = len(all_list_name)

list_3 = []
for sub_list_1, sub_list_2 in zip(all_list, all_list_name):
    # Добавляем первый элемент из sub_list_2 в начало sub_list_1 и сохраняем результат в sublist_3
    sublist_3 = sub_list_2 + sub_list_1
    # Добавляем sublist_3 в list_3
    list_3.append(sublist_3)

#print(list_3)

num_segment = (len(list_3) / 5) + 1
int_num_segment = int(num_segment)
chunk_size = int_num_segment
chunks = [list_3[k:k + chunk_size] for k in range(0, len(list_3), chunk_size)]
num_segment_1 = (len(all_list_name) / 5) + 1
int_num_segment_1 = int(num_segment_1)
chunk_size_1 = int_num_segment_1
chunks_1 = [all_list_name[k:k + chunk_size_1] for k in range(0, len(all_list_name), chunk_size_1)]


#final(chunks[0])
with IB('Люди', max=num_person) as bar:
    t1 = threading.Thread(target=final, args=(chunks[0],), daemon=True)
    t2 = threading.Thread(target=final, args=(chunks[1],), daemon=True)
    t3 = threading.Thread(target=final, args=(chunks[2],), daemon=True)
    t4 = threading.Thread(target=final, args=(chunks[3],), daemon=True)
    t5 = threading.Thread(target=final, args=(chunks[4],), daemon=True)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

#print(len(viwe_tt))

table = PT()
table.field_names = ['+/-', 'Фамилия', 'Таб. №']

table_2 = PT()
table_2.field_names = ['-', 'Фамилия', 'Таб. №']

outtt = []

for m in viwe_tt:
    #print(m)
    table.add_row(m)
    if m[0] == '-':
        outtt.append(m)

outus = len(outtt)
for n in outtt:
    #print(n)
    table_2.add_row(n)



print(table.get_string())
print('')
print('Отсутствующие:')
print(table_2.get_string())
print(f'\nвсего: {num_person}\nотсутствует: {outus}\nприсутствует: {num_person - outus}\n')

time_end = time.strftime('%X')
print(time_start, time_end)

input('для завершения нажмите "Enter" ')













