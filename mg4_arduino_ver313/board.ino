#include "CytronMotorDriver.h"
CytronMD motor(PWM_DIR, 5, 6);

void motorboard_u(){
  pinMode(PIN_PWM_UD,OUTPUT);
  pinMode(PIN_DIR_UD,OUTPUT);
//  if(digitalRead(10) == 0 && digitalRead(13) == 0){
    motor.setSpeed(30);
/*  }else{
    motor.setSpeed(0);
  }*/
}

void motorboard_s(){
  pinMode(PIN_PWM_UD,OUTPUT);
  pinMode(PIN_DIR_UD,OUTPUT);
    motor.setSpeed(0);
}

void motorboard_d(){
  pinMode(PIN_PWM_UD,OUTPUT);
  pinMode(PIN_DIR_UD,OUTPUT);
  if(digitalRead(SIG_L) == 0 && digitalRead(SIG_R) == 0){
    motor.setSpeed(-220);
  }else{
    motor.setSpeed(0);
  }
}


  
