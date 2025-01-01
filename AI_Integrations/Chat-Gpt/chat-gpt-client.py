from dotenv import load_dotenv
import os
load_dotenv()


SBR_WEBDRIVER = os.getenv("chat_gpt_api")
print(SBR_WEBDRIVER)