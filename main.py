import time
from plyer import notification
if __name__=='__main__':
	while(1):
		notification.notify(
			title ="Please Drink Water Now!!",
			message ="Drinking water at regular intervals is essential for a healthy body.An adult must consume 6lt of water everyday.",
			timeout=10,
		)
		time.sleep(60*60)