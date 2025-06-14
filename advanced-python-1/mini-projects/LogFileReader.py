import random
from datetime import datetime, timedelta

def log_generator(line_count):
    ips = ["192.168.0." + str(i) for i in range(1, 50)]
    methods = ["GET", "POST", "DELETE", "PUT"]
    resources = ["/", "/index.html", "/about", "/login", "/logout"]
    status_codes = [200, 301, 404, 500]

    current_time = datetime.now()

    for _ in range(line_count):
        ip = random.choice(ips)
        method = random.choice(methods)
        resource = random.choice(resources)
        status = random.choice(status_codes)
        date_str = current_time.strftime("%d/%b/%Y:%H:%M:%S +0000")
        yield f"{ip} - - [{date_str}] \"{method} {resource} HTTP/1.1\" {status} {random.randint(100, 5000)}\n"
        current_time += timedelta(seconds=random.randint(1, 5))

with open("access.log", "w") as f:
    for line in log_generator(1_000):  
        f.write(line)
# bu kod 1000 satırlık random log dosyası oluşturur.

# dosyayı generator ile okuma
def read_log_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line

# iterator ile filtreleme
class StatusCodeFilter:
    def __init__(self,lines, status_code):
        self.lines = lines
        self.status_code = status_code

    def __iter__(self):
        for line in self.lines:
            if f"{self.status_code}" in line:
                yield line

    def __next__(self):
        try:
            return next(self.lines)
        except StopIteration:
            raise StopIteration

lines = read_log_file("access.log")
filtered_lines = StatusCodeFilter(lines, 404)

for line in filtered_lines:
    print(line)



