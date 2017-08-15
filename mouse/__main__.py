# -*- coding: utf-8 -*-
import mouse
import fileinput
import json
import sys

class_by_name = {
	'ButtonEvent': mouse.ButtonEvent,
	'WheelEvent': mouse.WheelEvent,
	'MoveEvent': mouse.MoveEvent,
}

def print_event_json(event):
	# Could use json.dumps(event.__dict__()), but this way we guarantee semantic order.
	d = event._asdict()
	d['event_class'] = event.__class__.__name__
	print(json.dumps(d))
	sys.stdout.flush()
mouse.hook(print_event_json)

def load(line):
	d = json.loads(line)
	class_ = class_by_name[d['event_class']]
	del d['event_class']
	return class_(**d)

mouse.play(load(line) for line in fileinput.input())