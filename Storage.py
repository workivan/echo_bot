import asyncpg


class Storage:
    connection = None

    async def init(self, db_url):
        self.connection = await asyncpg.connect(db_url)

    async def add_sub(self, chat_id):
        await self.connection.execute(
            f"""update "user" set is_connected=true where chat_id={chat_id}""")
