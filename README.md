# tgscrack
Kerberos TGS_REP cracker written in Golang.  Wrote it as my first excercise in learning Go.

#Usage
Extract the encrypted service ticket parts from the TGS_REP message
```
python extractServiceTicketParts.py ticket.kirbi
```
Crack away: 
```
tgscrack -hashfile hashes.txt -wordlist rockyou.txt
```
# Building from source
```
go get github.com/leechristensen/tgscrack
go install github.com/leechristensen/tgscrack
```
# Credits
Tim Medin(@timmedin) for his work on Kerberoast
 - https://github.com/nidem/kerberoast
 - http://www.irongeek.com/i.php?page=videos/derbycon4/t120-attacking-microsoft-kerberos-kicking-the-guard-dog-of-hades-tim-medin

Benjamin Delphi(@gentilkiwi)
 - TGS ticket creation in Mimikatz
