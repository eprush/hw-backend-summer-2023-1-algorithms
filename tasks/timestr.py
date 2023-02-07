__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """

    def add_time(time, time_name):
        return "0" + str(time) + time_name if (time < 10) else str(time) + time_name

    def cut_time(res):
        if len(res) < 4:
            return res

        if not int(res[0]) and not int(res[1]):
            res = res[3:]
            return cut_time(res)
        return res

    result  = ""
    s       = seconds%60
    minutes = (seconds//60)%60
    hours   = (seconds//3600)%24
    days    = seconds//(3600*24)
    arr   = [days, hours, minutes, s]
    times = ["d", "h", "m", "s"]
    for i in range(len(arr)):
        result += add_time(arr[i], times[i])
    return cut_time(result)
