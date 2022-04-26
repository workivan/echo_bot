import asyncpg

from Pack import Pack
from payment import Payment


class Storage:
    connection = None

    async def init(self, db_url):
        self.connection = await asyncpg.connect(db_url)

    async def add_sub(self, chat_id):
        await self.connection.execute(
            f"""update "user" set is_connected=true where chat_id={chat_id}""")

    async def get_pays(self, chat_id):
        rows = await self.connection.fetch(f"""select * from "payment" where chat_id={chat_id} and send=false""")
        return [Payment(row) for row in rows if row is not None]

    async def get_pack_by_path(self, path):
        row = await self.connection.fetchrow(f"""select * from "pack" where path='{path}' """)
        return Pack(row) if row else None

    async def update_pay(self, chat_id, product):
        await self.connection.execute(f"""update "payment" set send=true where chat_id={chat_id} and product='{product}'""")

