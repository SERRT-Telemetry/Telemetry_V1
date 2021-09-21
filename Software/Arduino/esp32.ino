/*
  Rui Santos
  Complete project details at https://RandomNerdTutorials.com/esp32-esp8266-mysql-database-php/

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files.

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

*/

#ifdef ESP32
#include <WiFi.h>
#include <HTTPClient.h>
#else
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#endif

#include <Wire.h>

//Known Networks
const char* apa = "C-Net";
const char* apaPW = "mustang5";

const char* casa = "Machinest";
const char* casaPW = "Magicalairplane7691";

const char* rum = "RUMNET";
const char* rumPW = "Colegio2019";

const char* ssidList[] = {apa, casa, rum};
const char* pwList[] = {apaPW, casaPW, rumPW};

// REPLACE with your Domain name and URL path or IP address with path
const char* serverName = "http://serrt.great-site.net/post-esp-data.php"; //"http://esp32-serrt.000webhostapp.com/post-esp-data.php";

// Keep this API Key value to be compatible with the PHP code provided in the project page.
// If you change the apiKeyValue value, the PHP file /post-esp-data.php also needs to have the same key
String apiKeyValue = "tPmAT5Ab3j7F9";

String sensorName = "Speedometer";
String sensorLocation = "Car";

int msg;

void setup() {
  Serial.begin(115200);
  Serial.println("Scanning for known networks...");

//  // WiFi.scanNetworks will return the number of networks found
//  int n = WiFi.scanNetworks();
//  const char* ssid;
//  const char* password;
//  const char* temp;
//
//  for (int i = 0; i < n; ++i) {
//    Serial.println(WiFi.SSID(i));
//    for (int j = 0; j < sizeof(ssidList); j++) {
//      temp = WiFi.SSID(i).c_str();
//      if (temp == ssidList[j]) {
//        ssid = ssidList[j];
//        password = pwList[j];
//        Serial.println("Known wifi found: " + String(ssid));
//        break;
//      }
//    }
//  }
//
//  if (ssid == NULL) {
//    Serial.println("No known networks were found.");
//  }

  Serial.println("Trying to connect to " + String(rum) + "...");
  WiFi.begin(rum, rumPW);
  Serial.println("Connecting...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());

  Serial2.begin(9600, SERIAL_8N1, 16, 17);
}

void loop() {
  //Check WiFi connection status
  if (WiFi.status() == WL_CONNECTED) {
    WiFiClient client;
    HTTPClient http;

    msg = Serial2.read();

    // Your Domain name with URL path or IP address with path
    http.begin(client, serverName);

    // Specify content-type header
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");

    // Prepare your HTTP POST request data
    String httpRequestData = "api_key=" + apiKeyValue + "&sensor=" + sensorName
                             + "&location=" + sensorLocation + "&value1=" + String(msg);
    Serial.print("httpRequestData: ");
    Serial.println(httpRequestData);

    // You can comment the httpRequestData variable above
    // then, use the httpRequestData variable below (for testing purposes without the BME280 sensor)
    //String httpRequestData = "api_key=tPmAT5Ab3j7F9&sensor=BME280&location=Office&value1=24.75&value2=49.54&value3=1005.14";

    // Send HTTP POST request
    int httpResponseCode = http.POST(httpRequestData);

    // If you need an HTTP request with a content type: text/plain
    //http.addHeader("Content-Type", "text/plain");
    //int httpResponseCode = http.POST("Hello, World!");

    // If you need an HTTP request with a content type: application/json, use the following:
    //http.addHeader("Content-Type", "application/json");
    //int httpResponseCode = http.POST("{\"value1\":\"19\",\"value2\":\"67\",\"value3\":\"78\"}");

    if (httpResponseCode > 0) {
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
    }
    else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
    }
    // Free resources
    http.end();
  }
  else {
    Serial.println("WiFi Disconnected");
  }
  //Send an HTTP POST request every 30 seconds
  delay(30000);
}