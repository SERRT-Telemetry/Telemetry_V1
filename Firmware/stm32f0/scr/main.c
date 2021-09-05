#include "stm32f0xx.h"
#include "virtualCom.h"
#include "delay.h"
#include "can.h"


int main(void)
{
  
  int canMessage;
  
  canInit();
  canFilterInit();
  
  while (1)
  {
    
    if ((CAN->RF0R & CAN_RF0R_FMP0)!=0) 
    {
      canMessage = CAN->sFIFOMailBox[0].RDLR; //Read Message
      CAN->RF0R |= CAN_RF0R_RFOM0; 
  
      serialPrint("%X\n\r", canMessage);
      delay(1000);
    }  
  }
  
}
