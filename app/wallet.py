from app.database_lib import *

def usdt_new_wallet():
    wallet = random_string(40)
    secrets = "{} {} {} {} {} {} {}".format(random_string(5), random_string(5), random_string(5), random_string(5), random_string(5), random_string(5), random_string(5))
    return wallet, secrets