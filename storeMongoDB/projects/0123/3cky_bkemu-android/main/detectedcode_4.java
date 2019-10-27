    public boolean write(boolean isByteMode, int address, int value) {
        if (isByteMode) {
            writeByte(address, value);
        } else {
            writeWord(address, value);
        }
        return true;
    }
