#include "hal_data.h"

FSP_CPP_HEADER
void R_BSP_WarmStart(bsp_warm_start_event_t event);
FSP_CPP_FOOTER

/* Callback function */
int return_sig = 0, stop_sig = 0;
void irq4_callback(external_irq_callback_args_t *p_args)
{
    /* TODO: add your own code here */
    return_sig = 1;
}

/* Callback function */
void irq5_callback(external_irq_callback_args_t *p_args)
{
    /* TODO: add your own code here */
    stop_sig = !stop_sig;
}

int flag[4] = {0,};
void DFS(int depth){
    if (return_sig == 1) return;
    while (stop_sig == 1) {
        if (stop_sig == 0) break;
        R_BSP_SoftwareDelay(100, BSP_DELAY_UNITS_MILLISECONDS);
    }

    if (depth == 4) {
        R_IOPORT_PinWrite(&g_ioport_ctrl, LEDr, flag[0]);
        R_IOPORT_PinWrite(&g_ioport_ctrl, LEDy, flag[1]);
        R_IOPORT_PinWrite(&g_ioport_ctrl, LEDg, flag[2]);
        R_IOPORT_PinWrite(&g_ioport_ctrl, LEDb, flag[3]);

        R_BSP_SoftwareDelay(300, BSP_DELAY_UNITS_MILLISECONDS);

        return;
    }
    for (int i = 0; i < 2; i++) {
        flag[depth] = i;
        DFS(depth+1);
        if (return_sig == 1) return;
    }
}

/*******************************************************************************************************************//**
 * main() is generated by the RA Configuration editor and is used to generate threads if an RTOS is used.  This function
 * is called by main() when no RTOS is used.
 **********************************************************************************************************************/
void hal_entry(void)
{
    /* TODO: add your own code here */
    R_ICU_ExternalIrqEnable(&g_external_irq4_ctrl);
    R_ICU_ExternalIrqEnable(&g_external_irq5_ctrl);

    while(1) {
        while (stop_sig == 1) {
            if (return_sig == 1) {
                stop_sig = 0;
                break;
            }
        }
        DFS(0);
        if (return_sig == 1) {
            return_sig = 0;
            continue;
        }
        else {
            stop_sig = 1;
        }
    }


}

/*******************************************************************************************************************//**
 * This function is called at various points during the startup process.  This implementation uses the event that is
 * called right before main() to set up the pins.
 *
 * @param[in]  event    Where at in the start up process the code is currently at
 **********************************************************************************************************************/
void R_BSP_WarmStart(bsp_warm_start_event_t event)
{
    if (BSP_WARM_START_RESET == event)
    {

    }

    if (BSP_WARM_START_POST_C == event)
    {
        /* C runtime environment and system clocks are setup. */

        /* Configure pins. */
        R_IOPORT_Open (&IOPORT_CFG_CTRL, &IOPORT_CFG_NAME);
        R_ICU_ExternalIrqOpen(&g_external_irq4_ctrl, &g_external_irq4_cfg);
        R_ICU_ExternalIrqOpen(&g_external_irq5_ctrl, &g_external_irq5_cfg);


    }
}

