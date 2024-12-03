from services.platform.dexcom_follow import notify_follow
from services.platform.dexcom_clarity import notify_clarity

def process_and_redirect(data):
    """Redirige les données vers Dexcom Follow et Dexcom Clarity."""
    print(f"Plateforme reçoit les données : {data}")
    if data['status'] != 'normal':
        notify_follow(data)
        notify_clarity(data)
