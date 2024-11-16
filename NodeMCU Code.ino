#define BLYNK_PRINT Serial


#define BLYNK_TEMPLATE_ID "TMPL68CcrAfCy"
#define BLYNK_TEMPLATE_NAME "Control DC Motor"
#define BLYNK_AUTH_TOKEN "CXWjPxWhRTGkyq8rO1_CL7ZiRsnc-VtS"

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

 
char auth[] = BLYNK_AUTH_TOKEN;

char ssid[] = "SCIENCE";  // type your wifi name
char pass[] = "hehehehe";  // type your wifi password
 
int M1PWM = D5;
int M2PWM = D6;
int M1F = D1; //GPIO5
int M1R = D2; //GPIO4
int M2F = D3; //GPIO0

int pinValue1;
int pinValue2;

BLYNK_WRITE(V1)
{
  int pinValue1 = param.asInt();
  analogWrite(M1PWM,pinValue1);
  Blynk.virtualWrite(V1,pinValue1);
  Serial.print("V1 Slider Value is ");
  Serial.println(pinValue1);
}

BLYNK_WRITE(V2)
{
  int pinValue2 = param.asInt();
  analogWrite(M2PWM,pinValue2);
  Blynk.virtualWrite(V1,pinValue2);
  Serial.print("V2 Slider Value is ");
  Serial.println(pinValue2);
}
 

void setup(){
  pinMode(M1PWM, OUTPUT);
  pinMode(M2PWM, OUTPUT);
  pinMode(M1F, OUTPUT);
  pinMode(M1R, OUTPUT);
  pinMode(M2F, OUTPUT);
  Serial.begin(9600);
  Blynk.begin(auth,ssid,pass);
  
}

void loop(){
  Blynk.run();
 
}