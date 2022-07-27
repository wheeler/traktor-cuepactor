from traktor_nml_utils import TraktorCollection
from pathlib import Path

from util import are_cues_in_order_time, are_cues_in_order_hot, hotcues_have_gaps

# collection = TraktorCollection(Path('test_jul_24_collection.nml'))
collection = TraktorCollection(Path('test.nml'))

info = {'count': 0, 'out_of_order_count': 0, 'gap_count': 0}

for entry in collection.nml.collection.entry:
    if not are_cues_in_order_time(entry.cue_v2):
        info['out_of_order_count'] += 1
        print(info['count'], entry.artist, entry.title, 'cues are not in order (start)')
    elif not are_cues_in_order_hot(entry.cue_v2):
        info['out_of_order_count'] += 1
        print(info['count'], entry.artist, entry.title, 'cues are not in order (hotcue #)', [x.hotcue for x in entry.cue_v2])
    elif hotcues_have_gaps(entry.cue_v2):
        info['gap_count'] += 1
        print(info['count'], entry.artist, entry.title, 'hotcues are have a gap', [x.hotcue for x in entry.cue_v2])
    info['count'] += 1

print('info', info)
print('---')
