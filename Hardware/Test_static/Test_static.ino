//arduino outputs
#define DS_pin 11
#define STCP_pin 10
#define SHCP_pin 13

unsigned long previous_milis = 0L; // L from long, important!
int multiplex_delay_microseconds = 50; //total multiplex time of the cube:25ms
int layer_pin = 64; //the first output of a layer
unsigned long delay_time = 50L;//delay time in ms. Should be long for math with other long numbers

boolean registers[72];//pins
boolean cube[8][8][8];//cube matrix. Initial values != true?

//turns on a specific led 
void write_in_cube(int x, int y, int z, boolean value){
  cube[x][y][z]=value;
}

void setup(){
  pinMode(DS_pin,OUTPUT);
  pinMode(STCP_pin,OUTPUT);
  pinMode(SHCP_pin,OUTPUT);

  void clear_cube();
  void writeReg();
  //this lines are only for debug, they wont be in the final code!
  write_in_cube(0,1,2,HIGH);//random led in [0,1,2]
  write_in_cube(5,3,7,HIGH);//random led in [5,3,7]
  
}

void writeReg(int led_position){ // original writeReg function
  registers[led_position]=HIGH;
  digitalWrite(SHCP_pin,LOW);
  
  digitalWrite(STCP_pin,LOW);
  digitalWrite(DS_pin,registers[led_position]);
  digitalWrite(STCP_pin,HIGH);
  digitalWrite(SHCP_pin,HIGH);
  delayMicroseconds(multiplex_delay_microseconds);//multiplexing.
  registers[led_position]=LOW; 
}

void loop() {
  while(millis()-previous_milis<delay_time){//while for delay time
    for(int k=0; k<8; k++){
      registers[k+layer_pin]=HIGH;
      for(int j=0; j<8; j++){
        for(int i=0; i<8; i++){
          if(cube[i][j][k]){//the cube has booleans values
            int led_position=i*8+j;
            writeReg(led_position);     
          }
        }
      }
      registers[k+layer_pin]=LOW;
    }
  }
  previous_milis=millis();
  delay(delay_time);//the loop is going to run for delay_time, after, a delay of (delay_time)
}

void clear_cube(){
  memset(cube,LOW,sizeof(cube));//would work??
}
