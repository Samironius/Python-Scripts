import os, sys, rpm

path = sys.argv[1]
rpm_file = os.open("path", os.O_RDONLY)
ts = rpm.TransactionSet()
package = ts.hdrFromFdno(rpm_file)
print(package[rpm.RPMTAG_RELEASE])