#include "uart.h"

void uartEnable(void)
{
  //Enable GPIOA PA9      
  RCC->AHBENR |= RCC_AHBENR_GPIOAEN;                  //Enable clock for GPIOA
  GPIOA->MODER |= GPIO_MODER_MODER9_1;                //Set PA9 to alternate function 
  GPIOA->AFR[1] |= 0x10;                              //Set PA9 to USART1
  
  //Enable USART1 TX
  RCC->APB2ENR |= RCC_APB2ENR_USART1EN;               //Enable clock for USART1
  USART1->BRR = 0x1388;                               //Set baudrate to 9.6kbit/sec
  USART1->CR1 |= USART_CR1_UE | USART_CR1_TE;         //Enable USART1 TX

}

