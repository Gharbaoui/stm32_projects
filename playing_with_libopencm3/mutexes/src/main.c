#include <FreeRTOS.h>
#include <libopencm3/stm32/rcc.h>
#include <task.h>
#include <semphr.h>
#include "gpio.h"
#include "uart.h"
#include <stdio.h>
#include <string.h>

#include "SEGGER_RTT.h"

volatile uint32_t sharedResource;

void incrmenetTask(void *args __attribute((unused))) {
  while(1) {
    SEGGER_RTT_printf(0, "%lu\n\r", sharedResource);
    vTaskDelay(pdMS_TO_TICKS(3));
    ++sharedResource;
  }
}

void stopTask(void *args __attribute((unused))) {
  vTaskDelay(pdMS_TO_TICKS(5000));
  vTaskEndScheduler();
}

int main(void) {
  rcc_clock_setup_pll(&rcc_hsi_configs[RCC_CLOCK_3V3_180MHZ]);

  SEGGER_RTT_Init();
  SEGGER_RTT_ConfigUpBuffer(0, NULL, NULL, 0, SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL);
  sharedResource = 0;
  
  xTaskCreate(incrmenetTask, "task-1", 100, NULL, 2, NULL);
  xTaskCreate(incrmenetTask, "task-2", 100, NULL, 2, NULL);
  xTaskCreate(incrmenetTask, "task-3", 100, NULL, 2, NULL);

  xTaskCreate(stopTask, "done", 50, NULL, 1, NULL);

  vTaskStartScheduler();

  while (1) {

    __asm("nop");
  }
}
