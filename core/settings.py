from environs import Env

env = Env()
env.read_env()

OPENAI_API_KEY = env.str('OPENAI_API_KEY')
GOOGLE_API_KEY = env.str('GOOGLE_API_KEY')
GOOGLE_CSE_ID = env.str('GOOGLE_CSE_ID')
USE_CHAT_GPT = env.bool('USE_CHAT_GPT', True)
USE_FREE_CHAT_GPT = env.bool('USE_FREE_CHAT_GPT', True)
