void setup() {
    Serial.begin(9600); // Установка скорости передачи
}

void loop() {
    int sensorValue = analogRead(A0); // Чтение значения с датчика
    Serial.println(sensorValue); // Отправка значения в Serial
    delay(1000); // Задержка 1 секунды
}