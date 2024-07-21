#include "../inc/system.h"

static volatile uint64_t ticks = 0;

void sys_tick_handler(void) {
    ++ticks; 
}

uint64_t get_ticks(void) {
    return ticks;
}

static void clock_setup(void) {
    rcc_clock_setup_pll(&rcc_hsi_configs[RCC_CLOCK_3V3_84MHZ]);
}

static void gpio_setup(void) {
    rcc_periph_clock_enable(RCC_GPIOA);
    gpio_mode_setup(GPIOA, GPIO_MODE_AF, GPIO_PUPD_NONE, GPIO5);
    gpio_set_af(GPIOA, GPIO_AF1, GPIO5);
}

static void systick_setup(void) {
    systick_set_frequency(SYSTICK_FREQ, CPU_FREQ);
    systick_counter_enable();
    systick_interrupt_enable();
}


void system_setup(void) {
    clock_setup();
    gpio_setup();
    systick_setup();
}