#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>

void system_setup(void);

int main(void) {
    system_setup();    

    volatile uint16_t read_value = 0;
    while(1) {
        read_value = gpio_get(GPIOC, GPIO13);
        if (read_value & GPIO13) {
            // means that there's no press
            gpio_set(GPIOA, GPIO5);
        } else {
            // it means there was press
            gpio_clear(GPIOA, GPIO5);
        }
    }

    while(1) {
        __asm("nop");
    }
}
