import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print("world")

async def main():
    print(f"started at {time.strftime('%X')}")

    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1

    print("hello")


    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
