    public static String encode(BitSet allowedCharacters, String s, String charset) {
        if (s == null)
            return null;
        final StringBuilder encoded = new StringBuilder(s.length() * 3);
        final char[] characters = s.toCharArray();
        try {
            for (char c : characters) {
                if (allowedCharacters.get(c)) {
                    encoded.append(c);
                } else {
                    byte[] bytes = String.valueOf(c).getBytes(charset);
                    for (byte b : bytes)
                        encoded.append(String.format("%%%1$02X", b & 0xFF));
                }
            }
        } catch (Exception ex) {
            throw new RuntimeException(ex);
        }
        return encoded.toString();
    }
