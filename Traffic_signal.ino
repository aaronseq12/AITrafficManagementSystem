//First of all, we define the pins where we have 
//connected the Light emiting diods,
int red_1=13;
int orange_1=12;
int green_1=11;
int red_2=10;
int orange_2=9;
int green_2=8;
int red_3=7;
int orange_3=6;
int green_3=5;
int red_4=4;
int orange_4=3;
int green_4=2;
int LEDState=0;
int LEDPin=1;
int ButtonPin=0;
int ButtonNew;
int ButtonOld=1;

void direction_1_green(void)//green LED of direction 1 will turn ON
{
  digitalWrite(red_1,LOW);
  digitalWrite(orange_1,LOW);
  digitalWrite(green_1,HIGH);
  digitalWrite(red_2,HIGH);
  digitalWrite(orange_2,LOW);
  digitalWrite(green_2,LOW);
  digitalWrite(red_3,HIGH);
  digitalWrite(orange_3,LOW);
  digitalWrite(green_3,LOW);
  digitalWrite(red_4,HIGH);
  digitalWrite(orange_4,LOW);
  digitalWrite(green_4,LOW);
}

void direction_2_orange(void)//orange LED of direction 2 will turn ON
{
  digitalWrite(red_1,HIGH);
  digitalWrite(orange_1,LOW);
  digitalWrite(green_1,LOW);
  digitalWrite(red_2,LOW);
  digitalWrite(orange_2,HIGH);
  digitalWrite(green_2,LOW);
  digitalWrite(red_3,HIGH);
  digitalWrite(orange_3,LOW);
  digitalWrite(green_3,LOW);
  digitalWrite(red_4,HIGH);
  digitalWrite(orange_4,LOW);
  digitalWrite(green_4,LOW);
}

void direction_2_green(void)//green LED of direction 2 will turn ON
{
  digitalWrite(red_1,HIGH);
  digitalWrite(orange_1,LOW);
  digitalWrite(green_1,LOW);
  digitalWrite(red_2,LOW);
  digitalWrite(orange_2,LOW);
  digitalWrite(green_2,HIGH);
  digitalWrite(red_3,HIGH);
  digitalWrite(orange_3,LOW);
  digitalWrite(green_3,LOW);
  digitalWrite(red_4,HIGH);
  digitalWrite(orange_4,LOW);
  digitalWrite(green_4,LOW);
}

void direction_3_orange(void)//orange LED of direction 3 will turn ON
{
  digitalWrite(red_1,HIGH);
  digitalWrite(orange_1,LOW);
  digitalWrite(green_1,LOW);
  digitalWrite(red_2,HIGH);
  digitalWrite(orange_2,LOW);
  digitalWrite(green_2,LOW);
  digitalWrite(red_3,LOW);
  digitalWrite(orange_3,HIGH);
  digitalWrite(green_3,LOW);
  digitalWrite(red_4,HIGH);
  digitalWrite(orange_4,LOW);
  digitalWrite(green_4,LOW);
}

void direction_3_green(void)//green LED of direction 3 will turn ON
{
  digitalWrite(red_1,HIGH);
  digitalWrite(orange_1,LOW);
  digitalWrite(green_1,LOW);
  digitalWrite(red_2,HIGH);
  digitalWrite(orange_2,LOW);
  digitalWrite(green_2,LOW);
  digitalWrite(red_3,LOW);
  digitalWrite(orange_3,LOW);
  digitalWrite(green_3,HIGH);
  digitalWrite(red_4,HIGH);
  digitalWrite(orange_4,LOW);
  digitalWrite(green_4,LOW);
}

void direction_4_orange(void)//orange LED of direction 4 will turn ON
{
  digitalWrite(red_1,HIGH);
  digitalWrite(orange_1,LOW);
  digitalWrite(green_1,LOW);
  digitalWrite(red_2,HIGH);
  digitalWrite(orange_2,LOW);
  digitalWrite(green_2,LOW);
  digitalWrite(red_3,HIGH);
  digitalWrite(orange_3,LOW);
  digitalWrite(green_3,LOW);
  digitalWrite(red_4,LOW);
  digitalWrite(orange_4,HIGH);
  digitalWrite(green_4,LOW);
}

void direction_4_green(void)//green LED of direction 4 will turn ON
{
  digitalWrite(red_1,HIGH);
  digitalWrite(orange_1,LOW);
  digitalWrite(green_1,LOW);
  digitalWrite(red_2,HIGH);
  digitalWrite(orange_2,LOW);
  digitalWrite(green_2,LOW);
  digitalWrite(red_3,HIGH);
  digitalWrite(orange_3,LOW);
  digitalWrite(green_3,LOW);
  digitalWrite(red_4,LOW);
  digitalWrite(orange_4,LOW);
  digitalWrite(green_4,HIGH);
}

void direction_1_orange(void)//orange LED of direction 1 will turn ON
{
  digitalWrite(red_1,LOW);
  digitalWrite(orange_1,HIGH);
  digitalWrite(green_1,LOW);
  digitalWrite(red_2,HIGH);
  digitalWrite(orange_2,LOW);
  digitalWrite(green_2,LOW);
  digitalWrite(red_3,HIGH);
  digitalWrite(orange_3,LOW);
  digitalWrite(green_3,LOW);
  digitalWrite(red_4,HIGH);
  digitalWrite(orange_4,LOW);
  digitalWrite(green_4,LOW);
}

void pedestrian(void){
  ButtonNew=digitalRead(ButtonPin);
  if (ButtonOld==0 && ButtonNew==1){
    if (LEDState==0){
      digitalWrite(LEDPin,HIGH);
      LEDState=1;
    }
    else{
      digitalWrite(LEDPin,LOW);
      LEDState=0;
    }
  }
}

void setup() { // Declaring all the LED's as output
  for(int i=1;i<=13;i++){
    pinMode(i,OUTPUT);
  }
  pinMode(ButtonPin,INPUT);
}

void loop() //In the loop function, we controlled the signal one by one to control the flow of traffic.
{
  direction_1_green();
  delay(5000);
  direction_2_orange();
  delay(3000);
  direction_2_green();
  delay(5000);
  direction_3_orange();
  delay(3000);
  direction_3_green();
  delay(5000);
  direction_4_orange();
  delay(3000);
  direction_4_green();
  delay(5000);
  direction_1_orange();
  delay(3000);
}
