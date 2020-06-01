// Pins
#define DS_pin 11
#define STCP_pin 10
#define SHCP_pin 13

// Variables
unsigned long previous_milis = 0L; // L from long, important!
unsigned long default_time = 3000L;
unsigned long delay_time = default_time; //delay time in ms. Should be long for math with other long numbers
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
  clear_cube();
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

void get_input(String input){
  Serial.println("Input: " + input);
  
  while (input != ""){
    if (input.charAt(0) == 'd'){ // DELAY, variable characters

      // Takes the instruction substring
      String instruction = input.substring(0,input.indexOf("/"));//https://www.arduino.cc/en/Tutorial/StringIndexOf , https://en.wikipedia.org/wiki/Escape_sequences_in_C
      
      // Takes the time unit from the instruction
      String time_unit = instruction.substring(instruction.lastIndexOf(",")+1,instruction.lastIndexOf(",")+4);
      
      int multiplier;
      if (time_unit == "Seg"){
        multiplier = 1000;
      }
      else if (time_unit == "Mil"){
        multiplier = 1;
      }
      else if (time_unit == "Mic"){
        multiplier = 0,01;
      }
      else if (time_unit=="Nan"){
        multiplier = 0,000001;
      }
      else{
          Serial.println("error in time unit");
      }
      
      delay_time = instruction.substring(2,instruction.lastIndexOf(",")).toInt()*multiplier;//toInt is long ,https://www.arduino.cc/reference/en/language/variables/data-types/string/functions/toint
      load_to_cube();

      // Removes the parsed instruction from the input
      input.remove(0,input.indexOf("/") + 1);
    }
    
    else if(input.charAt(0) == 't'){ // TURN, 5 + 1 [\] characters
      
      // Takes the instruction substring
      String instruction = input.substring(0,5);

      //Gets the values from the instruction      
      int x = instruction.substring(1,2).toInt();
      int y = instruction.substring(2,3).toInt();
      int z = instruction.substring(3,4).toInt();
      String state = instruction.substring(4,5);

      // Loads the instruction on the virtual cube
      if(state == "T"){
        write_in_cube(x,y,z,true);
      }
      else if(state == "F"){
        write_in_cube(x,y,z,false);
      }
      else{
          Serial.println("error in boolean instruction type");
      }
      
      // Removes the parsed instruction from the input
      input.remove(0,5 + 1);
    }
    
    else if(input.charAt(0) == 'c'){// CLEAR, 5 + 1 [\] characters
      // Clears the virtual cube
      clear_cube();

      // Removes the parsed instruction from the input
      input.remove(0,5 + 1);
    }
    else if(input.charAt(0) == '.'){
      input.remove(0,1);
      Serial.println("Parse finished");
      delay_time = default_time;
      load_to_cube();
      break;
    }
    
    else{
      Serial.println("No input avalible");
      break;
    }
  }  
}

void load_to_cube(){
  previous_milis = millis();
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
  //previous_milis = millis();
}
