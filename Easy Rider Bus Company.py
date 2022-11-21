import datetime
import json
import re

json_load = json.loads(input())

lines_stops = dict()

lines_stop_types = dict()

stops = dict()

stop_times = dict()

errors = dict(
    bus_id=0,
    stop_id=0,
    stop_name=0,
    next_stop=0,
    stop_type=0,
    a_time=0
)

errors_format = dict(
    stop_name=0,
    stop_type=0,
    a_time=0
)

field_type = dict(
    bus_id=int,
    stop_id=int,
    stop_name=str,
    next_stop=int,
    stop_type=str,
    a_time=str
)

required_field = dict(
    bus_id=False,
    stop_id=True,
    stop_name=False,
    next_stop=True,
    stop_type=True,
    a_time=False
)

field_options = dict(
    bus_id=None,
    stop_id=None,
    stop_name=None,
    next_stop=None,
    stop_type=['', 'S', 'O', 'F'],
    a_time=None
)

field_format = dict(
    bus_id=False,
    stop_id=False,
    stop_name=True,
    next_stop=False,
    stop_type=True,
    a_time=True
)

for item in json_load:
    if not isinstance(item, dict):
        continue
    for key, value in item.items():
        if any([
            not isinstance(value, field_type.get(key)),
            not value and not required_field.get(key),
            field_options.get(key) and value not in field_options.get(key)
        ]):
            errors[key] += 1

print(f'Type and required field validation: {sum(errors.values())} errors')
for key, value in errors.items():
    print(f'{key}: {value}')

for item in json_load:
    if not isinstance(item, dict):
        continue
    for key, value in item.items():
        if any([
            key == 'stop_name' and not re.search('^[A-Z].*(Road|Avenue|Boulevard|Street)$',value),
            key == 'stop_type' and value not in field_options.get(key),
            key == 'a_time' and not re.search('^[0-2][0-9]:[0-5][0-9]$', value)
        ]):
            errors_format[key] += 1

print(f'Format validation: {sum(errors_format.values())} errors')
for key, value in errors_format.items():
    print(f'{key}: {value}')

for item in json_load:
    if not isinstance(item, dict):
        continue
    id = item['bus_id']
    if lines_stops.get(id):
        lines_stops[id] += 1
    else:
        lines_stops[id] = 1

print('Line names and number of stops:')
for key, value in lines_stops.items():
    print(f'bus_id: {key}, stops: {value}')

for item in json_load:
    if not isinstance(item, dict):
        continue
    id = item['bus_id']
    stop = item["stop_type"]
    if lines_stop_types.get(id):
        lines_stop_types[id].append(stop)
    else:
        lines_stop_types[id] = [stop]

for key, value in lines_stop_types.items():
    F = [i for i, val in enumerate(value) if val == 'F']
    S = [i for i, val in enumerate(value) if val == 'S']
    if len(F) != 1 or len(S) != 1:
        print(f'There is no start or end stop for the line: {key}.')
        exit()

all_stops, start_stops, transfer_stops, finish_stops, demand_stops = [], [], [], [], []
for item in json_load:
    all_stops.append(item["stop_name"])
    if item["stop_type"] == "S":
        start_stops.append(item["stop_name"])
    elif item["stop_type"] == "F":
        finish_stops.append(item["stop_name"])
    elif item["stop_type"] == 'O':
        demand_stops.append(item["stop_name"])


for stop in all_stops:
    if all_stops.count(stop) > 1:
        transfer_stops.append(stop)

transfer_stops = sorted(set(transfer_stops))
demand_stops = sorted(set(demand_stops))
start_stops = sorted(set(start_stops))
finish_stops = sorted(set(finish_stops))

print("Start stops:", len(start_stops), start_stops)
print("Transfer stops:", len(transfer_stops), transfer_stops)
print("Finish stops:", len(finish_stops), finish_stops)

buffer = ''
skip = []

for item in json_load:
    if not isinstance(item, dict):
        continue
    id = item['bus_id']
    time = item['a_time']
    station = item['stop_name']
    if stop_times.get(id) and id not in skip:
        current_station_time = datetime.datetime.strptime(time, '%H:%M')
        previous_station_time = datetime.datetime.strptime(stop_times[id], '%H:%M')
        if current_station_time < previous_station_time:
            buffer = buffer + f'bus_id line {id}: wrong time on station {station}\n'
            skip.append(id)
        else:
            stop_times[id] = time
    else:
        stop_times[id] = time

print('Arrival time test:')
if buffer == '':
    print('OK')
else:
    print(buffer)

inter = sorted(set(transfer_stops).intersection((demand_stops)))
print('On demand stops test:')
if len(inter) > 0:
    print(inter)
else:
    print('OK')
