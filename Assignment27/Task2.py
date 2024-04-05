import asyncio
import random

async def delayed_random_print():
    for number in range(1, 11):  # Iterate from 1 to 10
        delay_time = random.uniform(0.5, 2)  # Choose a random delay time between 0.5 to 2 seconds
        await asyncio.sleep(delay_time)      # Delay for the chosen time
        print(number)


asyncio.run(delayed_random_print())
