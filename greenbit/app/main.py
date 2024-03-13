from faker import Faker
from DB.core_crud import AsyncCore
from DB.orm_crud import AsyncOrm
import asyncio


def get_user_data():
    fake = Faker()
    while True:
        data = {
            "user_name": fake.first_name(),
            "email": fake.email(),
            "password": fake.password(),
        }
        yield data


user_data = get_user_data()


async def main():
    await AsyncOrm.create_tables()
    await AsyncOrm.insert_user_auth(data=next(user_data))


if __name__ == "__main__":
    asyncio.run(main())
