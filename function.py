import re


def parse_time(time_string):
    hours = int(re.findall(r'(\d+):\d+:\d+,\d+', time_string)[0])
    minutes = int(re.findall(r'\d+:(\d+):\d+,\d+', time_string)[0])
    seconds = int(re.findall(r'\d+:\d+:(\d+),\d+', time_string)[0])
    milliseconds = int(re.findall(r'\d+:\d+:\d+,(\d+)', time_string)[0])

    if hours < 10:
    	hours = f"0{hours}"
    if minutes < 10:
    	minutes = f"0{minutes}"
    if seconds < 10:
    	seconds = f"0{seconds}"
    if milliseconds < 10:
    	milliseconds = f"0{milliseconds}"
    	
    return f"{hours}:{minutes}:{seconds}.{milliseconds}"


def parse_srt(srt_string):
    srt_list = []

    for line in srt_string.split('\n\n'):
        if line != '':
            index = int(re.match(r'\d+', line).group())

            pos = re.search(r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+',
                            line).end() + 1
            content = line[pos:]
            start_time_string = re.findall(
                r'(\d+:\d+:\d+,\d+) --> \d+:\d+:\d+,\d+', line)[0]
            end_time_string = re.findall(
                r'\d+:\d+:\d+,\d+ --> (\d+:\d+:\d+,\d+)', line)[0]
            start_time = parse_time(start_time_string)
            end_time = parse_time(end_time_string)

            srt_list.append({
                'index': index,
                'content': content,
                'start': start_time,
                'end': end_time
            })

    return srt_list


def set_input_name(name):
    input_name = name.replace("\n", " ").replace(" ", "0").replace("-", "[oo]").replace(".", "2").replace(",", "3").replace("?", "4")
    return input_name


def set_output_name(name):
    output_name = name.replace("0", " ").replace("[oo]", "-").replace("2", "").replace("3", ",").replace("mp4", "").replace("4", "[qm]").replace(".", "").strip()
    return output_name
