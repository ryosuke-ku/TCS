    public int read(boolean isByteMode, int address) {
        return isByteMode ? readByte(address) : readWord(address);
    }
