// C++ code
//
int button;
void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT);
}

void loop()
{
  button = digitalRead(2);
  if (button){
    Serial.print(1);
  }
  else{
    Serial.print(0);
  }
  delay(500);
}
