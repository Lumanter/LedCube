
#define DS_pin 11
#define STCP_pin 10
#define SHCP_pin 13
#define delay_time 50
#define multiplex_delay_microseconds 100

boolean registers[72];//pins
boolean cube[8][8][8]//cube matrix. Initial values != true?


void write_in_cube(int x, int y, int z, boolean value){
  cube[x][y][z]=value;
    
}

void setup(){
  pinMode(DS_pin,OUTPUT);
  pinMode(STCP_pin,OUTPUT);
  pinMode(SHCP_pin,OUTPUT);
  //turn on leds,[0-7]
  write_in_cube(0,1,2,true);
  write_in_cube(5,3,7,true);
  
  void writeReg();
  
}

void writeReg(){
  digitalWrite(SHCP_pin,LOW);

  for(int i = 71;i >= 0;i--){
    digitalWrite(STCP_pin,LOW);
    digitalWrite(DS_pin,registers[i]);
    digitalWrite(STCP_pin,HIGH);
  }
  digitalWrite(SHCP_pin,HIGH);
}

void loop() {
  for(int k = 0;i < 8;i++){
    registers[k+64]=HIGH;
    for(int j = 0;i < 8;i++){
      for(int i = 0;i < 8;i++){
        if(cube[i][j][k]){
          registers[8*(j-1)+1]=HIGH;
          delayMicroseconds(100)//multiplexing
          registers[8*(j-1)+1]=LOW;          
        }
      }
    }
    registers[k+64]=LOW;
  }
}
