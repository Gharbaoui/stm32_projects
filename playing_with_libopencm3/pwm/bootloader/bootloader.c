#include <stdint.h>
#include <stdbool.h>


// 0x08000000 + 32Kb = 0x8008000 so this the start of our frimware
// first 4 bytes are for the stack pointer, and the second are
// the location of the reset_handler
// 0x8008000 + 0x4 = 0x8008004
#define RESET_HANDLER_POSITION (0x8008004)

static void branch_to_main(void) {
    typedef void (*void_func)(void);

    void_func jump_fn = (void_func)RESET_HANDLER_POSITION;

    jump_fn();
}

int main(void) {
    
    branch_to_main();

}
