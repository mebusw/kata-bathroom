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

only_ava_rooms = [
  {
     'room_id': 1,
     'periods': [
     ]
  }, {
     'room_id': 2,
     'periods': [
        {
           'time': '18:00-19:00',
           'status': 'available'
        }
     ]
  }
]

no_ava_rooms = [
  {
     'room_id': 1,
     'periods': [
     ]
  }
]

from pipe import *

# def ealiest_avaiable_period(room):
#   return {'room_id': room['room_id'], 
#           'time': sorted( \
#             room['periods'] | \
#               where(lambda p: p['status'] == 'available'), key=lambda p: p['time']) | \
#             select(lambda p: p['time']) | \
#             first('N/A')}

def ealiest_avaiable_period(room):
  return {'room_id': room['room_id'], 
          'time': sorted( \
                    room['periods'] \
                      | where(lambda p: p['status'] == 'available') \
                      | select(lambda p: p['time']) \
                  ) \
                  | first('N/A')}

def most_eap(rooms):
  return sorted(rooms \
                  | select(ealiest_avaiable_period) \
                  | where(lambda r: r['time'] != 'N/A'), \
          key=lambda x: x['time'] \
          ) \
          | first('No Availiable Room')



assert {'room_id': 1, 'time': '16:00-17:00'} == most_eap(rooms)

assert {'room_id': 2, 'time': '18:00-19:00'} == most_eap(only_ava_rooms)

assert 'No Availiable Room' == most_eap(no_ava_rooms)
