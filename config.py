# En este archivo configuramos todas las variables de usuario

# Token del bot de Telegram
# https://core.telegram.org/bots#how-do-i-create-a-bot
telegram_token="5857390887:AAEaf7YKD08h5z01vc3lrsqBckohMxQmNnU"
# Los IDs de telegram de los usuarios que responderá el bot
# Talk to @userinfobot bot on telegram to get yours
telegram_users=[5198110160]

# Activar o no la opción de envío de notas de voz
voice_enabled = True

# Modo de conectarnos a openai, mediante la web con usuario y contraseña (web)
# o mediante la API con una clave (api) que tiene un coste asociado
# el modo web es normalmente más lento y puede saturarse, pero recuerda las conversaciones
openai_mode = "api"

# Usuario y contraseña de OpenIA (no funcional ya)
openai_email = "electricalengineeringdev@gmail.com"
openai_password = "taherdev1999&%@"
# Cookie y token de sesión
openai_session = "XXXX"
openai_clearance = "XXXX"
openai_useragent = "XXXX"

# API de OpenAI (solo si el modo de openai es 'api')
# https://beta.openai.com/account/api-keys
openai_api_key = "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"

# Claves y servidor de AWS para Amazon polly
# https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/security_credentials
aws_access_key_id="XXXX"
aws_secret_access_key="XXXX"
region_name="eu-west-3"

# Configuración y API de Stability.ia
sd_engine_id = "stable-diffusion-512-v2-0"
sd_api_host = "https://api.stability.ai"
sd_api_key = "sk-aNay2jF9UCqG3MBvuG3CIudvK6ES3CWBDnRzcLzF3w93VWY7"
