'''
This files contains an example script of how to read Windows event logs using Python.
The script uses the win32evtlog module to read the logs.
The script reads the logs in reverse order, so it can get the latest events.
Requires admin privileges to read security logs.
'''

import win32evtlog
import win32evtlogutil

# Print all the available methods and attributes of win32evtlog
# print(dir(win32evtlog))

# Set the log server
log_server = 'localhost'
log_type = 'Application' # Choices include 'Application', 'Setup', 'Security', 'System' (Note: For security logs, need admin privileges)

read_log = win32evtlog.OpenEventLog(log_server, log_type)

# We need to send a flag to read the log in reverse order, so we can get the latest events
# Flags determine how the logs is read
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

offset = 0

while True:
    try:
        event_logs = win32evtlog.ReadEventLog(read_log, flags, offset)

        if event_logs:
            for event_log in event_logs:
                print('Event Category:', event_log.EventCategory)
                print('Time Generated:', event_log.TimeGenerated)
                print('Record Number:', event_log.RecordNumber)
                print('Source Name:', event_log.SourceName)
                print('Event ID: ', event_log.EventID)
                print('Event Type:', event_log.EventType)
                print('Event Description:', win32evtlogutil.SafeFormatMessage(event_log, log_type))
                print('Computer:', event_log.ComputerName)
                print('User:', event_log.StringInserts[0] if event_log.StringInserts else None)
                print('-----------------------------------------------------------------------------------')

                # Event Category: 0
                # Time Generated: 2023-06-17 10:59:53
                # Record Number: 11125
                # Source Name: igccservice
                # Event ID:  0
                # Event Type: 4
                # Event Description: PowerEvent handled successfully by the service.

                # Computer: DESKTOP-HEIO2DT
                # User: PowerEvent handled successfully by the service.
                # -----------------------------------------------------------------------------------
    except KeyboardInterrupt:
        print('Program terminated by user')
        print('-----------------------------------------------------------------------------------')
        break