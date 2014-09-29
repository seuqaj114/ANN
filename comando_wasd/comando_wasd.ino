int pfrente=5,ptras=3,pesq=6,pdirei=9;
char comd=0;

void setup(){
  Serial.begin(9600);
  pinMode(pfrente,OUTPUT);
  pinMode(ptras,OUTPUT);
  pinMode(pesq,OUTPUT);
  pinMode(pdirei,OUTPUT);
  analogWrite(pfrente,255);
  analogWrite(ptras,255);
  analogWrite(pesq,255);
  analogWrite(pdirei,255);
}

void loop(){
if(Serial.available()){
  comd=Serial.read();  
  switch(comd){
     case 'w':
       analogWrite(pfrente,0);
       delay(500);
       analogWrite(pfrente,255);
       break;
       
    case 'wd':
      analogWrite(pfrente,0);
      analogWrite(pdirei,0);
      delay(500);
      analogWrite(pfrente,255);
      analogWrite(pdirei,255);
      break;
    case 'wa':
      analogWrite(pfrente,0);
      analogWrite(pesq,0);
      delay(500);
      analogWrite(pfrente,255);
      analogWrite(pesq,255);
      break;
    case 'sd':
      analogWrite(ptras,0);
      analogWrite(pdirei,0);
      delay(500);
      analogWrite(ptras,255);
      analogWrite(pdirei,255);
      break;
    case 'sa':
      analogWrite(ptras,0);
      analogWrite(pesq,0);
      delay(500);
      analogWrite(ptras,255);
      analogWrite(pesq,255);
      break;   
      
   case 's':
     analogWrite(ptras,0);
     delay(500);
     analogWrite(ptras,255);
     break;
    
   case 'a':
     analogWrite(pesq,0);
     delay(500);
     analogWrite(pesq,255);
     
   case 'd':
     analogWrite(pdirei,0);
     delay(500);
     analogWrite(pdirei,255);

     default:
       comd=0;
       break;
     } 
  }
}
  
