rooms = [
  {
     'room_id': 1,
     'periods': [
        {
           'time': '17:00-18:00',
           'status': 'available'
        },
        {
           'time': '16:00-17:00',
           'status': 'available'
        },
        {
           'time': '18:00-19:00',
           'status': 'occupied'
        }
     ]
  }, {
     'room_id': 2,
     'periods': [
        {
           'time': '17:00-18:00',
           'status': 'occupied'
        },
        {
           'time': '18:00-19:00',
           'status': 'available'
        }
     ]
  }
]

from pipe import *

def ealiest_avaiable_period(room):
  return {'room_id': room['room_id'], 'time': sorted(room['periods'] | where(lambda p: p['status'] == 'available'), key=lambda p: p['time'])[0]['time']}

print sorted(rooms | select(ealiest_avaiable_period), key=lambda x: x['time'])[0]
