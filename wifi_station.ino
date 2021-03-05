#include <WebServer.h>
#include <WiFi.h>
#include <WiFiUdp.h>

//set up to connect to an existing network (e.g. mobile hotspot from laptop that will run the python code)
const char* ssid = "********";  // insert wifi network 
const char* password = "********";  // insert wifi password 
WiFiUDP Udp;
unsigned int localUdpPort = 4210;  //  port to listen on
char incomingPacket[255];  // buffer for incoming packets

void setup()
{
  pinMode(25, INPUT_PULLUP);
  pinMode(18, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(23, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(22, INPUT_PULLUP);
  pinMode(13, INPUT_PULLUP);
  pinMode(27, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  
  int status = WL_IDLE_STATUS;
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to wifi");
  Udp.begin(localUdpPort);
  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);

  // we recv one packet from the remote so we can know its IP and port
  bool readPacket = false;
  while (!readPacket) {
    int packetSize = Udp.parsePacket();
    if (packetSize)
     {
      // receive incoming UDP packets
      Serial.printf("Received %d bytes from %s, port %d\n", packetSize, Udp.remoteIP().toString().c_str(), Udp.remotePort());
      int len = Udp.read(incomingPacket, 255);
      if (len > 0)
      {
        incomingPacket[len] = 0;
      }
      Serial.printf("UDP packet contents: %s\n", incomingPacket);
      readPacket = true;
    } 
  }
}

void loop()
{
  int c = digitalRead(25);
  int d = digitalRead(23);
  int e = digitalRead(12);
  int f = digitalRead(13);
  int g = digitalRead(18);
  int a = digitalRead(4);
  int b = digitalRead(5);
  int switchPlay = digitalRead(27);
  int switchSharp = digitalRead(22);
  
  // once we know where we got the inital packet from, send data back to that IP address and port
  Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());

  Udp.printf("%d%d%d%d%d%d%d%d%d", c, d, e, f, g, a, b, switchPlay, switchSharp);
  Udp.endPacket();
  delay(1000);
}
