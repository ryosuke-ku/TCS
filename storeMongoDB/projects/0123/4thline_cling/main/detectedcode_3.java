    public String generate(DIDLContent content, boolean nestedItems) throws Exception {
        return documentToString(buildDOM(content, nestedItems), true);
    }
