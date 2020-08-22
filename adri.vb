' String to search in.
Dim searchString As String = "XXpXXpXXPXXP"
' Search for "P".
Dim searchChar As String = "P"

Dim testPos As Integer
' A textual comparison starting at position 4. Returns 6.
testPos = InStr(4, searchString, searchChar, CompareMethod.Text)

' A binary comparison starting at position 1. Returns 9.
testPos = InStr(1, SearchString, SearchChar, CompareMethod.Binary)

' If Option Compare is not set, or set to Binary, return 9.
' If Option Compare is set to Text, returns 3.
testPos = InStr(searchString, searchChar)

' Returns 0.
testPos = InStr(1, searchString, "W")

Dim testDateTime As Date = #1/27/2001 5:04:23 PM#
Dim testStr As String
' Returns current system time in the system-defined long time format.
testStr = Format(Now(), "Long Time")
' Returns current system date in the system-defined long date format.
testStr = Format(Now(), "Long Date")
' Also returns current system date in the system-defined long date 
' format, using the single letter code for the format.
testStr = Format(Now(), "D")

' Returns the value of testDateTime in user-defined date/time formats.
' Returns "5:4:23".
testStr = Format(testDateTime, "h:m:s")
' Returns "05:04:23 PM".
testStr = Format(testDateTime, "hh:mm:ss tt")
' Returns "Saturday, Jan 27 2001".
testStr = Format(testDateTime, "dddd, MMM d yyyy")
' Returns "17:04:23".
testStr = Format(testDateTime, "HH:mm:ss")
' Returns "23".
testStr = Format(23)

' User-defined numeric formats.
' Returns "5,459.40".
testStr = Format(5459.4, "##,##0.00")
' Returns "334.90".
testStr = Format(334.9, "###0.00")
' Returns "500.00%".
testStr = Format(5, "0.00%")

Dim testDateTime As Date = #1/27/2001 5:04:23 PM#
Dim testStr As String
' Returns current system time in the system-defined long time format.
testStr = Format(Now(), "Long Time")
' Returns current system date in the system-defined long date format.
testStr = Format(Now(), "Long Date")
' Also returns current system date in the system-defined long date 
' format, using the single letter code for the format.
testStr = Format(Now(), "D")

' Returns the value of testDateTime in user-defined date/time formats.
' Returns "5:4:23".
testStr = Format(testDateTime, "h:m:s")
' Returns "05:04:23 PM".
testStr = Format(testDateTime, "hh:mm:ss tt")
' Returns "Saturday, Jan 27 2001".
testStr = Format(testDateTime, "dddd, MMM d yyyy")
' Returns "17:04:23".
testStr = Format(testDateTime, "HH:mm:ss")
' Returns "23".
testStr = Format(23)

' User-defined numeric formats.
' Returns "5,459.40".
testStr = Format(5459.4, "##,##0.00")
' Returns "334.90".
testStr = Format(334.9, "###0.00")
' Returns "500.00%".
testStr = Format(5, "0.00%")
Dim testDateTime As Date = #1/27/2001 5:04:23 PM#
Dim testStr As String
' Returns current system time in the system-defined long time format.
testStr = Format(Now(), "Long Time")
' Returns current system date in the system-defined long date format.
testStr = Format(Now(), "Long Date")
' Also returns current system date in the system-defined long date 
' format, using the single letter code for the format.
testStr = Format(Now(), "D")

' Returns the value of testDateTime in user-defined date/time formats.
' Returns "5:4:23".
testStr = Format(testDateTime, "h:m:s")
' Returns "05:04:23 PM".
testStr = Format(testDateTime, "hh:mm:ss tt")
' Returns "Saturday, Jan 27 2001".
testStr = Format(testDateTime, "dddd, MMM d yyyy")
' Returns "17:04:23".
testStr = Format(testDateTime, "HH:mm:ss")
' Returns "23".
testStr = Format(23)

' User-defined numeric formats.
' Returns "5,459.40".
testStr = Format(5459.4, "##,##0.00")
' Returns "334.90".
testStr = Format(334.9, "###0.00")
' Returns "500.00%".
testStr = Format(5, "0.00%")
Dim testDateTime As Date = #1/27/2001 5:04:23 PM#
Dim testStr As String
' Returns current system time in the system-defined long time format.
testStr = Format(Now(), "Long Time")
' Returns current system date in the system-defined long date format.
testStr = Format(Now(), "Long Date")
' Also returns current system date in the system-defined long date 
' format, using the single letter code for the format.
testStr = Format(Now(), "D")

' Returns the value of testDateTime in user-defined date/time formats.
' Returns "5:4:23".
testStr = Format(testDateTime, "h:m:s")
' Returns "05:04:23 PM".
testStr = Format(testDateTime, "hh:mm:ss tt")
' Returns "Saturday, Jan 27 2001".
testStr = Format(testDateTime, "dddd, MMM d yyyy")
' Returns "17:04:23".
testStr = Format(testDateTime, "HH:mm:ss")
' Returns "23".
testStr = Format(23)

' User-defined numeric formats.
' Returns "5,459.40".
testStr = Format(5459.4, "##,##0.00")
' Returns "334.90".
testStr = Format(334.9, "###0.00")
' Returns "500.00%".
testStr = Format(5, "0.00%")