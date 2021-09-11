#include "stm32f0xx.h"
//Macros
#define BITRATE_500KBIT (0x001c0005UL)

int CAN_ID = 0x6B0;
//Function Prototypes
void canInit(void);
void canFilterInit(void);
