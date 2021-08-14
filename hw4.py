import os
import rpm




rpm_file = os.open("apacheds-2.0.0.AM26-x86_64.rpm", os.O_RDONLY)
ts = rpm.TransactionSet()
package = ts.hdrFromFdno(rpm_file)
print("RELEASE...:", package[rpm.RPMTAG_RELEASE])