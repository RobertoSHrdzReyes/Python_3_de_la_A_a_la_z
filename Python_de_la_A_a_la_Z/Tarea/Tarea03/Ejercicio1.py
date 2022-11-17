
title = "se busca tripulante"
message = "se ofrece puesto en la tripulación del capitán pyratilla para llevar a cabo labores de marinero. comida y bebida garantizada a lo largo de toda la aventura."
contact = "para más información, ir al puerto y buscar al capitán pyratilla, ya famoso en este pueblo costero (evitar preguntar en el casino)."

title = title.upper()

message1 = message.split(". ")
message1[0] = message1[0].capitalize()
message1[1] = message1[1].capitalize()
message = message1[0] + ". " + message1[1]
message = message[:47] + message[47:56].upper() + message[56:]

contact = contact.capitalize()
contact = contact[:55] + contact[55:64].upper() + contact[64:]

print("{}\n{}\n{}".format(title, message, contact))