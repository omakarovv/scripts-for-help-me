#!/usr/bin/env python3

class log_presenter:

    def proccess(self):
        with open('test_log.log', 'r') as f:
            while 1:
                for line in f:
                    self.log_collector(line)

    def log_collector(self, line):
         print(line)


if __name__ == '__main__':

    log_viewer = log_presenter()

    try:
        log_viewer.proccess()

    except TypeError:
        raise
