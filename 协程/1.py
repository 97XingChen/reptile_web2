import asyncio
async def execute(x):
    print('Number:',x)

croutine = execute(1)

task=asyncio.ensure_future(croutine)
print(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(task)
# print(croutine)
# loop=asyncio.get_event_loop()
# # loop.run_until_complete(croutine)
# task = loop.create_task(croutine)
# print(task)
# loop.run_until_complete(task)
# print(task)