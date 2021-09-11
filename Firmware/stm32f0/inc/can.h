#include "stm32f0xx.h"
//Macros
#define BITRATE_500KBIT (0x001c0005UL)

//Function Prototypes
void canInit(void);
void canFilterInit(void);
