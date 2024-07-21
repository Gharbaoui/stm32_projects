#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>
#include "../free_rtos_kernel/include/FreeRTOS.h"
#include "../free_rtos_kernel/include/task.h"
// #include <task.h>

int main(void) {
    // rcc_periph_clock_enable(RCC_GPIOA);
    // rcc_periph_clock_enable(RCC_GPIOC);
    // gpio_mode_setup(GPIOC, GPIO_MODE_INPUT, GPIO_PUPD_NONE, GPIO13);
    // gpio_mode_setup(GPIOA, GPIO_MODE_OUTPUT, GPIO_PUPD_PULLDOWN, GPIO5);
    

    // volatile uint16_t read_value = 0;
    // while(1) {
    //     read_value = gpio_get(GPIOC, GPIO13);
    //     if (read_value & GPIO13) {
    //         // means that there's no press
    //         gpio_clear(GPIOA, GPIO5);
    //     } else {
    //         // it means there was press
    //         gpio_set(GPIOA, GPIO5);
    //     }
    // }

    // while(1);
}
