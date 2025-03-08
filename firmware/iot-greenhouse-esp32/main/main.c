#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "driver/gpio.h"

void app_main(void)
{
  while (1)
  {
    printf("Tick\n");

    vTaskDelay(1000 / portTICK_PERIOD_MS);
    fflush(stdout);
  }
}