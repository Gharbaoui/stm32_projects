#ifndef __SYSTEM_H__
#define __SYSTEM_H__

#include <stdint.h>
#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>
#include <libopencm3/cm3/systick.h>
#include <libopencm3/cm3/vector.h>

#define CPU_FREQ 84000000
#define SYSTICK_FREQ 1000

#define CPU_FREQ 84000000
#define SYSTICK_FREQ 1000
uint64_t get_ticks(void);

void system_setup(void);
#endif