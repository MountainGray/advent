from advent import get_input, solution_timer
from collections import defaultdict

guards = defaultdict(lambda: defaultdict(int))

@solution_timer(2018, 4, 1)
def part_one(inp):

    # [1518-08-17 00:01] Guard #3529 begins shift
    # [1518-07-07 00:21] falls asleep
    log = []
    for i in inp:
        ymd, time, *text = i.split()
        year, month, day = ymd[1:].split("-")
        hour, minute = time[:-1].split(":")
        vals = (year, month, day, hour, minute)
        vals = (*[int(i) for i in vals], text)
        log.append(vals)
    log.sort()

    #guards = defaultdict(lambda: defaultdict(int))
    cur_guard = 0
    start_hour = 0
    start_min = 0

    for i in log:
        *date, text = i
        if text[0] == "Guard":
            cur_guard = int(text[1][1:])
        elif text[0] == "falls":
            *_, start_hour, start_min = date
        else:
            *_, end_hour, end_minute = date

            while (start_hour, start_min) != (end_hour, end_minute):
                guards[cur_guard][start_min] += 1

                if start_min == 59:
                    start_min = 0
                    start_hour += 1; start_hour %= 24
                else:
                    start_min += 1
            guards[cur_guard][start_min] += 1 # end inclusive

    sleep_sums = list(map(lambda x: (x[0], sum(x[1].values())), guards.items()))
    sleepiest = max(sleep_sums, key=lambda x: x[1])
    sleepiest_guard = sleepiest[0]
    sleepiest_minute = max(guards[sleepiest_guard].items(), key=lambda x: x[1])[0]

    return sleepiest_guard * sleepiest_minute


@solution_timer(2018, 4, 2)
def part_two():
    pair = max(guards.items(), key=lambda x: max(x[1].values()))
    guard = pair[0]
    minute = max(pair[1].items(), key=lambda x: x[1])[0]
    return guard * minute


#submit(2018,4,1,ans)

if __name__ == "__main__":
    inp = get_input(2018, 4)
    part_one(inp)
    part_two()

