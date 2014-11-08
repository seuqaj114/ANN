int pfrente=5,ptras=3,pesq=6,pdirei=9;
char comd=0;
int duration=150;
int durationstr=70;
int gap=150;
int gap2=250;

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
       delay(durationstr);
       analogWrite(pfrente,255);
       break;
    case 'r':
      analogWrite(pesq,0);
      delay(gap);
      analogWrite(pfrente,0);
      delay(duration);
      analogWrite(pfrente,255);
      delay(gap2);
      analogWrite(pesq,255);
      break;

    case 't':
      analogWrite(pdirei,0);
      delay(gap);
      analogWrite(pfrente,0);
      delay(duration);
      analogWrite(pfrente,255);
      delay(gap2);
      analogWrite(pdirei,255);
      break;
    case 'y':
      analogWrite(pesq,0);
      delay(gap);
      analogWrite(ptras,0);
      
      delay(duration);
      analogWrite(ptras,255);
      delay(gap2);
      analogWrite(pesq,255);
      break;   
    case 'u':
      analogWrite(pdirei,0);
      delay(gap);
      analogWrite(ptras,0);
      
      delay(duration);
      analogWrite(ptras,255);
      delay(gap2);
      analogWrite(pdirei,255);
      break;
   case 's':
     analogWrite(ptras,0);
     delay(durationstr);
     analogWrite(ptras,255);
     break;
    
   case 'a':
     analogWrite(pesq,0);
     delay(duration);
     analogWrite(pesq,255);
     break;
     
   case 'd':
     analogWrite(pdirei,0);
     delay(duration);
     analogWrite(pdirei,255);
     break;
     
     default:
       comd=0;
       break;
     } 
  }
}
  
