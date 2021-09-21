// https://github.com/ChuckBell/MySQL_Connector_Arduino/wiki/Examples#connect-by-hostname-connect_by_hostnameino

#include <HTTPClient.h>
#include <MySQL_Connection.h>
#include <MySQL_Cursor.h>
#include <WiFi.h>

// Known Networks
const char* apa = "C-Net";
const char* apaPW = "mustang5";

const char* casa = "Machinest";
const char* casaPW = "Magicalairplane7691";

const char* rum = "RUMNET";
const char* rumPW = "Colegio2019";

const char* ssidList[] = { apa, casa, rum };
const char* pwList[] = { apaPW, casaPW, rumPW };

byte mac_addr[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

IPAddress server_addr(127, 0, 0, 1); // IP of the MySQL *server* here
char user[] = "telemetry"; // MySQL user login username
char password[] = "solarpower"; // MySQL user login password

// Sample query
char INSERT_DATA[] = "INSERT INTO test_arduino.hello_sensor (message, sensor_num, value) VALUES ('%s',%d,%s)";
char query[128];
char temperature[10];

EthernetClient client;
MySQL_Connection conn((Client*)&client);

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        ; // wait for serial port to connect
    
    Serial.print("Connecting to ");
    Serial.println(rum);

    WiFi.begin(rum, rumPW);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
    
    Serial.println("Connecting...");
    if (conn.connect(server_addr, 3306, user, password)) {
        delay(1000);
        // Initiate the query class instance
        MySQL_Cursor* cur_mem = new MySQL_Cursor(&conn);
        // Save
        dtostrf(50.125, 1, 1, temperature);
        sprintf(query, INSERT_DATA, "test sensor", 24, temperature);
        // Execute the query
        cur_mem->execute(query);
        // Note: since there are no results, we do not need to read any data
        // Deleting the cursor also frees up memory used
        delete cur_mem;
        Serial.println("Data recorded.");
    } else
        Serial.println("Connection failed.");
    conn.close();
}

void loop() { }