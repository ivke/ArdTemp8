#include <PID_v1.h>
int tempV1pin=0;
int SetMPA=7; // multiplexer input cd4051 
int SetMPB=6;
int SetMPC=5;
int Rele1=4;
int Rele2=3;
int Rele3=2;
int Rele4=1;
int Rele5=8;
int Rele6=9;
int ADCT[8]; // vrednost bufferja za T
int ADCSp[]={0,0,0}; // zeljena vrednost ADC za Temperaturo pride iz računalnika ali je ročno nastavljena 
unsigned long CurrentTime; //timer
unsigned long PreviousTime;
int TimePeriod1=5000;
int TimePeriod2=2000;
double Setpoint, Input, Output;
String inputString="";
PID myPID(&Input, &Output, &Setpoint,2,2,1, DIRECT);
int casOn[10]; // cas ko je prizgan grelec (regulator 1,2,3) izracunan z PID funkcijo
int casOff; 

void setup()
{
  analogReference(EXTERNAL);
  Serial.begin(9600);
  pinMode(SetMPA,OUTPUT);
  pinMode(SetMPB,OUTPUT);
  pinMode(SetMPC,OUTPUT);
  pinMode(Rele1,OUTPUT);
  pinMode(Rele2,OUTPUT);
  pinMode(Rele3,OUTPUT);
  pinMode(Rele4,OUTPUT);
  pinMode(Rele5,OUTPUT);
  pinMode(Rele6,OUTPUT);
    
  // varnostno ker je vezan na rele in je v off na ON
  digitalWrite(Rele1,HIGH);
  digitalWrite(Rele2,HIGH);
  digitalWrite(Rele3,HIGH);
  digitalWrite(Rele4,HIGH);
  digitalWrite(Rele5,HIGH);
  digitalWrite(Rele6,HIGH);
  Setpoint = 10;
  //turn the PID on
  myPID.SetMode(AUTOMATIC);    
  delay(10000); // pocakamo 5 sekund da se temp. senzor stabilizira
  PreviousTime=millis();
  
}

void loop()
{
  
  for (int n=0; n<8;n++) {  // pogleda vse temperature in jih zapiše
    // izberemo temperaturni senzor
    Multiplexer(n+1);
    delay(300); // pod 300 ms vrednosti še niso stabilne nad so bi bilo potrebno izračunati glede na filter na koncu
    if (n<3) {  // prvi trije senzorji skrbijo tudi za regulacijo
      Setpoint=ADCSp[n];
      ADCT[n]=int(analogRead(tempV1pin)); // preberemo vrednost na temp. senzorju
      Input = ADCT[n];   // posredujemo za izračun
      myPID.Compute();   // izračunaj odziv od 0 do 255
      casOn[n]=Output*5; // cas deleza prizganega grelca max 255x5 ms
   } else 
    {  // za ostale se vrednost samo zapiše...
      Multiplexer(n+1);
      delay(300);
      ADCT[n]=int(analogRead(tempV1pin));
      //Serial.print(ADCT[n]);
      //Serial.print(" ");
    }
     //Serial.println("");
  }
  
    
  
  for (int n=0; n<3;n++) {
    CurrentTime=millis();
    if (CurrentTime-PreviousTime<casOn[n]) 
       {
        // prižgi rele
        RegTempSwitch(n+1,LOW);
        }
    else 
      {   // ugasni rele
         RegTempSwitch(n+1,HIGH);
      }
  }  
  CurrentTime=millis();
  
  if (CurrentTime-PreviousTime<TimePeriod2)    // poglej če je že čas da resetiramo števec
          {
        // ni ne naredi nič
          }     
       else   // reset števca
            {
              PrintValue(2); // izpiši podatke na USB
              PreviousTime=millis();  // prestavi števec na novo vrednost
            }
          
}
      
void PrintValue(int neki) {
  if (neki==1) {
            Serial.print(ADCT[5]);     //izpis 
            Serial.print(" ");
            Serial.print(ADCT[6]);  // izpis temperature
            Serial.print(" ");
            Serial.println(ADCSp[0]);  // izpis PIDa max 255
       } else 
       {
         for (int n=0; n<8; n++) {   
           
           long nek=long(ADCT[n])+10000*(n+1);
           Serial.println(nek); // izpis XYYYY - X0000 senzor + YYYY ADC
           }
       }
}

void Multiplexer(int kateri) {  // dekonvulucija kanalov in senzorjev temperature
  switch(kateri) { 
    case 1:// senzor 1 vodi do kanala 5
        digitalWrite(SetMPA,HIGH);
        digitalWrite(SetMPB,LOW);
        digitalWrite(SetMPC,HIGH);
        break;
    case 2: // senzor 2 vodi do kanala 7
        digitalWrite(SetMPA,HIGH);
        digitalWrite(SetMPB,HIGH);
        digitalWrite(SetMPC,HIGH);
        break;
    case 3: // senzor 3 vodi do kanala 6
        digitalWrite(SetMPA,LOW);
        digitalWrite(SetMPB,HIGH);
        digitalWrite(SetMPC,HIGH);
        break;
     case 4: // senzor 4 vodi do kanala 4
        digitalWrite(SetMPA,LOW);
        digitalWrite(SetMPB,LOW);
        digitalWrite(SetMPC,HIGH);
        break;
     case 5: // senzor 5 vodi do kanala 3
        digitalWrite(SetMPA,HIGH);
        digitalWrite(SetMPB,HIGH);
        digitalWrite(SetMPC,LOW);
        break;
     case 6: // senzor 6 vodi do kanala 0
        digitalWrite(SetMPA,LOW);
        digitalWrite(SetMPB,HIGH);
        digitalWrite(SetMPC,HIGH);
        break;
     case 7: // senzor 7 vodi do kanala 1
        digitalWrite(SetMPA,HIGH);
        digitalWrite(SetMPB,LOW);
        digitalWrite(SetMPC,LOW);
        break;
     case 8:  // senzor 8 vodi do kanala 2
        digitalWrite(SetMPA,LOW);
        digitalWrite(SetMPB,HIGH);
        digitalWrite(SetMPC,LOW);
        break;
    default:
      ;// nič 
  }
}

void RegTempSwitch(int kateri,int on) {  // poveže regulator z pravimi releji
  switch(kateri) {
    case 1: // Regulator 1 - talilec poveže temperaturo senzorja 1 z regulatorjem 1
      digitalWrite(Rele1,on);
      digitalWrite(Rele2,on);
      break;
    case 2: // Regulator 2 - zgornja plošča drugi del poveže Temp. senzor 2 z regulatorjem
      digitalWrite(Rele3,on);
      digitalWrite(Rele4,on);
      break;
    case 3: // Regulator 3 - spodnja plošča, opoveže temperaturni seznor T3 z regulatorjem
      digitalWrite(Rele5,on);
      digitalWrite(Rele6,on);
      break;
    }
}

int Commands(int comm, int param) {
  int RT;
  switch(comm) {
    case 1:  // od ena do 10 so rezervirani ukazi za kalibracijo -> seti prednastavljenih ciljnih vrednosti
      for (int n=0; n<3; n++) {
        ADCSp[n]= 0;
      }    
      break;
    case 2:
      for (int n=0; n<3; n++) {
        ADCSp[n]= 100;
      }
      break;
    case 3:
      for (int n=0; n<3; n++) {
        ADCSp[n]= 300;
      }
    
      break;
    case 5:
      for (int n=0; n<3; n++) {
        ADCSp[n]= 500;
      }
    
      break;
    case 6:
      for (int n=0; n<3; n++) {
        ADCSp[n]= 700;
      }
    
      break;
    case 7:
      for (int n=0; n<3; n++) {
        ADCSp[n]= 900;
      }
    
      break;
    case 10:  // nastavi novo vrednost, ki jo cilja PID na ACDSp
      RT=int(param/10000);
      ADCSp[RT-1]=param-(RT*10000); 
      //Serial.println("#cmd10");
      break;
  }

}

void serialEvent() { // n akoncu loopa ga odpre... nima še kode za error ...
  int command, param;
  
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline process a command
    if (inChar == '\n') {   
      String neki=inputString.substring(0,2);
      String neki2=inputString.substring(2,7);
      //Serial.println(neki);
      //Serial.println(neki2);
      //Serial.println(inputString);
      Commands(neki.toInt(),neki2.toInt());
      inputString="";
    }
  }
}
