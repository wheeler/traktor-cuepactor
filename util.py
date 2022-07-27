def are_cues_in_order_time(cue_list):
    prev = -1
    for cue in cue_list:
        current = cue.start
        if current < prev:
            return False
        prev = current
    return True

def are_cues_in_order_hot(cue_list):
    prev = -1
    for cue in cue_list:
        current = cue.hotcue
        if current < prev:
            return False
        prev = current
    return True

def hotcues_have_gaps(cue_list):
    expected = 0
    for cue in cue_list:
        current = cue.hotcue
        if current != expected:
            return True
        expected += 1
    return False
