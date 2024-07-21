#include <stdint.h>

void usart_setup(void);
void uart_write_byte(uint8_t data);
void uart_write(const uint8_t *data, uint32_t length);