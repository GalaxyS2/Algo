import time
start_time = time.clock()

counter_exchange = 0 # каунтер на перестановки
counter_compare = 0 # каунтер на порівняння
def mergeSort(animals):
    
    global counter_compare
    global counter_exchange
    
    print("Splitting ",animals)# це виводить в момент, коли список розбивається на менші списки (потім треба стерти)
    if len(animals)>1:
        mid = len(animals)//2
        left = animals[:mid]
        right = animals[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:# якщо елемент з лівого списка менший ніж з правого - то закинути його в енімалс
                counter_compare += 1
                animals[k]=left[i]
                i=i+1# це щоб перейти до наступного елементу в лівому списку
                counter_exchange +=1
            else:# якщо елемент з правого списка менший ніж з лівого - то закинути його в енімалс
                counter_compare += 1
                animals[k]=right[j]
                j=j+1# це щоб перейти до наступного елементу в правому списку
                counter_exchange +=1
            k=k+1# це щоб перейти до наступного елементу в списку енімалс (тіпа до пустого)

		# Якщо в одному зі списків закінчаться елементи - то всі з інакшого просто перенесуться (тіпа якщо правий пустий - то лівий весь попаде в кінець енімалс)
        while i < len(left): 
            animals[k]=left[i]
            i=i+1
            k=k+1
            counter_exchange +=1

        while j < len(right):
            animals[k]=right[j]
            j=j+1
            k=k+1
            counter_exchange +=1
    print(counter_compare, counter_exchange) # це виводить скільки було операцій порівняння і перестановки (потім треба стерти)

my_file = open("animals.txt")
animals = []
for line in my_file: # додає в масив енімалс по рядку з файлу
	animals.append(line.rstrip().split(", "))
my_file.close()

new_animals = []
for i in range(len(animals)):
	if animals[i][2] == "predator":
		new_animals.append([animals[i][0].lower() +" "+ "Predator", int(animals[i][3]), animals[i][1]])
	else:
		new_animals.append([animals[i][0].lower() +" "+ animals[i][2], int(animals[i][3]), animals[i][1]])
	
# от тут все як є - так і вивести (решту прінтів зверху позначено, які стерти)	
mergeSort(new_animals)
for i in range(len(new_animals)): #Для гарного виведення інфи
	new_animals[i][1] = str(new_animals[i][1])
	print(" ".join(new_animals[i]))# це щоб виводило рядочком, а не масивом
print("Comapers: ", counter_compare, "Exchanges: ", counter_exchange)


print(time.clock() - start_time, "seconds")