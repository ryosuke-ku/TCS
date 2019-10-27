    public synchronized int read(long cpuTime, int address) {
        setLastAccessCpuTime(cpuTime);
        return (address == CONTROL_REGISTER_ADDRESS)
                ? readControlRegister(cpuTime)
                : readDataRegister(cpuTime);
    }
