int DS_pin = 11;
int STCP_pin = 10;
int SHCP_pin = 13;

void setup()
{
 pinMode(DS_pin,OUTPUT);
 pinMode(STCP_pin,OUTPUT);
 pinMode(SHCP_pin,OUTPUT);
 
 writereg();
}

boolean registers[8];

void writereg()
{
  digitalWrite(STCP_pin, LOW);
  
  for (int i = 71; i>=0; i--)
  {
    digitalWrite(SHCP_pin, LOW);
    digitalWrite(DS_pin, registers[i] );
    digitalWrite(SHCP_pin, HIGH);
  }
  
  digitalWrite(STCP_pin, HIGH);
}

void loop()
{

 // Turns on all the leds
 for(int i = 0; i<72; i++)
 {
  registers[i] = HIGH;
  writereg();
 }

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
 */

 /*
 // Turns off all the LEDs
 for(int i = 0; i<72; i++)
 {
  registers[i] = LOW;
  writereg();
 }

 // Waits half a second
 delay(500);

 // Turns activates one layer and one column, therefore one LED is turn on
 registers[71] = HIGH;
 writereg();
 registers[0] = HIGH;
 writereg();

 // Waits one second
 delay(1000);
 */

 
}
