import uasyncio as asyncio

# Initialize the onboard LED

async def flash_led(led, frequency, task, duration=None):
    # Cancel the previous task if it exists
    if task is not None:
        task.cancel()

    period = 1 / frequency
    end_time = asyncio.get_event_loop().time() + duration if duration else None

    async def flash():
        while end_time is None or asyncio.get_event_loop().time() < end_time:
            led.toggle()
            await asyncio.sleep(period / 2)
        led.off()

    return asyncio.create_task(flash())