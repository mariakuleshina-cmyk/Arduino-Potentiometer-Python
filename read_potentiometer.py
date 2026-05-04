import serial
import time
import matplotlib.pyplot as plt

arduino = serial.Serial('COM9', 9600)  # Подключение к Arduino
time.sleep(2)    # Ожидание подключения
count = 0
data = []
    
for _ in range(100):  # Чтение 100 значений
    count += 1
    value = arduino.readline().decode('utf-8').strip()
    data.append(int(value))
    print(f"Значение {count}: {value}")
arduino.close()

plt.plot(data, color="#277F33")
plt.title("Данные потенциометра с Arduino")
plt.xlabel("Номер измерения")
plt.ylabel("Значение")
plt.show()








