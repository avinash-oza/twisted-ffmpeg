from collections import namedtuple
FileDescription = namedtuple('FileDescription', ['file_name', 'channel', 'time_period_start', 'time_period_end', 'ip_address', 'segment_date', 'full_source_path', 'output_file_name'], verbose=False)
FileDescription.__new__.__defaults__ = (None,) * len(FileDescription._fields)
