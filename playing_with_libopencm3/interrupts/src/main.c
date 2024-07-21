#include <libopencm3/cm3/systick.h>
#include <libopencm3/cm3/vector.h>
#include <libopencm3/stm32/gpio.h>
#include <libopencm3/stm32/rcc.h>

#define CPU_FREQ 84000000
#define SYSTICK_FREQ 1000

volatile uint64_t ticks = 0;
void sys_tick_handler(void) { ++ticks; }
static uint64_t get_ticks(void) { return ticks; }

static void systick_setup(void) {
  systick_set_frequency(SYSTICK_FREQ, CPU_FREQ);
  systick_counter_enable();
  // how does the systick timer let's know what is happening interrupts
  systick_interrupt_enable();
}

int main(void) {
  // rcc_clock_setup_pll(&rcc_hsi_configs[RCC_CLOCK_3V3_84MHZ]);
  // rcc_periph_clock_enable(RCC_GPIOA);
  // gpio_mode_setup(GPIOA, GPIO_MODE_OUTPUT, GPIO_PUPD_PULLDOWN, GPIO5);
  // systick_setup();
  //
  // uint64_t start_time = get_ticks();
  // while (1) {
  //   if (get_ticks() - start_time >= 1000) {
  //     gpio_toggle(GPIOA, GPIO5);
  //     start_time = get_ticks();
  //   }
  //   // other work
  // }
}
