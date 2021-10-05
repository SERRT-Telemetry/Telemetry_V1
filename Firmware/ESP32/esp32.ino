// https://github.com/ChuckBell/MySQL_Connector_Arduino/wiki/Examples#connect-by-hostname-connect_by_hostnameino
// https://blog.devgenius.io/visual-studio-code-arduino-configuration-and-import-solution-a5f188a0cfd0

#include <Dns.h>
#include <Ethernet.h>
#include <HTTPClient.h>
#include <MySQL_Connection.h>
#include <MySQL_Cursor.h>
#include <WiFi.h>
#include <SPI.h>
#include <WiFiNINA.h>

// Known Networks
const char* apa = "ADTRAN_2.4G GHz_1EAC";
const char* apaPW = "IytRdMeo";

const char* casa = "Machinest";
const char* casaPW = "Magicalairplane7691";

const char* rum = "RUMNET";
const char* rumPW = "Colegio2019";

const char* ssidList[] = { apa, casa, rum };
const char* pwList[] = { apaPW, casaPW, rumPW };

const char* ssid = apa;
const char* password = apaPW;

void initWiFi()
{
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    Serial.print("\nConnecting to WiFi ..");
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print('.');
        delay(1000);
    }
    Serial.println("\nConnected to WiFi with IP: " + WiFi.localIP());
}

char hostname[] = "serrt-database.c7sgroillrv6.us-east-2.rds.amazonaws.com"; // change to your server's hostname/URL
char user[] = "admin"; // MySQL user login username
char dbPassword[] = "Solarpower802"; // MySQL user login password
char database[] = "sensor_data"; // MySQL database name

IPAddress server_ip;
WiFiClient client;
MySQL_Connection conn((Client*)&client);

void setup()
{
    Serial.begin(115200);

    while (!Serial)
        ; // wait for serial port to connect

    initWiFi();

    // Begin DNS lookup
    WiFi.hostByName(hostname, server_ip);
    Serial.println("\nHostname sesolved to IP Adress: " + server_ip);
    // End DNS lookup

    Serial.println("\nConnecting to databse...");

    if (conn.connect(server_ip, 3306, user, dbPassword, database)) {
        delay(1000);
        // You would add your code here to run a query once on startup.
        Serial.println("\nSuccesfully connected to database!");
    } else {
        Serial.println("\nConnection failed.");
    }
    conn.close();
}

void loop() { }
