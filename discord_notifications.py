from discord_webhooks import DiscordWebhooks


def notify(status: str, time: str, target_name: str = None):
    with open("config.txt", "r") as f:
        l = f.readlines()
        WEBHOOK_URL = l[9].replace("\n", "")
    webhook = DiscordWebhooks(WEBHOOK_URL)
    webhook.set_footer(text="--Abhimanyu Sharma")
    if status == "login-success":
        webhook.set_content(title="Login Success!", description="Here's Your Report With :heart:")
        webhook.add_field(name="Time", value=str(time))
    if status == "login-failed":
        webhook.set_content(title="Login Failed!", description="Here's Your Report With :heart:")
        webhook.add_field(name="Time", value=str(time))
    if status == "message-sent":
        webhook.set_content(title="Message Sent!", description="Here's Your Report With :heart:")
        webhook.add_field(name="Time", value=str(time))
        webhook.add_field(name="Target's Name", value=str(target_name))
    if status == "found-target":
        webhook.set_content(title="Found Target", description="Here's Your Report With :heart:")
        webhook.add_field(name="Time", value=str(time))
    if status == "target-not-found":
        webhook.set_content(title="Target Not Found", description="Here's Your Report With :heart:")
        webhook.add_field(name="Time", value=str(time))
        webhook.add_field(name="Provided Username", value=str(target_name))
    if status == "shuttingdown-pc":
        webhook.set_content(title="Shutting Down Your PC", description="Here's Your Report With :heart:")
        webhook.add_field(name="Time", value=str(time))
    webhook.send()
