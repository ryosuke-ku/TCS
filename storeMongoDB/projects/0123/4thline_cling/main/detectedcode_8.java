        public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
            super.startElement(uri, localName, qName, attributes);

            Element newEl = getInstance().getMetadata().createElementNS(uri, qName);
            for (int i = 0; i < attributes.getLength(); i++) {
                newEl.setAttributeNS(
                    attributes.getURI(i),
                    attributes.getQName(i),
                    attributes.getValue(i)
                );
            }
            current.appendChild(newEl);
            current = newEl;
        }
