
function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}

function Date{
    (Get-Date).DayOfWeek
    (Get-Date).Date
}

$IPADDRESS = getIP
$USER = $env:USERNAME
$HOSTNAME = hostname
$VERSION = $HOST.Version.Major
$DATE = Date

$BODY = "This machine's IP is $IPADDRESS. User is $USER. Hostname is $HOSTNAME. PowerShell Version $VERSION. Today's Date is $DATE"

Send-MailMessage -To "zinkjm@mail.uc.edu" -From "judizink1@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)