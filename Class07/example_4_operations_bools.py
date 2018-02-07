is_waiting = False       # Wird gerne nach der Taetigkeit bezeichnet
has_time = True

# Konditioneller Codeteil, nach if immer ein Bool eingetragen sein
# Interpreter geht von oben nach unten, erste Bedingung
# Einrueckung immer erforderlich wenn Doppelpunkt (4 spaces, oder ein TAB)
if is_waiting:
    print "I am waiting"
    print "I am still waiting"
    print "I am still waiting"
elif not is_waiting and has_time:
    print "I am not waiting and have time"
else:
    print "I am not waiting"
