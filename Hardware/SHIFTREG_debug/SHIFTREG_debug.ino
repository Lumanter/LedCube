#define DS_pin 11
#define STCP_pin 10
#define SHCP_pin 13

void setup()
{
 pinMode(DS_pin,OUTPUT);
 pinMode(STCP_pin,OUTPUT);
 pinMode(SHCP_pin,OUTPUT);
 
 writereg();
}

boolean registers[72];

void writereg(){
  digitalWrite(STCP_pin, LOW);
  
  for (int i = 71; i>=0; i--)
  {
    digitalWrite(SHCP_pin, LOW);
    digitalWrite(DS_pin, registers[i] );
    digitalWrite(SHCP_pin, HIGH);
  }
  
  digitalWrite(STCP_pin, HIGH);
}

void turnAllOn(){
  for(int i = 0;i < 72;i++)
  {
    registers[i] = HIGH;
  }
  writereg();
}

void turnAllOff(){
  for(int i = 0;i < 72;i++)
  {
    registers[i] = LOW;
  }
  writereg();
}

void turnLayers(bool layers[]){
  for(int i = 0;i < 8;i++){
    if(layers[i] == true){
      registers[64+i] = HIGH;
    }
    else {
      registers[64+i] = LOW;
    }
  }
}

void loop()
{
 
 // Turns on all the leds
 turnAllOn();

 // Waits 2.5 seconds
 delay(2500);

 // Turns off the LEDs columns one by one
 for(int i = 63; i>=0; i--)
 {
  registers[i] = LOW;
  delay(300);
  writereg();

 }
 // Waits 2.5 seconds
 delay(2500);
  

  ////////////////

 /*
 // Turns off all the LEDs
 turnAllOff();

 // Waits half a second
 delay(500);

 // Turns activates one layer and one column, therefore one LED is turn on
 registers[71] = HIGH;
 registers[0] = HIGH;
 writereg();

 // Waits one second
 delay(1000);
 */

 ////////////////

 /*
 // With this list of layers and this function you can choose which cathode layer is turn on or off
 bool layers[8] = {true,true,true,true,true,true,true,true};
 turnLayers(layers);
 
 writereg();

 for (int i = 0;i < 64;i++){
  registers[i] = HIGH;
  writereg();
  delay(500);
  registers[i] = LOW;
  writereg();
 }
 */
 
}
