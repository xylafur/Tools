import re, sys

time_regex = re.compile(r"(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)")
_time_regex = re.compile(r"(\d\d):(\d\d):(\d\d),(\d\d\d)")
#13 seconds

def output_to_file(filename, lines):
    with open(filename, 'w') as f:
        for ii, line in enumerate(lines):
            f.write('{}\n'.format(ii + 1))
            f.write("{} --> {}\n".format(line['begin'], line['end']))
            for _line in line['lines']:
                f.write(_line + '\n')
            f.write('\n')

def increment_time(line, seconds):
    assert(seconds <= 60)
    match = re.search(_time_regex, line)
    hours, min, sec, mili = [int(each) for each in match.groups()[0:4]]

    sec += seconds
    if sec >= 60:
        min += sec // 60
        sec = sec % 60

    if min >= 60:
        hours += min // 60
        min = min % 60

    return "{:02d}:{:02d}:{:02d},{:03d}".format(hours, min, sec, mili)


def increment_times(lines, seconds):
    for line in lines:
        line['begin'] = increment_time(line['begin'], seconds)
        line['end'] = increment_time(line['end'], seconds)


def main(f):
    counter = 1
    lines = []
    for line in f:
        line = line.strip()
        if line == '':
            continue

        if line.isdigit():
            if int(line) == counter:
                counter += 1
                lines.append({})
        else:
            match = re.search(time_regex, line)
            if match:
                lines[counter - 2]['begin'] = match.groups()[0]
                lines[counter - 2]['end'] = match.groups()[1]
            else:
                if "lines" not in lines[counter - 2].keys():
                    lines[counter - 2]['lines'] = []
                lines[counter - 2]['lines'].append(line)
    return lines



if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("usage:\n{} <input filename> <output filename> "
              "<second offset>".format(sys.argv[0]))
        exit()
    _if = sys.argv[1]
    _of = sys.argv[2]
    sec = int(sys.argv[3])

    f = open(_if)
    lines = main(f)
    increment_times(lines, sec)
    output_to_file(_of, lines)
