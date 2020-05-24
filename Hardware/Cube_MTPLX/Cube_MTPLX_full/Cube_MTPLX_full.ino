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
  Serial.begin(9600);
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
  if (Serial.available()>0){//if there's data in the serial
    String input = Serial.readString();
    //convert string to char array
    unsigned int input_length = input.length()+1; 
    char char_input[input_length];
    input.toCharArray(char_input, input_length);

    get_input(char_input);
  }

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

void parse_input(String input){
  if (input.substring(0,5)== "delay"){
    delay_time=input.substring(7,8).toInt()*1000;//toInt is long ,https://www.arduino.cc/reference/en/language/variables/data-types/string/functions/toint
  }
  else if(input.substring(0,4)== "turn"){
    Serial.println("...");
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
      Serial.println("error1"); 
    } 
  }
  else if(input.substring(0,5)== "blink"){
    
  }
  else if(input.substring(0,5)== "clear"){
    clear_cube();
  }
  else{
    Serial.println("error2");
  }
  
}

void get_input(char char_input[]){
  char *instructions_array;
  instructions_array = strtok (char_input,"\n");
  for (int i=0; i<sizeof instructions_array/sizeof instructions_array[0]; i++) {
    String instruction(instructions_array[i]);
    parse_input(instruction); 
  }
}
