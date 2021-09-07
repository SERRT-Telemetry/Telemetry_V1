#include "can.h"

void canInit(void)
{

  //Enable GPIOD
  RCC->AHBENR |= RCC_AHBENR_GPIOBEN;                //Enable GPIOB Clock
  GPIOB->MODER |= GPIO_MODER_MODER8_1;              //Set PB.8 to Alternate Function Mode
  GPIOB->MODER |= GPIO_MODER_MODER9_1;              //Set PB.9 to Alternate Function Mode
  GPIOB->AFR[1] |= 0x4;                             //Set PB.8 to AF4
  GPIOB->AFR[1] |= 0x4 << 4;                        //Set PB.9 to AF4
  //Enable bxCAN Tx/Rx
  RCC->APB1ENR |= RCC_APB1ENR_CANEN;                //Enable CAN clock
  CAN->MCR |= CAN_MCR_INRQ;                         //Enter Initialization 
  while((CAN->MSR & CAN_MSR_INAK) != CAN_MSR_INAK); 
  CAN->BTR |= BITRATE_500KBIT;                                        
  CAN->MCR &= ~CAN_MCR_INRQ;                        //Enter Normal Mode
  while((CAN->MSR & CAN_MSR_INAK) == CAN_MSR_INAK);      

}

void canFilterInit(void)
{

  //Configure Filters
  CAN->FMR |= CAN_FMR_FINIT;                        //Initializa CAN Filter
  CAN->FA1R |= CAN_FA1R_FACT0;                      //Call filter 0
  CAN->FS1R |= CAN_FS1R_FSC0;                       //Select Dual 32 bit Filters
  CAN->FM1R &= ~CAN_FM1R_FBM0;                      //Set Filter to Identifier Mask, if not running switch to Identifier list
  
  CAN->sFilterRegister[0].FR1 = 0x6B0FFFFF;          //ID
  CAN->sFilterRegister[0].FR2 = 0xFFFFFFFFUL;       //???Filter
  CAN->FMR &= ~CAN_FMR_FINIT;                       //Finish Configuring filter

}