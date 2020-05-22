// Pins
#define DS_pin 11
#define STCP_pin 10
#define SHCP_pin 13

// Variables
unsigned long previous_milis = 0L; // L from long, important!
unsigned long delay_time = 3000L;//delay time in ms. Should be long for math with other long numbers
boolean registers[72]; //pins
boolean cube[8][8][8];//cube matrix. Initial values != true?

void setup(){
  pinMode(DS_pin,OUTPUT);
  pinMode(STCP_pin,OUTPUT);
  pinMode(SHCP_pin,OUTPUT);
   
  clear_cube();
  clear_registers();
  write_reg();
  
  //this lines are only for debug, they wont be in the final code!
  write_in_cube(0,0,0,HIGH);//random led in [0,0,0]
  write_in_cube(0,0,1,HIGH);//random led in [0,0,1]
  write_in_cube(0,0,2,HIGH);//random led in [0,0,2]
  write_in_cube(0,0,3,HIGH);//random led in [0,0,3]
  write_in_cube(0,0,4,HIGH);//random led in [0,0,4]
  write_in_cube(0,0,5,HIGH);//random led in [0,0,5]
  write_in_cube(0,0,6,HIGH);//random led in [0,0,6]
  write_in_cube(0,0,7,HIGH);//random led in [0,0,7]
}

void loop()
{
  while((millis() - previous_milis) < delay_time){ //while for delay time
    for(int k = 0;k < 8; k++){
      registers[k + 64] = HIGH;
      for(int j = 0;j < 8;j++){
        for(int i = 0;i < 8;i++){
          if(cube[i][j][k]){ //the cube has booleans values
            registers[i * 8 + j] = HIGH;
          }
        }
        
      }
      write_reg();
      clear_registers();
      write_reg();      
    }
  }
  delay(delay_time); // the loop is going to run for delay_time, after, a delay of (delay_time)
  previous_milis = millis();
}

void write_reg(){
  digitalWrite(STCP_pin, LOW);
  
  for (int i = 71;i >= 0; i--){
    digitalWrite(SHCP_pin, LOW);
    digitalWrite(DS_pin, registers[i] );
    digitalWrite(SHCP_pin, HIGH);
  }
  
  digitalWrite(STCP_pin, HIGH);
}

void clear_cube(){
  memset(cube,LOW,sizeof(cube));
}

void clear_registers(){  
  memset(registers,LOW,sizeof(registers));
}

void write_in_cube(int x,int y,int z,boolean value){
  cube[x][y][z] = value;
}
