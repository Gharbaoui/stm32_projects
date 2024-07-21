#include "./core/inc/system.h"
#include "./core/inc/timer.h"

int main(void) {
    system_setup();
    timer_setup();
    uint64_t start_time = get_ticks();
    float duty_cycle = 0.0f;
    bool going_up = false;
    timer_pwm_set_duty_cycle(duty_cycle);
    while (1) {
        if (get_ticks() - start_time >= 10) {
            if (going_up) {
                duty_cycle += 1.0f;
                if (duty_cycle > 100.0f)
                {
                    duty_cycle = 100.0f;
                    going_up = false;
                }
            } else {
                duty_cycle -= 1.0f;
                if (duty_cycle < 0.0f) {
                    duty_cycle = 0;
                    going_up = true;
                }
            }

            timer_pwm_set_duty_cycle(duty_cycle);
            start_time = get_ticks();
        }
        // other work
    }
}
