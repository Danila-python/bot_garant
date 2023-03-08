from data.db.base import Base, Users as UserDB
from data.db.base import get_session

async def post(message):
    async with get_session() as session:
        user_db = UserDB(
            user_id=message.for_user_id
        )
