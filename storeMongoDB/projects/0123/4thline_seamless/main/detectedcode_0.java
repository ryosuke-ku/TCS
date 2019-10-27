    public static URI createAbsoluteURI(URI base, URI relativeOrNot) throws IllegalArgumentException {
        if (base == null && !relativeOrNot.isAbsolute()) {
            throw new IllegalArgumentException("Base URI is null and given URI is not absolute");
        } else if (base == null && relativeOrNot.isAbsolute()) {
            return relativeOrNot;
        } else {
            assert base != null;
            // If the given base URI has no path we give it a root path
            if (base.getPath().length() == 0) {
                try {
                    base = new URI(base.getScheme(), base.getAuthority(), "/", base.getQuery(), base.getFragment());
                } catch (Exception ex) {
                    throw new IllegalArgumentException(ex);
                }
            }
            return base.resolve(relativeOrNot);
        }
    }
