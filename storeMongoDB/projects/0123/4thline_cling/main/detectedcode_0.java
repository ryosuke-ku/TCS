    public DIDLObject addProperty(Property property) {
        if (property == null) return this;
        getProperties().add(property);
        return this;
    }
