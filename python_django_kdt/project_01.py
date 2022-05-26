my_station = [
        '야탑',
        '모란',
        '이매',
        '선릉',
        '한티',
        '왕십리',
    ]

# 1)
# def station_list():
#     for stations in my_station:
#         result = stations
#         print(result)
#
# station_list()

# 1) 정답
def station_list(station_list):
    for stations in station_list:
        print(stations)

station_list(my_station)


# 2)
# def station_point():
#     for stations in my_station:
#         if stations == '선릉':
#             print(stations)

# 2) 정답
def station_point(station_list):
    for stations in station_list:
        if stations == '선릉':
            print(stations)

station_point(my_station)