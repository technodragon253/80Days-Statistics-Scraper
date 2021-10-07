import json
from message_handler import retrieve_payments, Channel, retrieve_sabotages, retrieve_game_dates

import loading_animation
l = loading_animation.loading_animation()
l.start()  

payments = []
sabotages = []

progress_anouncements = Channel("614336214786375682", "Progress Anouncements", "Anouncements")
wolves_general = Channel("614345822477352974", "Wolves General", "Azure Wolves")
wolves_commands = Channel("614350640264511508", "Wolves Commands", "Azure Wolves")
stallions_general = Channel("614345873463443457", "Stallions General", "Crimson Stallions")
stallions_commands = Channel("614503418299547661", "Stallions Commands", "Crimson Stallions")
boars_general = Channel("614345791133188096", "Boars General", "Argent Boars")
boars_commands = Channel("614350341344985098", "Boars Commands", "Argent Boars")

dates = retrieve_game_dates(progress_anouncements)

payments.append(retrieve_payments(wolves_commands))
payments.append(retrieve_payments(wolves_general))
payments.append(retrieve_payments(stallions_commands))
payments.append(retrieve_payments(stallions_general))
payments.append(retrieve_payments(boars_commands))
payments.append(retrieve_payments(boars_general))

sabotages.append(retrieve_sabotages(wolves_commands))
sabotages.append(retrieve_sabotages(wolves_general))
sabotages.append(retrieve_sabotages(stallions_commands))
sabotages.append(retrieve_sabotages(stallions_general))
sabotages.append(retrieve_sabotages(boars_commands))
sabotages.append(retrieve_sabotages(boars_general))


with open("output.json", "w") as f:
    s = [s.to_dict() for sabo in sabotages for s in sabo]
    s.sort(key=lambda obj: obj["time"])
    p = [p.to_dict() for payment in payments for p in payment]
    p.sort(key=lambda obj: obj["time"])
    out = {
        "start_dates": dates,
        "sabotages": s,
        "payments": p
    }

    json.dump(out, f, indent=4)
