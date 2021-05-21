# Requires PuTTY / PLINK

$Username1 = "root"
$Username2 = "admin"
$Username3 = "user"
$Password = "password"
$IPAddresses = "192.168.0.X","192.168.0.X"

foreach ($IP in $IPAddresses) {
        "hostname","date","exit" | plink.exe -P 22 $Username1@$IP -pw $Password ; 
        "hostname","date","exit" | plink.exe -P 22 $Username2@$IP -pw $Password ;
        "hostname","date","exit" | plink.exe -P 22 $Username3@$IP -pw $Password
}