
#define DS_pin 8
#define STCP_pin 9
#define SHCP_pin 10

boolean registers[16];

void setup() {
  pinMode(DS_pin,OUTPUT);
  pinMode(STCP_pin,OUTPUT);
  pinMode(SHCP_pin,OUTPUT);
  void writeReg();
}

void writeReg(){
  digitalWrite(SHCP_pin,LOW);

  for(int i = 15;i >= 0;i--){
    digitalWrite(STCP_pin,LOW);
    digitalWrite(DS_pin,registers[i]);
    digitalWrite(STCP_pin,HIGH);
  }
  digitalWrite(SHCP_pin,HIGH);
}

void loop() {
  for (int i = 0;i < 17;i++){
    registers[i] = HIGH;
    delay(100);
    writeReg();
  }

    for (int i = 0;i < 17;i++){
    registers[i] = LOW;
    delay(100);
    writeReg();
  }
}
