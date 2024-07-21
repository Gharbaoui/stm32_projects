PROJECT = pwm
BUILD_DIR = bin

# CFILES = main.c core/src/system.c core/src/timer.c
CFILES = main.c core/src/timer.c core/src/system.c

# TODO - you will need to edit these two lines!
DEVICE=stm32f446re
OOCD_FILE = board/STM32F446RE.cfg

# You shouldn't have to edit anything below here.
VPATH += $(SHARED_DIR)
INCLUDES += $(patsubst %,-I%, . $(SHARED_DIR))
OPENCM3_DIR=../libopencm3

include $(OPENCM3_DIR)/mk/genlink-config.mk
include ../rules.mk
include $(OPENCM3_DIR)/mk/genlink-rules.mk
