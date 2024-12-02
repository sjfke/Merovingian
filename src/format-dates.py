import pytz                                                          # python IANA timezone implementation
import tzlocal                                                       # python local time-zone
from pytz import timezone
from tzlocal import get_localzone
from datetime import datetime
epoch = 1682490209                                                   # UNIX epoch (naive, no time-zone)
dt_format = "%Y-%m-%d %H:%M:%S %Z%z"
dt = datetime.fromtimestamp(epoch).replace(tzinfo=pytz.UTC)          # make UTC datetime (time-zone aware)
print(dt.strftime(dt_format))                                        # 2023-04-26 08:23:29 UTC+0000
print(dt.astimezone(timezone('Europe/Zurich')).strftime(dt_format))  # 2023-04-26 10:23:29 CEST+0200
print(dt.astimezone(get_localzone()).strftime(dt_format))            # 2023-04-26 10:23:29 CEST+0200
