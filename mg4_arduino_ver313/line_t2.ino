void line_t(){
    const int threshold = 1;
    // 起動10秒でモーターを停止する
    //if(millis() < 10000){}
 
    // 左のセンサーの値
    int line_foto_get_l = digitalRead(10)  ;  
    // 右のセンサーの値
    int line_foto_get_r = digitalRead(13)  ;  
        
    digitalWrite(8, HIGH);
    digitalWrite(12, LOW);
    
    // 直進
    if(line_foto_get_l == threshold && line_foto_get_r == threshold){
      digitalWrite(8, HIGH);
      digitalWrite(12, LOW); 
      analogWrite(9, 100);
      analogWrite(11, 100);    
    // 左へ  
    }else if(line_foto_get_l <= threshold && line_foto_get_r == threshold){
      digitalWrite(8, HIGH);
      digitalWrite(12, LOW); 
      analogWrite(9, 100);
      analogWrite(11, 50);
    // 右へ  
    }else if(line_foto_get_r <= threshold && line_foto_get_l == threshold){
      digitalWrite(8, HIGH);
      digitalWrite(12, LOW);
      analogWrite(9, 50);
      analogWrite(11, 100); 
    }
  else{
    // モーターの完全停止
    digitalWrite(8, LOW);
    digitalWrite(12, LOW);   
    analogWrite(9, 0);
    analogWrite(11, 0);
  }
  //モータの動作を1続ける 0.05=50 1 5=5000
  delay(50);
}

void line_fot_get() {
    Serial.begin(9600) ;

 // 左のセンサーの値
    int line_foto_get_l = digitalRead(10)  ;  
 // 右のセンサーの値
    int line_foto_get_r = digitalRead(13)  ;   
    while(1) {
         if (digitalRead(10) == 1 && digitalRead(13) == 1){
         Serial.println("ryouhouhannnousiteru");
         delay (1000);
      } 
         else if (digitalRead(10) == 1 && digitalRead(13) != 1){
         Serial.println("hidari");
         delay (1000);
      } 
         else if (digitalRead(10) != 1 && digitalRead(13) == 1){
         Serial.println("migi");
         delay (1000);
      } 
         else{
         Serial.println("mazika");
         delay (1000);
      } 
      
  }
}
