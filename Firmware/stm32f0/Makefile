#-------------------------------------------------------------------------
#Linux/MacOS Makefile
#-------------------------------------------------------------------------
INSTALL_DIR  = ~
#-------------------------------------------------------------------------
#Compiler Config
#-------------------------------------------------------------------------
CC           = $(INSTALL_DIR)/gcc-arm-none-eabi-9-2019-q4-major/bin/arm-none-eabi-g++
CFLAGS       = -Iinc -O0 -Wall -Werror -pedantic -g
M0           = -mthumb -mcpu=cortex-m0
LFLAGS       = -TSTM32F072VB_FLASH.ld 
USE_NONHOST  = --specs=nosys.specs

#-------------------------------------------------------------------------
#CProject Config
#-------------------------------------------------------------------------

NAME         = firmware
SCRDIR       = scr
OBJECTS      = main.o system_stm32f0xx.o stm32f0xx_it.o delay.o can.o virtualCom.o  startup_stm32f072.s

#-------------------------------------------------------------------------
#Targets
#-------------------------------------------------------------------------

all: $(NAME).elf

.PHONY: debug
debug:	
	$(INSTALL_DIR)/gcc-arm-none-eabi-9-2019-q4-major/bin/arm-none-eabi-gdb $(NAME).elf

.PHONY: clean
clean:
	@rm *.o *.elf 

#-------------------------------------------------------------------------
#Target Rules
#-------------------------------------------------------------------------

%.o : $(SCRDIR)/%.c
	@$(CC) $(M0) $(CFLAGS) -o $@ -c $<

$(NAME).elf : $(OBJECTS)
	@$(CC) $(M0) $(USE_NONHOST) $(LFLAGS) -o $@ $^


