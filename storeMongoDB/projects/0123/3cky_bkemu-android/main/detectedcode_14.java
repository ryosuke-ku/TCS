    public synchronized boolean write(long cpuTime, boolean isByteMode, int address, int value) {
        if (isDebugEnabled) {
            d(TAG, "write: " + Integer.toOctalString(address) +
                    ", value: " + Integer.toOctalString(value) + ", isByteMode: " + isByteMode);
        }
        setLastAccessCpuTime(cpuTime);
        if (!isByteMode) {
            if (address == CONTROL_REGISTER_ADDRESS) {
                writeControlRegister(cpuTime, value);
            } else {
                writeDataRegister(cpuTime, value);
            }
        }
        return true;
    }
