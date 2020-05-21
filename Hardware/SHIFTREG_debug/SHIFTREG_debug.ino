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

/*
 * Turns on all the LEDs on the cube
 */
void turnAllOn(){
  for(int i = 0;i < 72;i++)
  {
    registers[i] = HIGH;
  }
  writereg();
}

/*
 * Turns off all the LEDs on the cube
 */
void turnAllOff(){
  for(int i = 0;i < 72;i++)
  {
    registers[i] = LOW;
  }
  writereg();
}

/*
 * Turns the choosen cathode layers on or off
 */
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

/*
 * Turns a specific LED either on or off using its coordinates
 */
void turnLED(int x,int y,int z,bool state){
  registers[(y * 8) + x] = HIGH;
  registers[z + 64] = HIGH;
  writereg();
}

void loop(){
  
  //-//-//-//-//-//-//-//
  /*
   * This section activates the entire cube and starts turning off al the columns one by one 
   * from last to first
   */
  /*
  // Turns on all the leds
  turnAllOn();

  // Waits 2.5 seconds
  delay(2500);

  // Turns off the LEDs columns one by one
  for(int i = 63;i >=0; i--){
    registers[i] = LOW;
    delay(225);
    writereg();
  }
  
  // Waits 2.5 seconds
  delay(1500);
*/

  //-//-//-//-//-//-//-//
  /*
   * This section turns off the entire cube and then blinks the LED for the first 
   * column and the highest layer
   */

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
  delay(500);
*/
 
  //-//-//-//-//-//-//-//
  /*
   * Using a function for controlling the layers this section of the code tests all 
   * the columns by turning them on for half a second in ascending order
   */

  /*
  // With this list of layers and this function you can choose which cathode layer is turn on or off
  bool layers[8] = {false,false,false,false,true,true,true,true};
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

 //-//-//-//-//-//-//-//
  /*
   * This part is a small simple test for multiplexing using the simple method of turning a LED on and off
   * rapidly
   */

  // Alternates between turning two LEDs that if turn on at the same time would turn on two extra LEDs, using this
  // Multiplexing method this won't happen
  turnAllOff();
  turnLED(0,0,7,true);
  turnAllOff();
  turnLED(7,7,0,true);

}
