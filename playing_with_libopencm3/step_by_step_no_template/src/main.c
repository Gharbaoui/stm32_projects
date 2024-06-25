#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>
#include <FreeRTOS.h>
#include <task.h>

static void task1(void *args __attribute((unused))) {
    for(;;) {
        gpio_toggle(GPIOA, GPIO5);
        __asm("nop");
        vTaskDelay(pdMS_TO_TICKS(1500));
    }
}

void system_setup(void);

int main(void) {
    rcc_clock_setup_pll(&rcc_hse_16mhz_3v3[RCC_CLOCK_3V3_168MHZ]);

    system_setup();
    xTaskCreate(task1, "Task1", 1000, (void*)(configMAX_PRIORITIES-1), 1, NULL);

    vTaskStartScheduler();


    while(1) {
        __asm("nop");
    }
}
