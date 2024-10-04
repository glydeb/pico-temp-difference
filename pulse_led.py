import uasyncio as asyncio

# Initialize the onboard LED

async def pulse_led(led, frequency, task, duration=None):
    # Cancel the previous task if it exists
    if task is not None:
        task.cancel()

    period = 1 / frequency
    end_time = asyncio.get_event_loop().time() + duration if duration else None

    async def pulse():
        while end_time is None or asyncio.get_event_loop().time() < end_time:
            for i in range(100):
                led.duty_u16(int(65535 * (i / 100)))
                await asyncio.sleep(period / 200)
            for i in range(100, -1, -1):
                led.duty_u16(int(65535 * (i / 100)))
                await asyncio.sleep(period / 200)
        led.off()

    return asyncio.create_task(pulse())
