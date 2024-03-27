#pragma once
#include "stm32f4xx_hal.h"

#define DEVICE_ADDRESS 0x27 << 1
#define ENABLE_PIN_ON 0b00000100
#define ENABLE_PIN_OFF 0b11111011
#define BACKLIGHT_ON 0b00001000
#define BACKLIGHT_0FF 0b00000000

void transmit_wrapper(uint8_t data);
void write_data(uint8_t data);
void send_word(uint8_t w, uint8_t rs);
void toggle_backlight(void);
void lcd_config(void);
void set_cursor_to_line(uint8_t line_number);
void send_char(char c);
void send_string(const char *str);
