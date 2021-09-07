#include "stm32f0xx.h"
#include "virtualCom.h"
#include "delay.h"
#include "can.h"

int main(void)
{ 

  int canMessage =0;

  delayInit();
  serialPrintInit();
  canInit();
  canFilterInit();
  
  while (1)
  {

    if ((CAN->RF0R & CAN_RF0R_FMP0)!=0) 
    {
      canMessage = CAN->sFIFOMailBox[0].RDLR; //Read Message
      CAN->RF0R |= CAN_RF0R_RFOM0; 
  
      serialPrint("Msg:%X\n\r", canMessage);
      delay(1000);
    } 
    else
    {
      serialPrint("No Msg\n\r");
      delay(1000);
    }
  
  }
}

/* 
int main(void)
{
  
  //int canMessage =0;
  
  //canInit();
  //canFilterInit();
  
  while (1)
  {
    serialPrint("Test\n\r");
    delay(1000);

    if ((CAN->RF0R & CAN_RF0R_FMP0)!=0) 
    {
      canMessage = CAN->sFIFOMailBox[0].RDLR; //Read Message
      CAN->RF0R |= CAN_RF0R_RFOM0; 
  
      serialPrint("Msg:%X\n\r", canMessage);
      delay(1000);
    } 
    
  }
  
}
*/