int LED1 = 43;
int LED2 = 47;
int trigPin = 36;
int echoPin = 37;
int incomingByte = 0;
String stringOne="";
#include <AFMotor.h> 
#include <Servo.h> 

// DC motor on M2
AF_DCMotor motor(1);
// DC hobby servo
Servo servo1;
Servo servo2;
void setup() {
  
   Serial.begin(9600); 

  //initialises servo

   servo1.attach(9);
  servo2.attach(10);
  servo1.write(0);
  servo2.write(0);
   
  // turn on dc motor 
  motor.setSpeed(150);
  motor.run(RELEASE);

   pinMode(LED1,OUTPUT);
    pinMode(LED2,OUTPUT);  
   pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
   Serial.flush();
}
int i=1;
byte inpt=0,inp2=0;
int pos;
//void loop()
//{
//  for (int j=39;j<=50;j++){
//      digitalWrite(j,HIGH);
//    }
//
//    delay(5000);
//  //digitalWrite(LED1,HIGH);
//  //digitalWrite(LED2,HIGH);
//  
//}

void loop() {



//        while(1) {
//      long duration, distance;
//      digitalWrite(trigPin,HIGH);
//      delayMicroseconds(1000);
//      digitalWrite(trigPin, LOW);
//      duration=pulseIn(echoPin, HIGH);
//      distance =(duration/2)/29.1;
//      if (distance<=6){
//      Serial.print(distance);
//      Serial.println("  cm");
//      }
////      if(distance<=6){
////        Serial.write("a");
////        digitalWrite(LED1,HIGH);
////        motor.run(RELEASE);
////        //Serial.println("CM");
////        delay(2000);
////        Serial.flush();
////        break;
//      }
//      delay(30);
//}
 
  while(1){
       motor.run(FORWARD);
       
 
      digitalWrite(LED1,HIGH);
      digitalWrite(LED2,HIGH);
      delay(1000);
      digitalWrite(LED1,LOW);
      digitalWrite(LED2,LOW);
      //delay(1000);
    
      
      stringOne="";
      //Serial.println("loop start-");
      while(1) {
      long duration, distance;
      digitalWrite(trigPin,HIGH);
      delayMicroseconds(1000);
      digitalWrite(trigPin, LOW);
      duration=pulseIn(echoPin, HIGH);
      distance =(duration/2)/29.1;
      
      if(distance<=6){
        Serial.write("a");
        digitalWrite(LED1,HIGH);
        motor.run(RELEASE);
        //Serial.println("CM");
        delay(2000);
        Serial.flush();
        break;
      }
      delay(5);
      }
      
      digitalWrite(LED1,LOW);
      digitalWrite(LED2,LOW);
      //Serial.println("waiting here");
      
      while(1){
        
      while (!Serial.available() ){
      }
      int a = Serial.read();
      if (a == 1){
      for (pos = 0; pos <= 60; pos += 1) { 
          servo1.write(pos);              // tell servo to go to position in variable 'pos'
          delay(15);                       // waits 15ms for the servo to reach the position
      }
       digitalWrite(LED1,HIGH);
      }
      
      else if (a == 2){
        for (pos = 0; pos <= 60; pos += 1) { 
          servo2.write(pos);              // tell servo to go to position in variable 'pos'
          delay(15);                       // waits 15ms for the servo to reach the position
      }
       digitalWrite(LED2,HIGH);
      }
      else 
      {
        digitalWrite(LED1,HIGH);
        digitalWrite(LED2,HIGH);
        //Serial.flush();
        //continue;
        delay(15);
      }

      motor.run(FORWARD);

      delay(3000);
      i++;
      
      digitalWrite(LED1,HIGH);
      digitalWrite(LED2,HIGH);


      if (a== 1)
      {
        for (pos = 60; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
          servo1.write(pos);              // teMll servo to go to position in variable 'pos'
          delay(15);                       // waits 15ms for the servo to reach the position
        }
        
      }

      if (a== 2)
      {
        for (pos = 60; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
          servo2.write(pos);              // teMll servo to go to position in variable 'pos'
          delay(15);                       // waits 15ms for the servo to reach the position
        }
        
      }
      
      digitalWrite(LED1,LOW);
      digitalWrite(LED2,LOW);
      delay(1000);
      Serial.flush();// sets the LED off
      break;
      } 

  }
}
