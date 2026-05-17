import datetime
import logging


def logger_hb():
    logger = logging.getLogger("hb_test")
    logger.setLevel(logging.WARNING)
    file_handler = logging.FileHandler("hb_test.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


def file_analyze(file: str):
    logger = logger_hb()
    key = "TSTFEED0300|7E3E|0400"

    filtered_file = []
    with open(file, "r") as file:
        for line in file:
            if key in line:
                filtered_file.append(line)

    previous_time = None

    for line in filtered_file:
        timestamp_index = line.find("Timestamp ")
        time_index = timestamp_index + len("Timestamp ")
        time_data = line[time_index : time_index + 8]
        time_data_formatted = datetime.datetime.strptime(time_data, "%H:%M:%S")
        if previous_time is None:
            previous_time = time_data_formatted
            continue
        time_difference = abs(
            int((time_data_formatted - previous_time).total_seconds())
        )

        if 31 < time_difference < 33:
            logger.warning(
                f"Time between events: {time_difference} second's! "
                f"Time snap event time: {previous_time.strftime('%H:%M:%S')} - "
                f"previous time snap event time: {time_data} "
            )

        elif 33 <= time_difference:
            logger.error(
                f"Heartbeat time more or equal 33 second: {time_difference} seconds! "
                f"Time snap event time: {previous_time.strftime('%H:%M:%S')} - "
                f"previous time snap event time: {time_data} "
            )

        else:
            pass

        previous_time = time_data_formatted


if __name__ == "__main__":
    file_analyze("hblog.txt")
