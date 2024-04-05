import asyncio

async def task_with_delay_2():
    print("Task with 2-second delay started.")
    await asyncio.sleep(2)
    print("Task with 2-second delay finished.")

async def task_with_delay_5():
    print("Task with 5-second delay started.")
    await asyncio.sleep(5)
    print("Task with 5-second delay finished.")

async def main():
    # Create tasks
    task1 = asyncio.create_task(task_with_delay_2())
    task2 = asyncio.create_task(task_with_delay_5())

    # Wait for the tasks to complete
    await task1
    await task2

# Run the main function
asyncio.run(main())
