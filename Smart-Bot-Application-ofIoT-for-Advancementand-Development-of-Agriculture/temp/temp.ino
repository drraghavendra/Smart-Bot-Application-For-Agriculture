float t;
int tempPin = 0;

void setup() {
   Serial.begin(9600);
}

void loop() {
   t = analogRead(tempPin);
   t=t*48.828125;
   Serial.print("TEMPERATURE = ");
   Serial.print(t); 
   Serial.print("*C");
   Serial.println();
   delay(1000); 
}
