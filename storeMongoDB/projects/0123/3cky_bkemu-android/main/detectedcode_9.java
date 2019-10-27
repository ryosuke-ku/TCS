    public synchronized void mountDiskImage(String diskImageFileUri, FloppyDriveIdentifier drive,
            boolean isReadOnly) throws Exception {
        getFloppyDrive(drive).mountDiskImage(diskImageFileUri, isReadOnly);
    }
