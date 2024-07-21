#include <FreeRTOS.h>
#include <libopencm3/stm32/gpio.h>
#include <libopencm3/stm32/rcc.h>
#include <task.h>

static void task1(void *args __attribute((unused))) {
  for (;;) {
    gpio_toggle(GPIOC, GPIO13);
    vTaskDelay(pdMS_TO_TICKS(1500));
  }
}

static void task2(void *args __attribute((unused))) {
  for (;;) {
    vTaskDelay(pdMS_TO_TICKS(1000));
    gpio_toggle(GPIOC, GPIO14);
  }
}

void system_setup(void);

int main(void) {
  // rcc_clock_setup_pll(&rcc_hse_16mhz_3v3[RCC_CLOCK_3V3_168MHZ]);
  rcc_clock_setup_pll(&rcc_hse_25mhz_3v3[RCC_CLOCK_3V3_84MHZ]);

  system_setup();
  xTaskCreate(task1, "Task1", 1000, (void *)(configMAX_PRIORITIES - 1), 1,
              NULL);
  xTaskCreate(task2, "Task2", 1000, (void *)(configMAX_PRIORITIES - 1), 1,
              NULL);

  vTaskStartScheduler();

  while (1) {
    __asm("nop");
  }
}
