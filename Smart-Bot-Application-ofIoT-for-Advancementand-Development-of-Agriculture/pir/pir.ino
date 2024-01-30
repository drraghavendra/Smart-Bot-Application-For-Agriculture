int pirPin = 2;
int buzzerPin = 12; 
void setup()
{
Serial.begin(9600);
pinMode(pirPin, INPUT);
pinMode(buzzerPin, OUTPUT);
}
void loop()
{
int pirVal = digitalRead(pirPin);
Serial.println(pirVal);
if(pirVal == HIGH)
{ //was motion detected
Serial.println("Motion Detected");
digitalWrite(buzzerPin, HIGH);
delay(300);
digitalWrite(buzzerPin, LOW);
}




}
