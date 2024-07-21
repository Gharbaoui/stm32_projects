#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>
#include "gpio.h"

void gpio_setup(void)
{
  rcc_periph_clock_enable(RCC_GPIOA);
  
  gpio_mode_setup(GPIOA, GPIO_MODE_AF, GPIO_PUPD_PULLUP, GPIO2);
  gpio_set_af(GPIOA, GPIO_AF7, GPIO2);
}