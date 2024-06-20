PROJECT?=main

SRCDIRECTORY=src
PREFIX = arm-none-eabi

LIBOPENCM3_PATH := ./deps/libopencm3
BUILD_DIR ?= build

SOURCE_FILES = $(wildcard $(SRCDIRECTORY)/*.c)
OBJFILES = $(patsubst $(SRCDIRECTORY)/%.c, $(BUILD_DIR)/%.o, $(SOURCE_FILES))
GENRATED_FILES += $(OBJFILES) $(patsubst $(BUILD_DIR)/%.o, $(BUILD_DIR)/%.d, $(OBJFILES))

all: $(BUILD_DIR)/$(PROJECT).elf

# building all the object files
$(BUILD_DIR)/%.o: $(SRCDIRECTORY)/%.c
	$(PREFIX)-gcc -Os -ggdb3 -mcpu=cortex-m4 -mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16 \
	-fno-common -ffunction-sections -fdata-sections -Wextra -Wshadow -Wno-unused-variable \
	-Wimplicit-function-declaration -Wredundant-decls -Wstrict-prototypes -Wmissing-prototypes \
	-MD -Wall -Wundef -I$(LIBOPENCM3_PATH)/include -DSTM32F4 -DSTM32F446RE -o $@ -c $<


# linking with libopencm3
$(BUILD_DIR)/$(PROJECT).elf: $(OBJFILES)
	$(PREFIX)-gcc -Tstm32f446re.ld -L$(LIBOPENCM3_PATH)/lib -nostartfiles -mcpu=cortex-m4 \
	-mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16 -specs=nano.specs -Wl,--gc-sections -Wl,--cref \
	-Wl,-Map=$(BUILD_DIR)/$(PROJECT).map -L../libopencm3/lib $(OBJFILES)   -lopencm3_stm32f4 -Wl,--start-group \
	-lc -lgcc -lnosys -Wl,--end-group -o $@
	$(PREFIX)-objcopy -Obinary $(BUILD_DIR)/$(PROJECT).elf $(BUILD_DIR)/$(PROJECT).bin

GENRATED_FILES += $(BUILD_DIR)/$(PROJECT).elf $(BUILD_DIR)/$(PROJECT).map

clean:
	rm -f $(GENRATED_FILES)