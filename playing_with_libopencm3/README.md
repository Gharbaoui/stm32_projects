### libopencm3 setup

by the way this is just for me when I'll work with libopencm3 with stm32f446re, so I'm not always
looking for setup again and again so I'll setup it once and when I ever want project I'll just copy it
to my local machine, I'll explain how to get started with stm32f446re as example if you did not understand
that's okay because it's not intended to, refer to the original one

##### Steps
1. get libopencm3-template
```
git clone --recursive https://github.com/libopencm3/libopencm3-template.git project_name
```

2. navigate to libopencm3 and run make
```sh
cd libopencm3
make
```

3. navigate to my-project
you could change the project name, I have no assembly for now so I just removed them and set my
board 'stm32f446re'
```
PROJECT = blink
BUILD_DIR = bin

CFILES = my-project.c

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
```
