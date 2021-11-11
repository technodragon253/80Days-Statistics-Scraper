import json
import message_handler
from message_handler import Channel
from constants import *
mh = message_handler.main()
if __name__ == "__main__":
    mh.debug = True

import loading_animation
l = loading_animation.loading_animation()
l.start()  

payments = []
sabotages = []

dates = mh.retrieve_game_dates(progress_anouncements)

payments.append(mh.retrieve_payments(wolves_commands))
payments.append(mh.retrieve_payments(wolves_general))
payments.append(mh.retrieve_payments(stallions_commands))
payments.append(mh.retrieve_payments(stallions_general))
payments.append(mh.retrieve_payments(boars_commands))
payments.append(mh.retrieve_payments(boars_general))

sabotages.append(mh.retrieve_sabotages(wolves_commands))
sabotages.append(mh.retrieve_sabotages(wolves_general))
sabotages.append(mh.retrieve_sabotages(stallions_commands))
sabotages.append(mh.retrieve_sabotages(stallions_general))
sabotages.append(mh.retrieve_sabotages(boars_commands))
sabotages.append(mh.retrieve_sabotages(boars_general))


with open("output.json", "w") as f:
    s = [s.__dict__() for sabo in sabotages for s in sabo]
    print(s)
    s.sort(key=lambda obj: obj["time"])
    p = [p.__dict__() for payment in payments for p in payment]
    print(p)
    p.sort(key=lambda obj: obj["time"])
    out = {
        "start_dates": dates,
        "sabotages": s,
        "payments": p
    }

    json.dump(out, f, indent=4)

l.stop()
