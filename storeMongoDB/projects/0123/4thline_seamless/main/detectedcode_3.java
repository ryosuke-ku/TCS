    public static URL createAbsoluteURL(InetAddress address, int localStreamPort, URI relativeOrNot) throws IllegalArgumentException {
        try {
            if (address instanceof Inet6Address) {
                return createAbsoluteURL(new URL("http://[" + address.getHostAddress() + "]:" + localStreamPort), relativeOrNot);
            } else if (address instanceof Inet4Address) {
                return createAbsoluteURL(new URL("http://" + address.getHostAddress() + ":" + localStreamPort), relativeOrNot);
            } else {
                throw new IllegalArgumentException("InetAddress is neither IPv4 nor IPv6: " + address);
            }
        } catch (Exception ex) {
            throw new IllegalArgumentException("Address, port, and URI can not be converted to URL", ex);
        }
    }
