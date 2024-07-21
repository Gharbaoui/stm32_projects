#include <FreeRTOS.h>
#include <libopencm3/cm3/nvic.h>
#include <libopencm3/stm32/exti.h>
#include <libopencm3/stm32/gpio.h>
#include <libopencm3/stm32/rcc.h>
#include <task.h>

// static void task1(void *args __attribute((unused))) {
//     for(;;) {
//         gpio_toggle(GPIOA, GPIO5);
//         __asm("nop");
//         vTaskDelay(pdMS_TO_TICKS(1500));
//     }
// }

// void system_setup(void);

int main(void) {
  // clock setup
  rcc_clock_setup_pll(&rcc_hse_16mhz_3v3[RCC_CLOCK_3V3_168MHZ]);
  rcc_periph_clock_enable(RCC_GPIOA);
  gpio_mode_setup(GPIOA, GPIO_MODE_OUTPUT, GPIO_PUPD_PULLDOWN, GPIO5);

  // gpio setup
  rcc_periph_clock_enable(RCC_GPIOC);
  rcc_periph_clock_enable(RCC_SYSCFG);
  gpio_mode_setup(GPIOC, GPIO_MODE_INPUT, GPIO_PUPD_NONE, GPIO13);

  exti_enable_request(EXTI13);                    // maybe INPUTS ??
  exti_set_trigger(EXTI13, EXTI_TRIGGER_FALLING); // maybe INPUTS ??
  exti_select_source(
      EXTI13, GPIOC); // making the EXIT controller work with the right I/O pin

  nvic_enable_irq(NVIC_EXTI15_10_IRQ);

  while (1) {
    __asm("nop");
  }
}

void exti15_10_isr(void) {
  // maybe the handler
  if (exti_get_flag_status(EXTI13)) {
    gpio_toggle(GPIOA, GPIO5);
    exti_reset_request(EXTI13);
  }
}
