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
}

void loop()
{
  if (Serial.available() > 0){//if there's data in the serial
    String input = Serial.readString();
    get_input(input);
  } 
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
  Serial.println("INSTRUCTION received: " + input);
  if (input.charAt(0)== "d"){//delay
    delay_time = input.substring(7,8).toInt()*1000;//toInt is long ,https://www.arduino.cc/reference/en/language/variables/data-types/string/functions/toint
    load_to_cube();
  }
  else if(input.charAt(0) == "t"){//turn
    Serial.println("...");
    int x = input.substring(6,7).toInt();
    int y = input.substring(9,10).toInt();
    int z = input.substring(12,13).toInt();
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
  else if(input.charAt(0)== "b"){//blink
    
  }
  else if(input.charAt(0)== "c"){//clear
    clear_cube();
  }
  else{
    Serial.println("error2");
  }
  
}

void get_input(String input){
  Serial.println("Input: " + input);

  int cont = 0;//the counter of the instructions_array elements to be inserted
  
  String instructions_array[input.length() / 5]; // CAMBIAR

  //identify the tipe of the instruction
  
  boolean there_is_delay = false;
  
  while (input != ""){
    if (input.charAt(0) == "d"){ //delay, 14 characters
      Serial.println("Delay: " + input.substring(0,14));
      instructions_array[cont] = input.substring(0,14);
      cont++;
      input.remove(0,16);
      there_is_delay = true;
      break;
    }
    else if(input.charAt(0) == "t"){//turn , 16 characters
      Serial.println("turn: " + input.substring(0,16));
      instructions_array[cont] = input.substring(0,16);
      cont++;
      input.remove(0,18);
   
    }
    else if(input.charAt(0) == "b"){//blink
      instructions_array[cont] = input.substring(0,23);
      cont++;
      input.remove(0,25);
      
    }
    else if(input.charAt(0) == "c"){//clear
      instructions_array[cont] = input.substring(0,5);
      cont++;
      input.remove(0,7);
    }
    else{
      Serial.println("error: input not recognized");
      break;
    }
  }

  if(!there_is_delay){
    instructions_array[cont] = "delay, "+String(delay_time)+", sec \n";
  }
  
  for (int i = 0;i < sizeof(instructions_array) / sizeof(instructions_array[0]);i++) {// sizeof returns the number of bytes
    String instruction = instructions_array[i] ;
    parse_input(instruction); 
  }

  if(input != ""){
    get_input(input);
  }
}

void load_to_cube(){
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
  previous_milis = millis();
}
