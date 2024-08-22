#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "Akhilesh";       
const char* password = "@Nukisu1234"; 

const char* udpAddress = "192.168.1.41"; 
const unsigned int udpPort = 4210;

WiFiUDP udp;

void setup() { 
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  IPAddress myip = WiFi.localIP();
  Serial.println(myip); 
  udp.begin(udpPort);
}

void loop() { 
  int adcValue = analogRead(A0);
 
  char packetBuffer[8];
  itoa(adcValue, packetBuffer, 10);
  udp.beginPacket(udpAddress, udpPort);
  udp.write(packetBuffer);
  udp.endPacket(); 
  delay(1);
}