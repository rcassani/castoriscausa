
# .bat file
    net stop OVRService
    xcopy "C:\Program Files\Oculus" "D:\Oculus" /O /X /E /H /K /-Y
    rmdir /S /Q "C:\Program Files\Oculus"
    mklink /D "C:\Program Files\Oculus" "D:\Oculus"
    net start OVRService