ps_command=r' Get-CimInstance -Class win32_quickfixengineering | Where-Object { $_.InstalledOn -gt (Get-Date).AddMonths(-3) }'

import subprocess
import ctypes

class disable_file_system_redirection:
    _disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
    _revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
    def __enter__(self):
        self.old_value = ctypes.c_long()
        self.success = self._disable(ctypes.byref(self.old_value))
    def __exit__(self, type, value, traceback):
        if self.success:
            self._revert(self.old_value)

with disable_file_system_redirection():
    process=subprocess.Popen('powershell "%s"'%ps_command, shell=True, stdout=subprocess.PIPE)
result=process.communicate()
ret=process.returncode
if ret==0:
    if result[0]:
        print result[0].strip()
    else:
        print None
        
else:
    print '%s\n%s'%(str(ret), str(result[1]))
