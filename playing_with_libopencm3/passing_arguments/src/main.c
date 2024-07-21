#include <FreeRTOS.h>
#include <libopencm3/stm32/gpio.h>
#include <libopencm3/stm32/rcc.h>
#include <task.h>

// 47:26

typedef struct {
  uint32_t gpio_port;
  uint16_t gpio_pin;
  uint16_t delay;
} GPIO_PARAMS;


volatile GPIO_PARAMS pin1 = {
  .gpio_port = GPIOA,
  .gpio_pin = GPIO5,
  .delay = 1500U
};
volatile GPIO_PARAMS pin2 = {
  .gpio_port = GPIOA,
  .gpio_pin = GPIO6,
  .delay = 1000U
};


static void task1(void *args) {
  volatile GPIO_PARAMS l = *((volatile GPIO_PARAMS*)args);
  for (;;) {
    gpio_toggle(l.gpio_port, l.gpio_pin);
    
    vTaskDelay(pdMS_TO_TICKS(l.delay));
  }
}

void system_setup(void);

int main(void) {
  rcc_clock_setup_pll(&rcc_hse_16mhz_3v3[RCC_CLOCK_3V3_168MHZ]);
  system_setup();


  if (xTaskCreate(task1, "Task1", 1000, &pin1, 1, NULL) != pdPASS) {
    gpio_toggle(GPIOA, GPIO5);
  }
  
  if (xTaskCreate(task1, "Task2", 1000, &pin2, 2, NULL) != pdPASS) {
    gpio_toggle(GPIOA, GPIO5);
  }

  vTaskStartScheduler();

  while (1) {
    __asm("nop");
  }
}
