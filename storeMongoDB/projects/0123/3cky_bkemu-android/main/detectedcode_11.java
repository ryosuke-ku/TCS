    protected FloppyDrive getFloppyDrive(FloppyDriveIdentifier drive) {
        return (drive != null) ? floppyDrives[drive.ordinal()] : null;
    }
