from config import dp
from handlers import (
    start,
    questionnaire
    questionnaire,
    chat_actions
)
from database import sql_commands

@@ -14,6 +15,7 @@ async def on_startup(_):

start.register_start_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
chat_actions.register_chat_actions_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(