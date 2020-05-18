//arduino outputs
#define DS_pin 11
#define STCP_pin 10
#define SHCP_pin 13

unsigned long previous_milis = 0L; // L from long, important!
int multiplex_delay_microseconds = 50; //total multiplex time of the cube:25ms
int layer_pin = 64; //the first output of a layer
unsigned long delay_time = 50L;//delay time in ms. Should be long for math with other long numbers

boolean registers[72];//pins
boolean cube[8][8][8];//cube matrix. Initial values != true?, if don't work try https://stackoverflow.com/questions/3280203/how-to-initialize-three-dimensional-array-in-arduino

//turns on a specific led 
void write_in_cube(int x, int y, int z, boolean value){
  cube[x][y][z]=value;
}

void setup(){
  Serial.begin(9600);
  pinMode(DS_pin,OUTPUT);
  pinMode(STCP_pin,OUTPUT);
  pinMode(SHCP_pin,OUTPUT);

  clear_cube();
  
  //this lines are only for debug, they wont be in the final code!
  write_in_cube(0,1,2,true);//random led in [0,1,2]
  write_in_cube(5,3,7,true);//random led in [5,3,7]
  
}

void writeReg(int led_position){ //write in the registers
  registers[led_position]=HIGH;
  digitalWrite(SHCP_pin,LOW);
  digitalWrite(STCP_pin,LOW);
  digitalWrite(DS_pin,registers[led_position]);
  digitalWrite(STCP_pin,HIGH);
  digitalWrite(SHCP_pin,HIGH);
  delayMicroseconds(multiplex_delay_microseconds);//multiplexing.
}

void loop() {
  if (Serial.available()>0){//if there's data in the serial
    String input=Serial.readString();
    parse_input(input);
  }

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
  memset(cube,false,sizeof(cube));//would work??
}

void parse_input(String input){
  if (input.substring(0,5)== "delay"){
    delay_time=input.substring(7,8).toInt()*1000;//toInt is long ,https://www.arduino.cc/reference/en/language/variables/data-types/string/functions/toint
  }
  else if(input.substring(0,4)== "turn"){
    int x=input.substring(6,7).toInt();
    int y=input.substring(9,10).toInt();
    int z=input.substring(12,13).toInt();
    String state=input.substring(15);
    if(state=="T"){//verify datatypes
      write_in_cube(x,y,z,true);
    }
    else if (state=="F"){
      write_in_cube(x,y,z,false);
    }
    else{
      Serial.println("error"); 
    } 
  }
  else if(input.substring(0,5)== "blink"){
    
  }
  else if(input.substring(0,5)== "clear"){
    clear_cube();
  }
  else{
    Serial.println("error");
  }
  
}
