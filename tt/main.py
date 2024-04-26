from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get(
    "gotJ9saaxKFFpbPa4JlIDhQIHE9UIptge09DCku0V2ZBurbCN6Hskdr-2DNmPDSELuB9uTMqIC1wgQSeWsaVyd5G1nLjy1U_FJ43EoBY2H9tI47Zjts5jBYwEJlQXDu-AZ34uXI=",
)  # set your own ms_token, think it might need to have visited a profile


async def user_example():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3,headless=False)
        user = api.user(username="shivani_dhall18nov")
        user_data = await user.info()
        print(user_data)

        async for video in user.videos(count=30):
            print(video)
            print(video.as_dict)


if __name__ == "__main__":
    task=asyncio.run(user_example())

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(task)