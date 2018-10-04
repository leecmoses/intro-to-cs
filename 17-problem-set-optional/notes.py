#############
#   Notes   #
# Lesson 17 #
#############

'''
Quiz: Latency
'''
speed_of_light = 300000. # km per second

def speed_fraction(traceroute,distance):
    time_in_seconds = traceroute / 1000.
    return (distance * 2 / time_in_seconds) / speed_of_light


'''
Quiz: Converting Seconds
'''
def convert_seconds(n):
    result = ''
    hour = int(n / 3600)
    minute = int(n % 3600 / 60)
    second = int(n % 3600 % 60)
    if hour == 1:
        result += str(hour) + ' hour, '
    else:
        result += str(hour) + ' hours, '
    if minute == 1:
        result += str(minute) + ' minute, '
    else:
        result += str(minute) + ' minutes, '
    if n == int(n):
        if second == 1:
            result += str(second) + ' second'
        else:
            result += str(second) + ' seconds'
    else:
        second = n % 3600 % 60.
        if second == 1:
            result += str(second) + ' second'
        else:
            result += str(second) + ' seconds'
    return result

'''
Quiz: Download Calculator
* Use prior function to help solve download calculator
'''
def band(str):
    if str == 'kb':
        return 2 ** 10
    if str == 'kB':
        return 2 ** 10 * 8
    if str == 'Mb':
        return 2 ** 20
    if str == 'MB':
        return 2 ** 20 * 8
    if str == 'Gb':
        return 2 ** 30
    if str == 'GB':
        return 2 ** 30 * 8
    if str == 'Tb':
        return 2 ** 40
    if str == 'TB':
        return 2 ** 40 * 8

def download_time(num1,str1,num2,str2):
    time = 1.0 * (num1 * band(str1)) / (num2 * band(str2))
    return convert_seconds(time)