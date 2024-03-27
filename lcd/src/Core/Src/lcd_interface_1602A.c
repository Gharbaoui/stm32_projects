#include "lcd_interface_1602A.h"

extern I2C_HandleTypeDef hi2c1;

static uint8_t backlight_state = BACKLIGHT_ON;

//static void DelayUS(uint32_t us) {
//  uint32_t cycles = (SystemCoreClock/1000000L)*us;
//  uint32_t start = DWT->CYCCNT;
//  volatile uint32_t cnt;
//
//  do
//  {
//    cnt = DWT->CYCCNT - start;
//  } while(cnt < cycles);
//}

void transmit_wrapper(uint8_t data)
{
	HAL_I2C_Master_Transmit(&hi2c1, DEVICE_ADDRESS, &data, 1, 100);
}

void write_data(uint8_t data)
{
//	transmit_wrapper(data);
//	HAL_Delay(1);
//	pulse_E_line(data);

	transmit_wrapper(data | ENABLE_PIN_ON); // setting E pin to high
	HAL_Delay(1); // E line is high for 1ms which is enough
	transmit_wrapper(data & ENABLE_PIN_OFF);
	HAL_Delay(1);
}

//void pulse_E_line(uint8_t data)
//{
//	transmit_wrapper(data | ENABLE_PIN_ON); // setting E pin to high
//	HAL_Delay(1); // E line is high for 1ms which is enough
//	transmit_wrapper(data & ENABLE_PIN_OFF);
//	HAL_Delay(1);
//}

void send_word(uint8_t w, uint8_t rs)
{
	uint8_t high_part = w & 0xf0;
	uint8_t low_part = (w << 4) & 0xf0;
	write_data(high_part | rs | backlight_state);
	HAL_Delay(1);
	write_data(low_part | rs | backlight_state);
	HAL_Delay(1);
}

void toggle_backlight(void)
{
	if (backlight_state == BACKLIGHT_0FF)
		backlight_state = BACKLIGHT_ON;
	else
		backlight_state = BACKLIGHT_0FF;

	transmit_wrapper(backlight_state);
}

void lcd_config(void)
{
	// function set with 2 lines and 5x10 dots for the font
	send_word(0b00011100, 0);
	// clear display
	send_word(0b00000001, 0);
	// return home
	send_word(0b00000010, 0);
	// display on/off control
	send_word(0b00001111, 0);
}

void set_cursor_to_line(uint8_t line_number)
{
	// maybe a check later value should be 0 or 1 that's it
	if (line_number == 1)
		send_word(0b11000000, 0);
	else
		send_word(0b10000000, 0);
}


void send_char(char c)
{
	send_word((uint8_t)c, 1);
}

void send_string(const char *str)
{
	while (*str != 0)
	{
		send_char(*str);
		++str;
	}
}
