    public boolean hasProperty(java.lang.Class<? extends Property> propertyClass) {
        for (Property property : getProperties()) {
            if (propertyClass.isInstance(property)) return true;
        }
        return false;
    }
