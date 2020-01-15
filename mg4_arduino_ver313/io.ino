void io_open() {
  pinMode(PIN_BATT, INPUT);
  digitalWrite(PIN_BATT, LOW);
}

double io_get_batt() {
  return analogRead(PIN_BATT) * 5.0 / 1024.0 / V_RATIO;
}
