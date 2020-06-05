// Pins
#define DS_pin 11
#define STCP_pin 10
#define SHCP_pin 13

// Variables
unsigned long previous_milis = 0L;
unsigned long default_time = 3000L;
unsigned long delay_time = default_time; 
boolean registers[72];
boolean cube[8][8][8];
boolean last = false;

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
  if (Serial.available() > 0){ // If the is data in the serial
    String input = Serial.readString(); // Take that data
    get_input(input); // Analyze it
  } 
}

/*
 * Writes the registers list on the bit array od the shift registers
 */
void write_reg(){
  digitalWrite(STCP_pin, LOW);
  
  for (int i = 71;i >= 0; i--){
    digitalWrite(SHCP_pin, LOW);
    digitalWrite(DS_pin, registers[i] );
    digitalWrite(SHCP_pin, HIGH);
  }
  
  digitalWrite(STCP_pin, HIGH);
}


/*
 * Clears the memory of the virtual cube
 */
void clear_cube(){
  memset(cube,LOW,sizeof(cube));
}

/*
 * Clears the registers list used for interacting withe the bit array in the shift registers
 */
void clear_registers(){  
  memset(registers,LOW,sizeof(registers));
}

/*
 * This function lets us modify the virtual cube
 */
void write_in_cube(int x,int y,int z,boolean value){
  cube[x][y][z] = value;
}


/*
 * Takes the input and processes all the commands to either modify the virtual cube, load the virtual cube or clear the cube
 */
void get_input(String input){
  Serial.println("Input: " + input);
  
  while (input != ""){
    if (input.charAt(0) == 'd'){ // DELAY

      // Takes the instruction substring
      String instruction = input.substring(0,input.indexOf("/"));
      
      // Takes the time unit from the instruction
      String time_unit = instruction.substring(instruction.lastIndexOf(",")+1,instruction.lastIndexOf(",")+4);

      // Sets the time multiplier necesary for the delay
      float multiplier;
      if (time_unit == "Seg"){
        multiplier = 1000;
      }
      else if (time_unit == "Mil"){
        multiplier = 1;
      }
      else if (time_unit == "Mic"){
        multiplier = 1/1000;
      }
      else if (time_unit=="Nan"){
        multiplier = 1/1000000;
      }

      // Sets the delay time and loads the cube
      delay_time = instruction.substring(2,instruction.lastIndexOf(",")).toInt()*multiplier;//toInt is long ,https://www.arduino.cc/reference/en/language/variables/data-types/string/functions/toint
      load_to_cube();

      // Removes the parsed instruction from the input
      input.remove(0,input.indexOf("/") + 1);

      // Tells the system that the latest message is not a turn
      if(last == true){
        last = false;
      }
    }
    
    else if(input.charAt(0) == 't'){ // TURN
      
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

      // Tells the system that the latest message is a turn
      if(last == false){
        last = true;
      }
    }

    else if(input.charAt(0) == 'b') { // BLINK
      // Removes the parsed instruction from the input
      input.remove(0,input.indexOf("/") + 1);
    }
    
    else if(input.charAt(0) == 'c'){ // CLEAR
      // Clears the virtual cube
      clear_cube();

      // Removes the parsed instruction from the input
      input.remove(0,5 + 1);
    }
    
    else if(input.charAt(0) == '.'){ // FINISH
      
      // Removes the last char from the string
      input.remove(0,1);
      Serial.println("Parse finished");

      // Sets the time to default
      delay_time = default_time;

      // If the last instruction was a delay load the virtual cube empty
      if(last == false){
        clear_cube();
      }

      // Loads the cube with the default time
      load_to_cube();

      // Empties the cube before finishing
      clear_cube();
      break;
    }
    
    else{
      Serial.println("Error: No input avalible");
      break;
    }
  }  
}

/*
 * Loads the virtual cube into the real cube using a multiplexing loop
 */
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
}
